import argparse
import sys
import requests
import logging
import os
import re
from bs4 import BeautifulSoup
from page_loader.functions import GetPageNames, save, save_page_src


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
    except FileExistsError:
        err_msg = f'Directory "{page.get_dir_name()}" is already exist'
        logging.error(err_msg)
        raise FileExistsError(2, err_msg)
    except OSError:
        err_msg = f'Output directory "{os.path.abspath(path)}" do not exist.'
        logging.error(err_msg)
        raise OSError(2, err_msg)
    logging.info('Download a page: %s', link)
    try:
        page_data = requests.get(link)
        page_data.raise_for_status()
    except requests.RequestException as e:
        err_msg = f'Cannot get page: {link} due to {e}'
        logging.error(err_msg)
        logging.info('Remove directory: %s', page.get_dir_name())
        os.rmdir(page.get_dir_path())
        raise ConnectionError(2, err_msg)
    html = BeautifulSoup(page_data.content, 'html.parser')
    href_list = html.find_all('link', {'href': re.compile('.*')})
    src_list = html.find_all(['img', 'script'], attrs={'src': re.compile('.*')})
    logging.info('Start to dowload a page\'s source.')
    save_page_src(href_list, page, 'href')
    save_page_src(src_list, page, 'src')
    logging.info('Save a page: %s', page.page_name)
    save(page.get_path(), html.prettify(), 'w')
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
    parser.add_argument('-o', '--output', metavar='PATH',
                        dest='path', default=os.getcwd(), type=str,
                        help='a directory path to save a page(should be exist) \
                        (default: CWD)')
    args = parser.parse_args()
    try:
        file_path = download(args.link, args.path)
    except IOError as e:
        sys.exit(e.errno)
    print(file_path)
