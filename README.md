[![Python 3.8 | 3.9 | 3.10 | 3.11 | 3.12](https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/downloads)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Preocts/python-src-template/main.svg)](https://results.pre-commit.ci/latest/github/Preocts/python-src-template/main)
[![Python tests](https://github.com/Preocts/python-src-template/actions/workflows/python-tests.yml/badge.svg?branch=main)](https://github.com/Preocts/python-src-template/actions/workflows/python-tests.yml)

# python-src-template

A template I use for most projects and is setup to jive with my environment at
the company I work with.

This is not the one-shot solution to project structure or packaging. This is
just what works well for one egg on the Internet. Feel free to use it as you see
fit.

## FAQ

- **Q:** Should I follow everything to the absolute letter in this template?
  - **A:** Heck no, I don't even do that! This is just the closest
    one-size-fits-most template I've put together. Use what you want how you
    want.

- **Q:** Why do you hard pin your development and test requirements?
  - **A:** For control over the environment used to develop on the package. It
    is also beneficial in many of the areas I work where artifactory proxies are
    between `pip` and the pypi public index. Versions remaining hard pinned
    ensure the package is always cleared for use through the artifactory.

- **Q:** Why not put the requirements into the `pyproject.toml`?
  - **A:** Mostly because `pip-compile` does all the work for me and doesn't
    target the `pyproject.toml`. Partly because many of my projects need to be
    scanned by utilities that still think `requirements.txt` is the only pattern
    to use.

- **Q:** Why does this template change so often?
  - **A:** I'm constantly finding new tweaks that make the template fit just a
    little better. I'm also open to ideas and suggestions so please drop an
    issue if you have one.

---

# Local developer installation

The following steps outline how to install this repo for local development. See
the [CONTRIBUTING.md](CONTRIBUTING.md) file in the repo root for information on
contributing to the repo.

## Prerequisites

### It is recommended to use a virtual environment

Use a ([`venv`](https://docs.python.org/3/library/venv.html)), or equivalent,
when working with python projects. Leveraging a `venv` will ensure the installed
dependency files will not impact other python projects or any system
dependencies.

**Windows users**: Depending on your python install you will use `py` in place
of `python` to create the `venv`.

**Linux/Mac users**: Replace `python`, if needed, with the appropriate call to
the desired version while creating the `venv`. (e.g. `python3` or `python3.8`)

**All users**: Once inside an active `venv` all systems should allow the use of
`python` for command line instructions. This will ensure you are using the
`venv`'s python and not the system level python.

### Create the `venv`:

```console
python -m venv venv
```

Activate the `venv`:

```console
# Linux/Mac
. venv/bin/activate

# Windows
venv\Scripts\activate
```

The command prompt should now have a `(venv)` prefix on it. `python` will now
call the version of the interpreter used to create the `venv`

To deactivate (exit) the `venv`:

```console
deactivate
```


---

## Developer Installation Steps

Clone this repo and enter root directory of repo:

```console
git clone https://github.com/[ORG NAME]/[REPO NAME]
cd [REPO NAME]
```

Install editable library and development requirements:

```console
python -m pip install --editable .[dev,test]
```

Install pre-commit [(see below for details)](#pre-commit):

```console
pre-commit install
```

---

## Pre-commit and nox tools

Run pre-commit on all files:

```console
pre-commit run --all-files
```

Run tests with coverage (quick):

```console
nox -e coverage
```

Run tests (slow):

```console
nox
```

Build dist:

```console
nox -e build
```

---

## Updating dependencies

New dependencys can be added to the `requirements-*.in` file. It is recommended
to only use pins when specific versions or upgrades beyond a certain version are
to be avoided. Otherwise, allow `pip-compile` to manage the pins in the
generated `requirements-*.txt` files.

Once updated following the steps below, the package can be installed if needed.

To update the generated files with a dependency:

```console
nox -e update
```

To attempt to upgrade all generated dependencies:

```console
nox -e upgrade
```

---

## [pre-commit](https://pre-commit.com)

> A framework for managing and maintaining multi-language pre-commit hooks.

This repo is setup with a `.pre-commit-config.yaml` with the expectation that
any code submitted for review already passes all selected pre-commit checks.

---

## Error: File "setup.py" not found.

Update `pip` to at least version 22.3.1
