# python-src-template

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Preocts/python-module-template/main.svg)](https://results.pre-commit.ci/latest/github/Preocts/python-module-template/main)
[![Python package](https://github.com/Preocts/python-module-template/actions/workflows/python-tests.yml/badge.svg?branch=main)](https://github.com/Preocts/python-module-template/actions/workflows/python-tests.yml)

[Project description here]

## Requirements

- [Python](https://python.org) >= 3.7

---

## A template for my library style boilerplate.

Straight forward to use!

**Kind of...**

While this is the way **I** usually start my Python project setup, this is not
the only way to do things. This template leverages the `pyproject.toml` as
completely as `setuptool` currently supports. I choose to enforce clean commits
with `pre-commit` and have it baked into the `Makefile` install.  The settings
for `mypy` are as strict as I can make them.  The default `tox` setup attempts
tests on all stable versions of Python, runs `mypy` in full strictness, and
enforces `pre-commit` success.  The GitHub actions are setup to run tox across
Windows, Linux, and MacOS.  This is all just the setup I'm comfortable and
familiar with.  I entreat you to take what you need and make something of your
own.  Every artist is different as is every choice of canvas.

**Why `src/` structure**?

The benefit I get from this project structure comes from testing. The `src/`
structure forces us to test on the installed version of the modules within
`site-packages/` and not our local code. Even though these files are symlinked
in most cases with the dev install, the calls and import references are the
same. This ensures we are testing on what will be setup in the not-my machine.

---

### All module files go under `src/`

- Rename `src/module_name` as desired
- Update the `pyproject.toml`
  - Fill in `[project]` metadata
  - Add dependencies to `dependencies`
  - Add optional dependencies to `[project.optional-dependencies]` as needed
  - Fill in `[project.urls]` if desired (used by sites like pypi)
  - Add/remove `[project.scripts]` as needed
  - Add/remove `[tool.setuptools.package-data]` as needed
  - In `[tool.coverage.run]` update `source_pkgs` to the module name(s) from
    above
  - In `[tool.tox]` update `mypy -p module_name` to reflect name of module(s)
  - Run `make install-dev` or follow steps below to ensure local editible
    library is installed

### GitHub Actions

This module is loaded with a `python-tests.yml` which will execute some github
actions running unit tests and coverage checks. This file and directory can be
removed if undesired.

---

# Local developer installation

It is **strongly** recommended to use a virtual environment
([`venv`](https://docs.python.org/3/library/venv.html)) when working with python
projects. Leveraging a `venv` will ensure the installed dependency files will
not impact other python projects or any system dependencies.

The following steps outline how to install this repo for local development. See
the [CONTRIBUTING.md](CONTRIBUTING.md) file in the repo root for information on
contributing to the repo.

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

```console
$ git clone https://github.com/{{ORG_NAME}}/{{REPO_NAME}}
$ cd {{REPO_NAME}}
```

Create the `venv`:

```console
$ python -m venv venv
```

Activate the `venv`:

```console
# Linux/Mac
$ . venv/bin/activate

# Windows
$ venv\Scripts\activate
```

The command prompt should now have a `(venv)` prefix on it. `python` will now
call the version of the interpreter used to create the `venv`

Install editable library and development requirements:

```console
# Update pip and tools
$ python -m pip install --upgrade pip

# Install editable version of library
$ python -m pip install --editable .[dev]
```

Install pre-commit [(see below for details)](#pre-commit):

```console
$ pre-commit install
```

---

## Misc Steps

Run pre-commit on all files:

```console
$ pre-commit run --all-files
```

Run tests:

```console
$ tox [-r] [-e py3x]
```

Build dist:

```console
$ python -m pip install --upgrade build

$ python -m build
```

To deactivate (exit) the `venv`:

```console
$ deactivate
```
---

## Note on flake8:

`flake8` is included in the `requirements-dev.txt` of the project. However it
disagrees with `black`, the formatter of choice, on max-line-length and two
general linting errors. `.pre-commit-config.yaml` is already configured to
ignore these. `flake8` doesn't support `pyproject.toml` so be sure to add the
following to the editor of choice as needed.

```ini
--ignore=W503,E203
--max-line-length=88
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

| PHONY             | Description                                                                |
| ----------------- | -------------------------------------------------------------------------- |
| `init`            | Update pip to newest version                                               |
| `install`         | install the project                                                        |
| `install-test`    | install test requirements and project as editable install                  |
| `install-dev`     | install development/test requirements and project as editable install      |
| `upgrade-dev`     | update all dependencies, regenerate requirements.txt (disabled by default) |
| `coverage`        | Runs `tox -p`. results to stdout, json, and html                           |
| `build-dist`      | Build source distribution and wheel distribution                           |
| `clean-artifacts` | Deletes python/mypy artifacts, cache, and pyc files                        |
| `clean-tests`     | Deletes tox, coverage, and pytest artifacts                                |
| `clean-build`     | Deletes build artifacts                                                    |
| `clean`           | Deletes build, tox, coverage, pytest, mypy, cache, and pyc artifacts       |
