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

Be sure to run the expected formatters and linters prior to opening the PR.

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

### [Install nox](https://nox.thea.codes/en/stable/index.html)

It is recommended to use a tool such as `pipx` or `uvx` to install nox. nox is
needed to run the provided sessions for developer setup, linting, tests, and
dependency management. It is optional, but these instructions will not cover
manually steps outside of nox.


## Nox Sessions

### Developer Install

This builds the `/.venv`, installs the editable
package, and installs all dependency files.

```bash
nox -s dev
```

### Run tests with coverage

```console
nox -s test
```

### Run formatters and linters

```console
nox -s lint
```

### Build dist

```console
nox -s build
```

---

## Updating dependencies

New dependencys can be added to the `requirements-*.txt` file. It is recommended
to only use pins when specific versions or upgrades beyond a certain version are
to be avoided. Otherwise, allow `pip-compile` to manage the pins in the
generated `constraints.txt` file.

Once updated following the steps below, the package can be installed if needed.

### Update the generated files with changes

```console
nox -s update-deps
```

### Upgrade all generated dependencies

```console
nox -s upgrade-deps
```

---

## [pre-commit](https://pre-commit.com)

> A framework for managing and maintaining multi-language pre-commit hooks.

This repo is setup with a `.pre-commit-config.yaml` with the expectation that
any code submitted for review already passes all selected pre-commit checks.
