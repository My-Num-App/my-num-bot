import re
import src.config.element_paths as elm_paths
import src.util.element_parser_util as util
from src.object.make_content import MakeContent
from src.object.post_content import PostContent


def parse_make_urls(content):
    make_urls = util.get_html_tags_hrefs_by_path(content, elm_paths.MAKE_PATH)
    return make_urls


def parse_make_content(content):
    post_urls = util.get_html_tags_hrefs_by_path(content, elm_paths.POST_URL_PATH)
    next_page_url = util.get_html_tag_href_by_path(content, elm_paths.NEXT_PAGE_URL_PATH)

    return MakeContent(next_page_url, post_urls)


def get_post_content(content):
    phone_numbers = util.get_html_tags_texts(content, elm_paths.PHONE_NUMBER_PATH)
    num_owner = util.get_html_tag_text_by_paths(content, elm_paths.PHONE_NUMBER_OWNER_PATHS)
    num_owner_location = util.get_html_tag_text_by_path(content, elm_paths.PHONE_NUMBER_OWNER_LOCATION_PATH)

    return PostContent(num_owner, phone_numbers, num_owner_location)


def post_count(content):
    count = 0
    count_elm = util.get_html_tag_text_by_path(content, elm_paths.POST_COUNT)
    if count_elm:
        count = re.findall("[0-9]+", count_elm)[0]
    return int(count)
