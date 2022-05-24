.PHONY: init
init:
	pip install --upgrade pip setuptools wheel pip-tools

.PHONY: install
install:
	pip install .

.PHONY: install-dev
install-dev:
	pip install -r requirements-dev.txt
	pip install --editable .
	pre-commit install

.PHONY: build-dist
build-dist:
	rm -rf ./dist
	python setup.py sdist bdist_wheel

.PHONY: clean-artifacts
clean-artifacts:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.mypy_cache' -exec rm -rf {} +

.PHONY: clean-tests
clean-tests:
	rm -f coverage.xml
	rm -rf .tox
	rm -rf coverage_html_report
	rm -rf .coverage
	find . -name '.pytest_cache' -exec rm -rf {} +

.PHONY: clean-build
clean-build:
	rm -rf dist
	rm -rf build

.PHONY: clean-all
clean-all: clean-artifacts clean-tests clean-build
