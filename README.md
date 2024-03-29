## Description:
page-loader – утилита командной строки, которая скачивает страницы из интернета и сохраняет их на компьютере. Вместе со страницей она скачивает все ресурсы (картинки, стили и js) давая возможность открывать страницу без интернета.

### Requrements:
* Python 3.8+
* Poetry
* GNU Make

### Usage:
```bash
page-loader -h
usage: page-loader [-h] [-o PATH] LINK

Download a page by a web-site link and save it to a mentioned directory.

positional arguments:
  LINK                  a link on a page that should be loaded

options:
  -h, --help            show this help message and exit
  -o PATH, --output PATH
                        a directory path to save a page(should be exist) (default: CWD)
```

### Install:
```bash
make install
make build
make package-install
```

### Check codestyle
```bash
make lint
```

### Run tests
```bash
make test
make test-coverage
```



### Hexlet tests and linter status:
[![Actions Status](https://github.com/Noboribetsu/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/Noboribetsu/python-project-lvl3/actions)

### Codeclimate:
[![Maintainability](https://api.codeclimate.com/v1/badges/fa7875262d906b122ea8/maintainability)](https://codeclimate.com/github/Noboribetsu/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/fa7875262d906b122ea8/test_coverage)](https://codeclimate.com/github/Noboribetsu/python-project-lvl3/test_coverage)

### GitHub actions:
[![build&test](https://github.com/Noboribetsu/python-project-lvl3/actions/workflows/build&test.yml/badge.svg)](https://github.com/Noboribetsu/python-project-lvl3/actions/workflows/build&test.yml)

### Step 1(page-loader):
[![asciicast](https://asciinema.org/a/oSTkLoOrnafURZSjNfDZRih60.svg)](https://asciinema.org/a/oSTkLoOrnafURZSjNfDZRih60)

### Step 2(page's files download: img):
[![asciicast](https://asciinema.org/a/Jc4NHeld7egGfIwOC24jpZkws.svg)](https://asciinema.org/a/Jc4NHeld7egGfIwOC24jpZkws)

### Step 3(+ links, scripts):
[![asciicast](https://asciinema.org/a/UMof37S2wnGPakYKGksXlPJUp.svg)](https://asciinema.org/a/UMof37S2wnGPakYKGksXlPJUp)

### Step 4(add logging):
[![asciicast](https://asciinema.org/a/xcqfUq0VbUT9uCcjf5YtLf8yz.svg)](https://asciinema.org/a/xcqfUq0VbUT9uCcjf5YtLf8yz)

### Step 5(add exceptions):
[![asciicast](https://asciinema.org/a/oAG8HnfbTtWLSLCrpZZqI26uQ.svg)](https://asciinema.org/a/oAG8HnfbTtWLSLCrpZZqI26uQ)

### Step 6(add progression spinner):
[![asciicast](https://asciinema.org/a/O8GPefWQnSwcdkKJSUS1MmkSp.svg)](https://asciinema.org/a/O8GPefWQnSwcdkKJSUS1MmkSp)
