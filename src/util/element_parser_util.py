from bs4 import BeautifulSoup


def get_html_tags_texts(content, path):
    tag_texts = set()
    soup = BeautifulSoup(content, 'html.parser')
    html_elms = soup.select(path)
    for html_elm in html_elms:
        tag_texts.add(html_elm.text)
    return tag_texts


def get_html_tag_text_by_paths(content, paths):
    tag_text = None
    soup = BeautifulSoup(content, 'html.parser')
    for path in paths:
        html_elms = soup.select(path)
        if html_elms:
            tag_text = html_elms[0].text
    return tag_text


def get_html_tag_text_by_path(content, path):
    tag_text = None
    soup = BeautifulSoup(content, 'html.parser')
    html_elms = soup.select(path)
    if html_elms:
        tag_text = html_elms[0].text
    return tag_text


def get_html_tag_href_by_path(content, path):
    tag_href = None
    soup = BeautifulSoup(content, 'html.parser')
    html_elms = soup.select(path)
    if html_elms:
        tag_href = html_elms[0].attrs.get('href')
    return tag_href


def get_html_tags_hrefs_by_path(content, path):
    tag_hrefs = set()
    soup = BeautifulSoup(content, 'html.parser')
    html_elms = soup.select(path)
    for html_elm in html_elms:
        tag_hrefs.add(html_elm.attrs.get('href'))
    return tag_hrefs
