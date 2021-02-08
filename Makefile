SRCDIR="./src/budget_helper"
TESTDIR="./tests"

.PHONY: update-deps init update install clean clean-pyc clean-build clean-test tests install-dev

update-deps:
	pip-compile --upgrade --generate-hashes
	pip-compile --upgrade --generate-hashes --output-file requirements-dev.txt requirements-dev.in

install:
	pip install --upgrade pip setuptools wheel
	pip install --upgrade -r requirements.txt
	pip install --editable .

install-dev:
	pip install --upgrade -r requirements-dev.txt
	pre-commit install

init:
	pip install pip-tools
	rm -rf .tox

update: init update-deps install

# Run all cleaning steps
clean: clean-build clean-pyc clean-test

clean-pyc: ## Remove python artifacts.
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-build: ## Remove build artifacts.
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-test: ## Remove test artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	find . -name '.pytest_cache' -exec rm -fr {} +

tests: ## Run all tests found in the /tests directory.
	python -m pytest -v $(TESTDIR)
