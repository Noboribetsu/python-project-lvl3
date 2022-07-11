import argparse
import requests
import os
from bs4 import BeautifulSoup
from page_loader.functions import GetPageNames, save, save_page_src
import re


def download(link, path):
    """
        Downdload a web-site page by a link and
        save it to an existing directory.
    """
    if os.path.exists(path):
        page = GetPageNames(link, path)
        page_data = requests.get(link)
        html = BeautifulSoup(page_data.text, 'html.parser')
        os.mkdir(page.get_dir_path())
        list(map(
            lambda x: save_page_src(x, page, 'href'),
            html.find_all('link', {'href': re.compile('.*')})
        ))
        list(map(
            lambda x: save_page_src(x, page, 'src'),
            html.find_all(['img', 'script'], attrs={'src': re.compile('.*')})
        ))
        save(page.get_path(), html.prettify())
        return page.get_path()
    else:
        raise NameError('A directory do no exist!')


def page_loader():
    """
        Parse arguments for CLI: path, link.
        Call download function with parsed arguments.
        Print result - actual path of a dowloaded page.
    """
    parser = argparse.ArgumentParser(
        description='Download a page by a web-site \
         link and save it to a mentioned directory.'
    )
    parser.add_argument('link', metavar='LINK',
                        type=str, help='a link on a page that should be loaded')
    parser.add_argument('--output', metavar='PATH',
                        dest='path', default=os.getcwd(), type=str,
                        help='a directory path to save a page(should be exist) \
                        (default: CWD)')
    args = parser.parse_args()
    file_path = download(args.link, args.path)
    print(file_path)
