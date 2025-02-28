# Contributing

Before contributing, please either ask to claim an existing open issue or create
a new issue to discuss your proposed changes with the owner(s) of this repo
before making any changes.

Any pull requests without a clearly defined issue being solved will be closed.

### Bug reports

Found a bug but do not have time or do not wish to contribute a fix? Please
submit an issue for our awareness. Your feedback drives the continued
development of the project!

### Pull Request

All pull requests must:

- Pass all linting and formatting checks
- Have tests that cover all branches of the added feature
- If the PR is a bug fix there must be a test that duplicates the bug, proving
  it is fixed

### Code Style

Follow the patterns seen in the code. Walk where others have walked.

The majority of code style nits will be met when passing `pre-commit` checks
prior to submitting a pull request.

### Tests

  - Smaller tests are easier to work with
  - Mock at a minimum
  - No test should be dependent on another
  - No test should be dependent on secrets/tokens


---

# Local developer installation

The following steps outline how to install this repo for local development.

## Prerequisites

### Clone repo

```console
git clone https://github.com/[ORG NAME]/[REPO NAME]

cd [REPO NAME]
```

### Virtual Environment

Use a ([`venv`](https://docs.python.org/3/library/venv.html)), or equivalent,
when working with python projects. Leveraging a `venv` will ensure the installed
dependency files will not impact other python projects or any system
dependencies.

**Windows users**: Depending on your python install you will use `py` in place
of `python` to create the `venv`.

**Linux/Mac users**: Replace `python`, if needed, with the appropriate call to
the desired version while creating the `venv`. (e.g. `python3` or `python3.12`)

**All users**: Once inside an active `venv` all systems should allow the use of
`python` for command line instructions. This will ensure you are using the
`venv`'s python and not the system level python.

### Create the `venv`:

```console
python -m venv .venv
```

Activate the `venv`:

```console
# Linux/Mac
. .venv/bin/activate

# Windows
.venv\Scripts\activate
```

The command prompt should now have a `(venv)` prefix on it. `python` will now
call the version of the interpreter used to create the `venv`

To deactivate (exit) the `venv`:

```console
deactivate
```

---

## Developer Installation Steps

### Install editable library and development requirements

```console
python -m pip install --editable .[dev,test]
```

### Install pre-commit [(see below for details)](#pre-commit)

```console
pre-commit install
```

### Install with nox

If you have `nox` installed with `pipx` or in the current venv you can use the
following session. This is an alternative to the two steps above.

```console
nox -s install
```

---

## Pre-commit and nox tools

### Run pre-commit on all files

```console
pre-commit run --all-files
```

### Run tests with coverage (quick)

```console
nox -e coverage
```

### Run tests (slow)

```console
nox
```

### Build dist

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

### Update the generated files with changes

```console
nox -e update
```

### Upgrade all generated dependencies

```console
nox -e upgrade
```

---

## [pre-commit](https://pre-commit.com)

> A framework for managing and maintaining multi-language pre-commit hooks.

This repo is setup with a `.pre-commit-config.yaml` with the expectation that
any code submitted for review already passes all selected pre-commit checks.

---

## Error: File "setup.py" not found

Update `pip` to at least version 22.3.1
