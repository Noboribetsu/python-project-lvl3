import tempfile
import os

import pytest
import requests
from page_loader import download

links = [
    'https://ru.hexlet.io/courses',
    'https://ru.hexlet.io/assets/application.css',
    'https://ru.hexlet.io/assets/professions/nodejs.png',
    'https://ru.hexlet.io/packs/js/runtime.js',
]
dir_name = 'ru-hexlet-io-courses_files'
filenames = [
    'ru-hexlet-io-courses.html',
    'ru-hexlet-io-assets-professions-nodejs.png',
    'ru-hexlet-io-assets-professions-pic1.png',
    'ru-hexlet-io-assets-professions-pic2.jpg',
]


def get_file_path(name):
    return os.path.join('tests/fixtures', name)


def read(path):
    with open(path) as f:
        data = f.read()
    return data


def test_output_exception():
    with pytest.raises(OSError):
        download(links[0], 'path/to/dir')


def test_connection_exception():
    wrong_link = 'https://i.am.wrong.link/courses'
    with pytest.raises(IOError):
        with tempfile.TemporaryDirectory() as tmpdir:
            download(wrong_link, tmpdir)


def test_src_exception(requests_mock):
    data = read(get_file_path('test1.html'))
    requests_mock.get(links[0], text=data)
    requests_mock.get(links[1], text='Not found', status_code=404)
    requests_mock.get(links[2], text='pic1.png')
    requests_mock.get(
        links[3], exc=requests.exceptions.ConnectionError('Error')
    )
    with tempfile.TemporaryDirectory() as tmpdir:
        download(links[0], tmpdir)
        dir_path = os.path.join(tmpdir, dir_name)
        assert len(os.listdir(dir_path)) == 2


def test_page_loader(requests_mock):
    data = read(get_file_path('test1.html'))
    requests_mock.get(links[0], text=data)
    requests_mock.get(links[1], text='nodejs.png')
    requests_mock.get(links[2], text='pic1.png')
    requests_mock.get(links[3], text='pic2.jpg')
    with tempfile.TemporaryDirectory() as tmpdir:
        expected_path = os.path.join(tmpdir, filenames[0])
        dir_path = os.path.join(tmpdir, dir_name)
        actual_path = download(links[0], tmpdir)
        actual_data = read(actual_path)
        expected_data = read(get_file_path('result.html'))
        file1 = read(os.path.join(dir_path, filenames[1]))
        assert expected_path == actual_path
        assert os.path.exists(dir_path)
        assert actual_data == expected_data
        assert file1 == 'pic1.png'
        assert len(os.listdir(dir_path)) == 4
