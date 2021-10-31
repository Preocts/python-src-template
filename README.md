# python-template
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Preocts/python-template/main.svg)](https://results.pre-commit.ci/latest/github/Preocts/python-template/main)
[![Python package](https://github.com/Preocts/python-template/actions/workflows/python-tests.yml/badge.svg?branch=main)](https://github.com/Preocts/python-template/actions/workflows/python-tests.yml)
[![codecov](https://codecov.io/gh/Preocts/python-template/branch/main/graph/badge.svg?token=5GE4T7XU3L)](https://codecov.io/gh/Preocts/python-template)

### TODO:
- Auto detect use of `requirements.txt` and insert into `setup.cfg`
- Publish write-up on the /src layout
- CLI tool for starting new project without cloning/using template
- Version bump shell script

This is a template example of how I structure an initial python project.

## What's included in (how to use) this template:

## `./src` Layout

This template uses a package layout that forces the developer to have the package installed locally for testing. This is done by nesting the package modules within the `src` directory. The `src` directory is not, itself, a module and should not be referenced from imports. The benefit of this layout is that all tests are run against **installed** code which is closer to an actual deployment. Additionally, the developer will have the confidence that the `setup.cfg` is correctly including the desired modules as the tests will fail if they do not install correctly.

## `setup.cfg`

The configuration settings of `setup.py` have been moved into `setup.cfg`. In addition, `setup.cfg` contains the settings for these additional items:
- mypy
- coverage
- requirements.txt (see below)

When using this template, be sure the `setup.py` is edited to reflect the desired `[metadata]` values and supported python versions.

**requirements.txt**

The `requirements.txt` file list of required third-part libraries lives inside of the `setup.cfg`. This field is not reflected in this template as there are no external dependencies.  To add requirements, add this to the `setup.cfg` with a list of libraries and option version requirements:

```cfg
[options]
install_requires =
    library_name
    other_library_name==2.3
```

## pytest

pytest is used to run tests for this template. It supports the unittest framework as well. The only requirement is that all test files be located in the `./tests` directory.

## Coverage

Coverage is used to run pytest, measuring code coverage and exporting two reports on a successful run. `coverage.xml` and an html version located in `coverage_html_report`.  I use both in different places.  `.xml` is for CodeCov and the html goes to a local tool for review. Strip out what you don't need/want.

**Note:** As you add modules to the library you will need to edit the `setup.cfg` and add the module names (directory name) to the `[coverage:run]` list of `source_pkgs`.

```cfg
[coverage:run]
source_pkgs =
    module_name
```

## `tox.ini`

tox is the method of choice for running unit tests. The program simplifies the task of running tests against multiple versions of python. Running all tests should be as simple as running `tox` at the command line. Missing interpreter versions will be skipped without error. Be sure to install testing specific libraries in the default command list if you add any. `coverage` and `pytest` are installed by default of the template.

**Note:** By default a coverage percentage of **90**% is required to pass. This can be adjusted as desired in the `tox.ini`.


## `requirements-dev.txt`

The requirements-dev.in (and *.txt) includes the following for a dev environment:
- `pre-commit`: Linting, formatting, and error checks on local commit
- `black`: Formatter of choice, installed to allow editor to run on save
- `mypy`: Type checking and linting of code in editor
- `flake8`: Linting of code in PEP8 standard in editor
- `pytest`: Testing framework of choice
- `coverage`: Identify weak points of testing
- `tox`: Run tests in isolated environments mirroring clean installs

## pre-commit - [https://pre-commit.com/](https://pre-commit.com/)

Installed with dev requirements, pre-commit will run a series of checks against any file being committed to the local repo by `git`.  See `.pre-commit-config.yaml` for a list of checks used.

**Note:** `pre-commit install` will need to be run the first time the local repo is initialized.

## .github actions

**`pre-commit.yml`**: This registers a GitHub action that runs pre-commit against any pull request against `main` and any push to `main`

**`python-tests.yml`**: This registers a GitHub action that runs tests via tox on any pull request against `main` and any push to `main`. The tests are run on the lastest version of the following OS images:
- MacOS
- Windows
- Ubuntu

Versions, OS choices, and when to run the tests can be easily changed in this yml file.

**Additionally** CodeCov is included in the workflow here. This final step can be removed as desired.

---

# Below is a template README

---

# Module Name

Module Description

### Requirements
- Python >= 3.8

## Local developer installation

It is **highly** recommended to use a `venv` for installation. Leveraging a `venv` will ensure the installed dependency files will not impact other python projects.

Clone this repo and enter root directory of repo:
```bash
$ git clone https://github.com/[name]/[module_name]
$ cd [module_name]
```

Create and activate `venv`:
```bash
# Linux/MacOS
python3 -m venv venv
. venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate.bat
# or
py -m venv venv
venv\Scripts\activate.bat
```

Your command prompt should now have a `(venv)` prefix on it.

Install editable library and development requirements:
```bash
# Linux/MacOS
pip install -r requirements-dev.txt
pip install --editable .

# Windows
python -m pip install -r requirements-dev.txt
python -m pip install --editable .
# or
py -m pip install -r requirements-dev.txt
py -m pip install --editable .
```

Install pre-commit hooks to local repo:
```bash
pre-commit install
pre-commit autoupdate
```

Run tests
```bash
tox
```

To exit the `venv`:
```bash
deactivate
```

---

### Makefile

This repo has a Makefile with some quality of life scripts if your system supports `make`.

- `update` : Clean all artifacts, update pip, update requirements, install everything
- `build-dist` : Build source distribution and wheel distribution
- `clean-artifacts` : Deletes python/mypy artifacts including eggs, cache, and pyc files
- `clean-tests` : Deletes tox, coverage, and pytest artifacts
- `clean-build` : Deletes build artifacts
- `clean-all` : Runs all clean scripts
