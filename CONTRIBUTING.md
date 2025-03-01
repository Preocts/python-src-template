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

# Developer installation

## Prerequisites

- [**uv**](https://docs.astral.sh/uv) >= 0.6.3

[Installation options can be found here.](https://docs.astral.sh/uv/getting-started/installation/)

Or just use [pipx](https://pypi.org/project/pipx/)

```bash
pipx install uv
```


### Clone repo

```bash
git clone https://github.com/[ORG NAME]/[REPO NAME]
```

---

## Developer Installation Commands

### 1. Install editable library and development requirements

```bash
uv sync
```

### 2. Install pre-commit [(see below for details)](#pre-commit)

```bash
pre-commit install
```

---

## Nox sessions

This repo uses [nox](https://nox.thea.codes/en/stable/index.html) to simplify
workflow actions.

### Run tests and report coverage (quick):

```bash
nox --session coverage
```

### Run tests against all supported versions (slow):

```bash
nox
```

### Run pre-commit on all files

```bash
nox --session pre_commit
```

### Build dist

```bash
nox --session build
```

---

## [pre-commit](https://pre-commit.com)

> A framework for managing and maintaining multi-language pre-commit hooks.

This repo is setup with a `.pre-commit-config.yaml` with the expectation that
any code submitted for review already passes all selected pre-commit checks.
