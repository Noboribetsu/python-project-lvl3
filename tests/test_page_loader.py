import tempfile
import os

from page_loader import download


link = 'https://ru.hexlet.io/courses'
filename = 'ru-hexlet-io-courses.html'


def test_page_loader(requests_mock):
    requests_mock.get(link, text='data')
    with tempfile.TemporaryDirectory() as tmpdir:
        expected_path = os.path.join(tmpdir, filename)
        path = download(link, tmpdir)
        assert expected_path == path
        with open(path) as f:
            actual = f.read()
        assert actual == 'data'
