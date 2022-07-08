import tempfile
import os

from page_loader import download


links = [
    'https://ru.hexlet.io/courses',
    '/assets/professions/nodejs.png',
    '/assets/professions/pic1.png',
    'https://ru.hexlet.io/courses/assets/professions/pic2.jpg',
]
dir_name = 'ru-hexlet-io-courses_files'
filenames = [
    'ru-hexlet-io-courses.html',
    'ru-hexlet-io-courses-assets-professions-nodejs.png',
    'ru-hexlet-io-courses-assets-professions-pic1.png',
    'ru-hexlet-io-courses-assets-professions-pic2.jpg',
]


def get_file_path(name):
    return os.path.join('tests/fixtures', name)


def read(path):
    with open(path) as f:
        data = f.read()
    return data


def test_page_loader_path(requests_mock):
    data = read(get_file_path('test1.html'))
    requests_mock.get(links[0], text=data)
    with tempfile.TemporaryDirectory() as tmpdir:
        expected_path = os.path.join(tmpdir, filenames[0])
        expected_dir_path = os.path.join(tmpdir, dir_name)
        actual_path = download(links[0], tmpdir)
        assert expected_path == actual_path
        assert os.path.exists(expected_dir_path)


def test_page_loader_files(requests_mock):
    data = read(get_file_path('test1.html'))
    requests_mock.get(links[0], text=data)
    requests_mock.get(''.join((links[0], links[1])), text='nodejs.png')
    requests_mock.get(''.join((links[0], links[2])), text='pic1.png')
    requests_mock.get(''.join(links[3]), text='pic2.jpg')
    with tempfile.TemporaryDirectory() as tmpdir:
        dir_path = os.path.join(tmpdir, dir_name)
        actual_path = download(links[0], tmpdir)
        actual = read(actual_path)
        expected = read(get_file_path('test1.html'))
        file1 = read(os.path.join(dir_path, filenames[1]))
        assert actual != expected
        assert file1 == 'nodejs.png'
        assert len(os.listdir(dir_path)) == 3
