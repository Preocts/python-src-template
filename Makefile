.PHONY: init
init:
	pip install --upgrade pip setuptools wheel pip-tools

.PHONY: dev-install
dev-install:
	pip install -r requirements-dev.txt
	pip install --editable .
	pre-commit install
	pre-commit autoupdate

.PHONY: update
update: clean-artifacts clean-tests init dev-install

.PHONY: clean-artifacts
clean-artifacts:
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.mypy_cache' -exec rm -rf {} +

.PHONY: clean-tests
clean-tests:
	rm -f coverage.xml
	rm -rf .tox
	rm -rf coverage_html_report
	rm -rf .coverage
	rm -f code_lines.txt
	find . -name '.pytest_cache' -exec rm -rf {} +

.PHONY: clean-build
clean-build:
	rm -rf dist
	rm -rf build

.PHONY: clean-all
clean-all: clean-artifacts clean-tests clean-build

.PHONY: build-dist
build-dist:
	rm -rf ./dist
	python setup.py sdist bdist_wheel
