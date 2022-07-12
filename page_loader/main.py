import argparse
import sys
import requests
import logging
import os
from bs4 import BeautifulSoup
from page_loader.functions import GetPageNames, save, save_page_src
import re


def download(link, path):
    """
        Downdload a web-site page by a link witl all loacal sources and
        save it to an existing directory.
    """
    page = GetPageNames(link, path)
    try:
        os.mkdir(page.get_dir_path())
        logging.basicConfig(level=logging.INFO)
        logging.info(
            'Create directory for page\'s files: %s',
            page.get_dir_path()
        )
    except OSError:
        err_msg = f'Output directory "{os.path.abspath(path)}" do not exist.'
        logging.error(err_msg)
        raise OSError(2, err_msg)
    logging.info('Dowload a page: %s', link)
    try:
        page_data = requests.get(link)
        page_data.raise_for_status()
    except requests.RequestException as e:
        err_msg = f'Cannot get page: {link} due to {e}'
        logging.error(err_msg)
        raise ConnectionError(2, err_msg)
    html = BeautifulSoup(page_data.text, 'html.parser')
    any(map(
        lambda x: save_page_src(x, page, 'href'),
        html.find_all('link', {'href': re.compile('.*')})
    ))
    any(map(
        lambda x: save_page_src(x, page, 'src'),
        html.find_all(['img', 'script'], attrs={'src': re.compile('.*')})
    ))
    logging.info('Save a page data: %s', page.page_name)
    save(page.get_path(), html.prettify())
    return page.get_path()


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
    try:
        file_path = download(args.link, args.path)
    except IOError as e:
        logging.error(e.strerror)
        sys.exit(e.errno)
    print(file_path)
