install:
	poetry install

selfcheck:
	poetry check

check: selfcheck lint test test-coverage

build: check
	poetry build

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff
publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

gendiff:
	poetry run gendiff

lint:
	poetry run isort .
	poetry run black . --line-length 80
	poetry run flake8 gendiff

.PHONY: install test lint selfcheck check build
