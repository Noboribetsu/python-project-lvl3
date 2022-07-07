import argparse
import requests
import os
from urllib.parse import urlparse


def get_file_name(link):
    """ Make a file name from a link"""
    file_name = []
    url = urlparse(link)
    file_name.append(url.netloc.replace('.', '-'))
    file_name.append(url.path.replace('/', '-'))
    if not url.path.endswith('.html'):
        file_name.append('.html')
    return ''.join(file_name)


def download(link, path):
    """
        Downdload a web-site page by a link and
        save it to an existing directory.
    """
    if os.path.exists(path):
        try:
            r = requests.get(link)
        except requests.RequestException as error:
            print('Requests error:', error)
        file_path = os.path.join(path, get_file_name(link))
        with open(file_path, 'w') as f:
            f.write(r.text)
        return file_path
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
