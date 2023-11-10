import math
from requests import request
import src.config.general as conf
import src.parser.parse_service as parse_service


def get_content(url):
    headers = {
        'User-Agent': conf.USER_AGENT
    }
    response = request(conf.GET, url, headers=headers)
    return response.text


def parse_post_by_url(post_urls):
    for post_url in post_urls:
        print('page =>', post_url)
        post_content = parse_service.get_post_content(get_content(f'{conf.TURBO_AZ}{post_url}'))
        print(f'{post_content.num_owner}\'s phone number is {post_content.phone_numbers} and lives in {post_content.num_owner_location}')


def get_parsed_page(url):
    make_content = get_content(f'{conf.TURBO_AZ}{url}')
    parsed_make_content = parse_service.parse_make_content(make_content)
    count = parse_service.post_count(make_content)
    parse_post_by_url(parsed_make_content.post_urls)
    next_page_url = parsed_make_content.next_page_url
    if next_page_url:
        for _ in range(1, math.ceil(count/6)):
            if next_page_url is None:
                return
            print('Getting the url...', f'{conf.TURBO_AZ}{next_page_url}')
            next_make_content = get_content(f'{conf.TURBO_AZ}{next_page_url}')
            parsed_make_content = parse_service.parse_make_content(next_make_content)
            parse_post_by_url(parsed_make_content.post_urls)
