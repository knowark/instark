
clean:
	find . -name '__pycache__' -exec rm -fr {} +

test:
	pytest

coverage-application: 
	pytest -x --cov=instark/application tests/application/ \
	--cov-report term-missing -s

coverage-infrastructure: 
	pytest -x --cov=instark/infrastructure tests/infrastructure/ \
	--cov-report term-missing -s

coverage: 
	pytest -x --cov=instark tests/ --cov-report term-missing -s
