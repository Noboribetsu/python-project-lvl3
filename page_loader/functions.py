import logging
import os
from urllib.parse import urlparse
import requests
from progress.spinner import Spinner


class GetPageNames():
    """
        Class for page.
        Make all neccesary names,paths of page, page's src.
    """
    def __init__(self, link, path):
        url = urlparse(link)
        name = []
        self.scheme = url.scheme
        self.netloc = url.netloc
        name.append(url.netloc.replace('.', '-'))
        name.append(url.path.replace('/', '-') if len(url.path) > 1 else '')
        name.append('_files')
        self.dir_name = ''.join(name)
        name.pop()
        self.dir_path = os.path.join(path, self.dir_name)
        if url.path.endswith('.html'):
            self.page_name = ''.join(name)
        else:
            name.append('.html')
            self.page_name = ''.join(name)
        self.page_path = os.path.join(
            os.path.abspath(path), self.page_name
        )

    def get_path(self):
        return self.page_path

    def get_dir_path(self):
        return self.dir_path

    def get_dir_name(self):
        return self.dir_name

    def ispagelink(self, link):
        url = urlparse(link)
        if url.netloc:
            if url.netloc != self.netloc:
                return False
        return True

    def get_page_src(self, link):
        suffix = ('.png', '.jpg',
                  '.js', '.css', '.ico', '.txt', '.rss')
        name = []
        url = urlparse(link)
        url = url._replace(
            scheme=self.scheme,
            netloc=self.netloc,
        )
        name.append(url.netloc.replace('.', '-'))
        name.append(url.path.replace('/', '-'))
        if url.path.endswith(suffix):
            return url.geturl(), ''.join(name)
        else:
            name.append('.html')
            return url.geturl(), ''.join(name)


def save(path, data, type):
    with open(path, type) as f:
        f.write(data)


def save_page_src(links, page, attr):
    """Download all local page's sources."""
    msg = f'Download page\'s "{attr}":'
    spinner = Spinner(msg)
    state = ''
    while state != 'FINISHED':
        for data in links:
            if page.ispagelink(data.get(attr)):
                src_url, src_name = page.get_page_src(data.get(attr))
                try:
                    src = requests.get(src_url)
                    src.raise_for_status()
                    save(os.path.join(
                        page.get_dir_path(), src_name), src.content, 'wb'
                    )
                    data[attr] = os.path.join(page.get_dir_name(), src_name)
                    spinner.next()
                except requests.RequestException as e:
                    spinner.finish()
                    logging.warning(
                        'Cannot get page\'s source: %s due to %s', src_url, e)
        spinner.finish()
        state = 'FINISHED'
