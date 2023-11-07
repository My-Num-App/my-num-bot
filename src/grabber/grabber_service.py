from selenium import webdriver

from src.util.check_path import check_path
import src.config.general as conf
import src.config.element_paths as element_conf
import re

driver = webdriver.Chrome()


def wait_for_elements(path):
    enabled = is_element_exists(path)
    if enabled:
        return driver.find_elements('xpath', path)
    while not enabled:
        try:
            elm = driver.find_elements('xpath', path)
            print('found it')
            return elm
        except:
            print('trying to find...')


def is_element_exists(path):
    try:
        driver.find_element('xpath', path)
        return True
    except:
        return False


def wait_for_element(path):
    enabled = is_element_exists(path)
    if enabled:
        return driver.find_element('xpath', path)
    while not enabled:
        try:
            elm = driver.find_element('xpath', path)
            print('found it')
            return elm
        except:
            print('trying to find...')


def search_model(i):
    if i < 2:
        i = 2
    try:

        wait_for_element(element_conf.GET_MODELS_BUTTON).click()
        wait_for_element(f'/html/body/div[4]/div[3]/form/div/div[2]/div[1]/div/div[2]/div/div[{i}]').click()
        wait_for_element(element_conf.SEARCH_BUTTON).click()
        return driver.current_url
    except:
        print('cannot complete search_model action')
        exit(1)


def get_model_count():
    driver.get(conf.TURBO_AZ)
    wait_for_element(element_conf.GET_MODELS_BUTTON).click()
    count = wait_for_elements('/html/body/div[4]/div[3]/form/div/div[2]/div[1]/div/div[2]/div/div')
    driver.close()
    return len(count)


def get_post_count():
    count_str = wait_for_element(element_conf.POST_COUNT_PATH).text
    try:
        count = re.findall("[0-9]", count_str)[0]
        return int(count)
    except:
        return 1


def get_next_page(i):
    try:
        if i < 2:
            i = 2
        next_page_path = f'/html/body/div[4]/div[3]/div[2]/div/div[6]/nav/span[{i}]'
        driver.find_element('xpath', next_page_path).click()
        return driver.current_url
    except:
        print('cannot find page')
        return None


def setup():
    count = get_model_count()
    for i in range(2, count):
        search_model(i)
        urls = get_urls(None)
        for url in urls:
            get_data(url)

        f = 2
        while True:
            next_page_url = get_next_page(f)
            if next_page_url is None:
                driver.close()
                break
            urls = get_urls(next_page_url)
            for url in urls:
                get_data(url)
            f += 1


def get_urls(page_url):
    if page_url is not None:
        driver.get(conf.TURBO_AZ)

    urls = []
    for i in range(1, get_post_count()):
        try:
            url_path = f'/html/body/div[4]/div[3]/div[2]/div/div[1]/div[2]/div[{i}]/a[1]'

            url = driver.find_element('xpath', url_path)

            urls.append(url.get_attribute('href'))
        except:
            print('[x] path is not found')

    print('Urls grabbed from a page ->', urls)
    return urls


def get_data(post_url):
    phone_number = ''
    print(post_url)
    driver.get(post_url)

    path = check_path(driver, element_conf.SHOW_NUM_BUTTON_PATHS)

    if path is not None:
        show_num_button = driver.find_element('xpath', path)
        show_num_button.click()

    num_path = check_path(driver, element_conf.NUMBER_PATHS)
    if num_path is not None and path is not None:
        phone_number = driver.find_element('xpath', num_path).text

    print('phone number:', phone_number)
