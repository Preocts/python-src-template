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

### [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

uv is required to use the provided noxfile sessions for developer setup,
linting, and tests. Using nox is completely optional, all sessions can be
manually recreated. These instructions will not cover those cases.

## Nox Sessions

### Developer Install

This builds the `/.venv`, installs the editable package, and installs
pre-commit.

```console
uvx nox -s dev
```

### Validate uv.lock

```console
uvx nox -s lock
```

### Run tests and display coverage

```console
uvx nox -s test
```

Passing extra arguements to pytest:

```console
uvx nox -s test -- -vvv -x --full-trace
```

### Run linters

```console
uvx nox -s lint
```

### Run formatters

```console
uvx nox -s format
```

### Run all checks

```console
uvx nox
```

### Build dist

```console
uvx nox -s build
```

---

## Updating dependencies

New dependencies should be added with the uv cli command `uv add
[package-name]`. This will ensure the `uv.lock` file is updated as well.

### Upgrade an existing package to latest

```console
uvx nox -s upgrade-package -- package-name
```

### Upgrade all packages to latest

```console
uvx nox -s upgrade
```
