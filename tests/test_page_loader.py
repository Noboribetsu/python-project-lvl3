import subprocess
import tempfile
import os


link = 'https://ru.hexlet.io/courses'
filename = 'ru-hexlet-io-courses.html'


def get_fixtures_path(name):
    return os.path.join('tests/fixtures', name)


def test_page_loader(requests_mock):
    requests_mock.get(link, text='data')
    with tempfile.TemporaryDirectory() as tmpdir:
        expected_path = os.path.join(tmpdir, filename)
        path = subprocess.run(
            ['page-loader', '--output', tmpdir, link],
            stdout=subprocess.PIPE, encoding='utf-8')
        with open(expected_path) as f:
            actual = f.read()
        assert path == expected_path
        assert actual == 'data'
