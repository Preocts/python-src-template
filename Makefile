.PHONY: init install update update-deps clean-pyc

init:
	pip install --upgrade pip setuptools wheel pip-tools
	rm -rf .tox

install:  # install run-time requirements
	pip install --upgrade -r requirements.txt -r requirements-dev.txt
	pip install --editable .

update: init update-deps install

update-deps: # update dependancies
	pip-compile --upgrade --output-file requirements.txt requirements.in
	pip-compile --upgrade --output-file requirements-dev.txt requirements-dev.in

clean-pyc: ## Remove python artifacts.
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.mypy_cache' -exec rm -rf {} +
	find . -name '.pytest_cache' -exec rm -rf {} +
