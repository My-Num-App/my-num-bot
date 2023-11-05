from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


def get_urls():
    driver = webdriver.Chrome(chrome_options)

    url = 'https://turbo.az'

    driver.get(url)

    urls = []
    for i in range(1, 10):
        try:
            title = f'/html/body/div[4]/div[3]/div/div/section[1]/div[2]/div[1]/div[{i}]/a[1]'

            titles = driver.find_element('xpath', title)

            urls.append(titles.get_attribute('href'))
        except:
            print('an error occurred')

    driver.close()
    return urls


def get_data(post_url):
    post_data = []
    driver = webdriver.Chrome(chrome_options)

    driver.get(post_url)

    # show_num_button_xpath = '/html/body/div[2]/div[3]/div[2]/div[2]/div/aside/div/div[1]/div[2]/div[3]/div[1]'
    show_num_button_xpath = '/html/body/div[4]/div[3]/div[2]/div[2]/div/aside/div/div[1]/div[4]/div[1]'
    show_num_button = driver.find_element('xpath', show_num_button_xpath)

    show_num_button.click()

    # number_xpath = '/html/body/div[4]/div[3]/div[2]/div[2]/div/aside/div/div[1]/div[4]/div[2]/div[1]/a'
    number_xpath = '/html/body/div[2]/div[3]/div[2]/div[2]/div/aside/div/div[1]/div[2]/div[3]/div[2]/div/a'
    phone_number = driver.find_element('xpath', number_xpath).text
    post_data.append(['number', phone_number])

    print(post_data)
    driver.close()


def main():
    for post_url in get_urls():
        get_data(post_url)


if __name__ == '__main__':
    main()

