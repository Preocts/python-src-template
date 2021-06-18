# python-template
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Preocts/python-template/main.svg)](https://results.pre-commit.ci/latest/github/Preocts/python-template/main)

### TODO:
- Auto detect module names and edit `setup.cfg` coverage lines
- Auto detect use of `requirements.txt` and insert into `setup.cfg`

This is a template example of how I structure an initial python project.

## What's included in (how to use) this template:

### SRC Layout

This template uses a package layout that forces the developer to have the package installed locally for testing. This is done by nesting the package modules within the `src` directory. The `src` directory is not, itself, a module and should not be referenced from imports. The benefit of this layout is that all tests are run against **installed** code which is closer to an actual deployment. Additionally, the developer will have the confidence that the `setup.cfg` is correctly including the desired modules as the tests will fail if they do not install correctly.

### setup.cfg

The configuration settings of `setup.py` have been moved into `setup.cfg`. In addtion, `setup.cfg` contains the settings for these additional items:
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

### pytest

pytest is used to run tests for this template. It supports the unittest framework as well. The only requirement is that all test files be located in the `./tests` directory.

### Coverage

Coverage is used to run pytest, measuring code coverage and exporting two reports on a successful run. `coverage.xml` and an html version located in `coverage_html_report`.

**Note:** As you add modules to the library you will need to edit the `setup.cfg` and add the module names (directory name) to the `[coverage:run]` list of `source_pkgs`.

```cfg
[coverage:run]
source_pkgs =
    module_name
```

### tox.ini

tox is the method of choice for running unit tests. The program simplifies the task of running tests against multiple versions of python. Running all tests should be as simple as running `tox` at the command line. Missing interpreter versions will be skipped without error.

**Note:** By default a coverage percentage of **90**% is required to pass. This can be adjusted as desired in the `tox.ini`.


---

# Module Name

Module Description

### Requirements
- Python >= 3.6

## Local developer installation

It is **highly** recommended to use a `venv` for installation. Leveraging a `venv` will ensure the installed dependency files will not impact other python projects or system level requirements.

The instruction below make use of a bash shell and a Makefile.  All commands should be able to be run individually of your shell does not support `make`

Clone this repo and enter root directory of repo:
```bash
$ git clone https://github.com/Preocts/[MODULE_NAME]
$ cd [MODULE_NAME]
```

Create and activate `venv`:
```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

Your command prompt should now have a `(venv)` prefix on it.

Install editable library and development requirements:
```bash
(venv) $ pip install -r requirements-dev.txt
(venv) $ pip install --editable .
```

Run tests
```bash
(venv) $ tox
```

To exit the `venv`:
```bash
(venv) $ deactivate
```

---

### Makefile

This repo has a Makefile with some quality of life scripts if your system supports `make`.

- `update` : Clean all artifacts, update pip, update requirements, install everything
- `clean-pyc` : Deletes python/mypy artifacts
- `clean-tests` : Deletes tox, coverage, and pytest artifacts
- `build-dist` : Build source distribution and wheel distribution
