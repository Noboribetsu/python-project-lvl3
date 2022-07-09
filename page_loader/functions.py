import os
from urllib.parse import urlparse


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
        name.append(url.path.replace('/', '-'))
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
        if link:
            url = urlparse(link)
            if url.netloc:
                if url.netloc != self.netloc:
                    return False
            return True
        return False

    def get_page_src(self, link):
        name = []
        url = urlparse(link)
        url = url._replace(
            scheme=self.scheme,
            netloc=self.netloc,
        )
        name.append(url.netloc.replace('.', '-'))
        name.append(url.path.replace('/', '-'))
        return url.geturl(), ''.join(name)


def save(path, data):
    with open(path, 'w') as f:
        f.write(data)
