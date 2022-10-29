.PHONY: init
init:
	python -m pip install --upgrade pip

.PHONY: install
install:
	python -m pip install --upgrade .

.PHONY: install-dev
install-dev:
	python -m pip install --editable .[dev,test]
	pre-commit install

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
