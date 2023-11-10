from src.grabber.grabber_service import get_content, get_parsed_page
from src.parser.parse_service import parse_make_urls
from src.config.general import TURBO_AZ


def setup():
    content = get_content(TURBO_AZ)
    make_urls = parse_make_urls(content)
    for make_url in make_urls:
        get_parsed_page(make_url)


def main():
    setup()


if __name__ == '__main__':
    main()
