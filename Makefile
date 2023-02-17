.PHONY: init
init:
	python -m pip install --upgrade -r requirements/requirements-base.txt

.PHONY: install
install:
	python -m pip install --upgrade .

.PHONY: install-dev
install-dev:
	python -m pip install --upgrade --editable .
	python -m pip install --upgrade -r requirements/requirements-dev.txt
	python -m pip install --upgrade -r requirements/requirements-test.txt
	pre-commit install

.PHONY: upgrade-dev
upgrade-dev:
	pip-compile --resolver=backtracking requirements/requirements-base.in
	pip-compile --resolver=backtracking requirements/requirements.in
	pip-compile --resolver=backtracking requirements/requirements-dev.in
	pip-compile --resolver=backtracking requirements/requirements-test.in

.PHONY: coverage
coverage:
	coverage run -m pytest tests/
	coverage report -m
	coverage html
	@# This should work for most linux and windows users
	@# python -c "import os;import webbrowser; webbrowser.open(f'{os.getcwd()}/htmlcov/index.html')"

	@# WSL users can use this (change Ubuntu-20.04 to your distro name)
	python -c "import os;import webbrowser; webbrowser.open(f'file://wsl.localhost/Ubuntu-20.04{os.getcwd()}/htmlcov/index.html')"

.PHONY: docker-test
docker-test:
	docker build -t docker-test .
	docker run --rm docker-test

.PHONY: docker-clean
docker-clean:
	docker system prune -f

.PHONY: build-dist
build-dist:
	python -m pip install --upgrade build
	python -m build

.PHONY: clean
clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.mypy_cache' -exec rm -rf {} +
	rm -rf .tox
	rm -f coverage.xml
	rm -f coverage.json
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf .coverage.*
	find . -name '.pytest_cache' -exec rm -rf {} +
	rm -rf dist
	rm -rf build
