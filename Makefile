.PHONY: init install lock install-dev clean-pyc clean-install clean update

init:
	pip install --upgrade pip setuptools wheel
	pip install pip-tools

install: init # install run-time requirements
	pip install -r requirements.txt
	pip install -e .

lock:  # generate new hashes for requirement files
	pip-compile --generate-hashes
	pip-compile --generate-hashes --output-file requirements-dev.txt requirements-dev.in

update: # update dependancies
	pip-compile --upgrade --generate-hashes
	pip-compile --upgrade --generate-hashes --output-file requirements-dev.txt requirements-dev.in
	pip install --upgrade -r requirements.txt -r requirements-dev.txt


install-dev:  # Install development requirements
	pip install -r requirements-dev.txt

clean-pyc: ## Remove python artifacts.
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	find . -name '__pycache__' -exec rm -rf {} +

clean-install: ## Remove install artifacts.
	pip uninstall gitclient-preocts
	rm -rf ./src/*.egg-info

clean: clean-pyc clean-install
