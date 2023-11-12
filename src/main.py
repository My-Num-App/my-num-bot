from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.grabber.grabber_service import get_content, get_parsed_page
from src.parser.parse_service import parse_make_urls
from src.config.general import TURBO_AZ
from src.database.database_service import DatabaseService


def setup(db):
    content = get_content(TURBO_AZ)
    make_urls = parse_make_urls(content)
    for make_url in make_urls:
        get_parsed_page(make_url, db)


def main():
    db_service = DatabaseService()
    setup(db_service)


if __name__ == '__main__':
    main()
