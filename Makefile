install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov= --cov-report xml

package-uninstall:
	python3 -m pip uninstall  dist/*.whl

.PHONY: 