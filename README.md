[![Python 3.10 | 3.11 | 3.12 | 3.13 | 3.14](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)](https://www.python.org/downloads)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Nox](https://img.shields.io/badge/%F0%9F%A6%8A-Nox-D85E00.svg)](https://github.com/wntrblm/nox)

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Preocts/python-src-template/main.svg)](https://results.pre-commit.ci/latest/github/Preocts/python-src-template/main)
[![Python tests](https://github.com/Preocts/python-src-template/actions/workflows/python-tests.yml/badge.svg?branch=main)](https://github.com/Preocts/python-src-template/actions/workflows/python-tests.yml)

# python-src-template

- [Contributing Guide and Developer Setup Guide](./CONTRIBUTING.md)
- [License: MIT](./LICENSE)

---

A template I use for most projects.

This is not the one-shot solution to project structure or packaging. This is
just what works well for one egg on the Internet. Feel free to use it as you see
fit.

## FAQ

- **Q:** Should I follow everything to the absolute letter in this template?
  - **A:** Heck no, I don't even do that! This is just the closest
    one-size-fits-most template I've put together. Use what you want how you
    want.

- **Q:** Why does this template change so often?
  - **A:** I'm constantly finding new tweaks that make the template fit just a
    little better. I'm also open to ideas and suggestions so please drop an
    issue if you have one.

- **Q:** Why nox?
  - **A:** Duplicatable workflows that are platform agnostic. Whether locally,
    in a container, in a github action, or on your machine; there is one
    official way workflows are run.
