build:
	poetry build

install:
	poetry install

package-install:
	python3 -m pip install --user ./dist/*.whl.

run:
	poetry run gendiff $(args)

lint:
	poetry run flake8 gendiff
