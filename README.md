# python-template

This is a template example of how I structure an initial python project.

### Why three `requirement` files?

Personal preference. I find it easier when setting up CI pipelines to have a `requirements-test.txt` with all required libraries for testing without needing to install the linters.

Requirement file break-down:
- `requirements.in` : Any required third-part libraries for the project to run
- `requirements-dev.in` : Any development requirements which include linters and formatters
- `requirements-test.in` : Any libraries required specifically for unit testing

*Below this line is my standard README.md*

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
make install-test
pre-commit install
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
