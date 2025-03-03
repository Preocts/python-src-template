[![Python 3.9 | 3.10 | 3.11 | 3.12 | 3.13](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](https://www.python.org/downloads)
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

## Prerequisites

- [**uv**](https://docs.astral.sh/uv) >= 0.6.3

## FAQ

- **Q:** Why uv over venv and setup-tools?
  - **A:** Primarily because of the lower barrier of entry that the uv workflow
    offers to the next-dev and the non-dev. Speed is nice, but where Astral has
    really pushed value with uv is in the simplicity.

- **Q:** Should I follow everything to the absolute letter in this template?
  - **A:** Heck no, I don't even do that! This is just the closest
    one-size-fits-most template I've put together. Use what you want how you
    want.

- **Q:** Why does this template change so often?
  - **A:** I'm constantly finding new tweaks that make the template fit just a
    little better. I'm also open to ideas and suggestions so please drop an
    issue if you have one.
