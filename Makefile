.PHONY: init
init:
	python -m pip install --upgrade pip setuptools

.PHONY: install
install:
	python -m pip install --upgrade .

.PHONY: install-dev
install-dev:
	python -m pip install --editable .[dev,test]
	pre-commit install

.PHONY: install-test
install-test:
	python -m pip install .[test]

# Optional: use requirements.in to manage requirements
# Use optional dynamic field in pyproject.toml
# .PHONY: upgrade-dev
# upgrade-dev:
# 	python -m pip install pip-tools
# 	pip-compile --upgrade
# 	python -m pip install --upgrade --editable .[dev,test]

.PHONY: build-dist
build-dist:
	python -m pip install --upgrade build
	python -m build

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
