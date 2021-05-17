.PHONY: init install lock update clean tests

init:
	pip install --upgrade pip setuptools wheel
	pip install pip-tools

install: init # install run-time requirements
	pip install -r requirements.txt

lock:  # generate new hashes for requirement files
	pip-compile --generate-hashes --output-file requirements.txt requirements.in
	pip-compile --generate-hashes --output-file requirements-dev.txt requirements-dev.in
	pip-compile --generate-hashes --output-file requirements-test.txt requirements-test.in

update: # update dependancies
	pip-compile --upgrade --generate-hashes --output-file requirements.txt requirements.in
	pip-compile --upgrade --generate-hashes --output-file requirements-dev.txt requirements-dev.in
	pip-compile --upgrade --generate-hashes --output-file requirements-test.txt requirements-test.in
	pip install --upgrade -r requirements.txt -r requirements-dev.txt -r requirements-test.txt

install-dev:  # Install development requirements
	pip install -r requirements-dev.txt -r requirements-test.txt
	pre-commit install

tests: # Run pytests and coverage report
	coverage erase
	coverage run -m pytest -v ./tests
	coverage report
	coverage xml
	coverage html

clean-pyc: ## Remove python artifacts.
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.mypy_cache' -exec rm -rf {} +

clean-tests: ## Remove pytest and coverage artifacts
	find . -name '.pytest_cache' -exec rm -rf {} +
	find . -name '.coverage' -exec rm -f {} +
	find . -name 'coverage.xml' -exec rm -f {} +
	find . -name 'coverage_html_report' -exec rm -rf {} +

clean-install: ## Remove build artifacts.
	find . -name '*.egg-info' -exec rm -rf {} +

clean: clean-pyc clean-install clean-tests
