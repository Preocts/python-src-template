.PHONY: init dev-install update clean-pyc clean-tests build-dist stats clean-build clean-all

init:
	pip install --upgrade pip setuptools wheel pip-tools

dev-install:  # install development requirements
	pip install -r requirements-dev.txt
	pip install --editable .
	pre-commit install
	pre-commit autoupdate

update: clean-pyc clean-tests init update-deps dev-install

update-deps: # update dependancies
	pip-compile --upgrade --output-file requirements-dev.txt requirements-dev.in

clean-pyc: ## Remove python/mypy artifacts
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.mypy_cache' -exec rm -rf {} +

clean-tests: ## Removes tox, coverage, and pytest artifacts
	rm -f coverage.xml
	rm -rf .tox
	rm -rf coverage_html_report
	rm -rf .coverage
	rm -f code_lines.txt
	find . -name '.pytest_cache' -exec rm -rf {} +

clean-build: ## Remove build artifacts
	rm -rf dist
	rm -rf build

clean-all: clean-pyc clean-tests clean-build

build-dist: ## Builds source distribution and wheel distribution files
	rm -rf ./dist
	python setup.py sdist bdist_wheel
