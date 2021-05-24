# python-template
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Preocts/python-template/main.svg)](https://results.pre-commit.ci/latest/github/Preocts/python-template/main)


This is a template example of how I structure an initial python project.

---

# Module Name

Module Description

### Requirements
- Python 3.8

### Installation

It is **highly** recommended to use a `venv` for installation. Leveraging a `venv` will ensure the installed dependency files will not impact other python projects.

The instruction below make use of a bash shell and a Makefile.  All commands should be able to be run individually of your shell does not support `make`

Clone this repo and enter root directory of repo:
```bash
git clone https://github.com/Preocts/[MODULENAME]
cd [MODULENAME]
```

Create and activate `venv`:
```bash
python3.8 -m venv venv
source ./venv/bin/activate
```

Your command prompt should now have a `(venv)` prefix on it.

Install the scripts:
```bash
make install
```

Install the scripts for development/tests:
```bash
make install-dev
```

To lock present requirement file versions:
```bash
make lock
```

To update versions of requirement libraries:
```bash
make update
```

To exit the `venv`:
```bash
deactivate
```
