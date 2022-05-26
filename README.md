# python-src-template

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Preocts/python-module-template/main.svg)](https://results.pre-commit.ci/latest/github/Preocts/python-module-template/main)
[![Python package](https://github.com/Preocts/python-module-template/actions/workflows/python-tests.yml/badge.svg?branch=main)](https://github.com/Preocts/python-module-template/actions/workflows/python-tests.yml)
[![codecov](https://codecov.io/gh/Preocts/python-module-template/branch/main/graph/badge.svg?token=sn79oOaqRI)](https://codecov.io/gh/Preocts/python-module-template)

[Project description here]

## Requirements

- [Python](https://python.org) >= 3.8

---

## A template for my library style boilerplate.

Straight forward to use!

### All module files go under `src/`

- Update requirements.in as needed
- Rename `module_name` as desired
- Update `py_modules = module_name` in `setup.cfg` with name
- Requires are placed in `setup.cfg`:

```cfg
[options]
install_requires =
    library_name
    other_library_name==2.3
```
- Run `make dev-install` or follow steps below to ensure local editible library is installed

### GitHub Actions

This module is loaded with a `python-tests.yml` which will execute some github actions running unit tests and coverage checks. This file and directory can be removed if undesired.

Within the `python-tests.yml` there is a commented step `Upload coverave to Codecov`.  If you have the repo associated with Covecov you can uncomment this step and the results of the coverage will be sent automagically.

---

# Local developer installation

It is **strongly** recommended to use a virtual environment
([`venv`](https://docs.python.org/3/library/venv.html)) when working with python
projects. Leveraging a `venv` will ensure the installed dependency files will
not impact other python projects or any system dependencies.

The following steps outline how to install this repo for local development. See
the [CONTRIBUTING.md](../CONTRIBUTING.md) file in the repo root for information
on contributing to the repo.

**Windows users**: Depending on your python install you will use `py` in place
of `python` to create the `venv`.

**Linux/Mac users**: Replace `python`, if needed, with the appropriate call to
the desired version while creating the `venv`. (e.g. `python3` or `python3.8`)

**All users**: Once inside an active `venv` all systems should allow the use of
`python` for command line instructions. This will ensure you are using the
`venv`'s python and not the system level python.

---

## Installation steps

Clone this repo and enter root directory of repo:

```bash
git clone https://github.com/{{ORG_NAME}}/{{REPO_NAME}}
cd {{REPO_NAME}}
```

Create the `venv`:

```bash
python -m venv venv
```

Activate the `venv`:

```bash
# Linux/Mac
. venv/bin/activate

# Windows
venv\Scripts\activate
```

The command prompt should now have a `(venv)` prefix on it. `python` will now
call the version of the interpreter used to create the `venv`

Install editable library and development requirements:

```bash
# Update pip and tools
python -m pip install --upgrade pip wheel setuptools

# Install development requirements
python -m pip install -r requirements-dev.txt

# Install editable version of library
python -m pip install --editable .
```

Install pre-commit [(see below for details)](#pre-commit):

```bash
pre-commit install
```

---

## Misc Steps

Run pre-commit on all files:

```bash
pre-commit run --all-files
```

Run tests:

```bash
tox [-r] [-e py3x]
```

To deactivate (exit) the `venv`:

```bash
deactivate
```

---

## [pre-commit](https://pre-commit.com)

> A framework for managing and maintaining multi-language pre-commit hooks.

This repo is setup with a `.pre-commit-config.yaml` with the expectation that
any code submitted for review already passes all selected pre-commit checks.
`pre-commit` is installed with the development requirements and runs seemlessly
with `git` hooks.

---

## Makefile

This repo has a Makefile with some quality of life scripts if the system
supports `make`.  Please note there are no checks for an active `venv` in the
Makefile.

| PHONY             | Description                                                        |
| ----------------- | ------------------------------------------------------------------ |
| `init`            | Update pip, setuptools, and wheel to newest version                |
| `install`         | install the project                                                |
| `install-dev`     | install development requirements and project                       |
| `build-dist`      | Build source distribution and wheel distribution                   |
| `clean-artifacts` | Deletes python/mypy artifacts including eggs, cache, and pyc files |
| `clean-tests`     | Deletes tox, coverage, and pytest artifacts                        |
| `clean-build`     | Deletes build artifacts                                            |
| `clean-all`       | Runs all clean scripts                                             |
