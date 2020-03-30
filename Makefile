clean:
	find . -name '__pycache__' -exec rm -fr {} +
	rm -rf ./.cache .mypy_cache ./schema/.mypy_cache .coverage

test:
	pytest

PROJECT = instark

COVFILE ?= .coverage

coverage-application: 
	export COVERAGE_FILE=$(COVFILE); pytest --cov=$(PROJECT)/application \
	tests/application/ --cov-report term-missing -x -s -W \
	ignore::DeprecationWarning -o cache_dir=/tmp/questionark/cache

coverage-infrastructure: 
	export COVERAGE_FILE=$(COVFILE); pytest --cov=$(PROJECT)/infrastructure \
	tests/infrastructure/ --cov-report term-missing -x -s -W \
	ignore::DeprecationWarning -o cache_dir=/tmp/questionark/cache

coverage: 
	export COVERAGE_FILE=$(COVFILE); pytest --cov=$(PROJECT) tests/ \
	--cov-report term-missing -x -s -vv -W ignore::DeprecationWarning \
	-o cache_dir=/tmp/questionark/cache

serve:
	python -m $(PROJECT) serve

serve-dev:
	export QUESTIONARK_MODE=DEV; python -m $(PROJECT) serve

PART ?= patch

version:
	bump2version $(PART) $(PROJECT)/__init__.py --tag --commit

dev-deploy:
	 bin/dev_deploy.sh




#
#clean:
#	find . -name '__pycache__' -exec rm -fr {} +
#	rm -rf ./.cache
#	rm -f .coverage
#	rm -rf .mypy_cache
#
#test:
#	pytest
#
#COVFILE ?= .coverage
#PROJECT = instark
#
#coverage-application:
#	# mypy $(PROJECT)/application
#	export COVERAGE_FILE=$(COVFILE); pytest -x \
#	--cov=$(PROJECT)/application tests/application/ \
#	--cov-report term-missing \
#	--cov-report xml:$(COVFILE).xml -s -vv \
#	-o cache_dir=/tmp/pytest/cache
#
#coverage-infrastructure:
#	mypy $(PROJECT)/infrastructure
#	export COVERAGE_FILE=$(COVFILE); pytest -x \
#	--cov=$(PROJECT)/infrastructure tests/infrastructure/ \
#	--cov-report term-missing \
#	--cov-report xml:$(COVFILE).xml -s -vv \
#	-o cache_dir=/tmp/pytest/cache
#
#coverage: 
#	mypy $(PROJECT)
#	export COVERAGE_FILE=$(COVFILE); pytest -x \
#	--cov=$(PROJECT) tests/ \
#	--cov-report term-missing \
#	--cov-report xml: $(COVFILE).xml -s -vv \
#	-o cache_dir=/tmp/pytest/cache
#
#update:
#	pip-review --auto
#	pip freeze > requirements.txt
#
#serve:
#	python -m $(PROJECT) serve
