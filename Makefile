
clean:
	find . -name '__pycache__' -exec rm -fr {} +
	rm -rf ./.cache
	rm -f .coverage
	rm -rf .mypy_cache

test:
	pytest

COVFILE ?= .coverage
PWD = $(shell pwd)

coverage-application: 
	mypy instark/application
	pytest -x --cov=instark/application tests/application/ --cov-report term-missing -s

coverage-infrastructure: 
	mypy instark/infrastructure
	pytest -x --cov=instark/infrastructure tests/infrastructure/ \
	--cov-report term-missing -s

coverage: 
	mypy instark
	pytest -x --cov=instark tests/ --cov-report term-missing -s

update:
	pip-review --auto
	pip freeze > requirements.txt

serve:
	python -m instark serve
