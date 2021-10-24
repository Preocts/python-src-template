# `src` Structured Projects

*Note: Any reference to installing a package with pip in this write-up is assuming the use of [`venv`](https://docs.python.org/3.8/library/venv.html)*

This style of project layout works especially well with source distribution planned projected. Because this layout removes your modules from being imported directly and forces you to import the installed version, you gain a level of confidence that your testing mimics the end-user's experience. Any over-looked assumptions on imports and opens will reveal themselves quickly. Your tests, also running off the installed version, will quickly identify missing requirements.

Take a look at this very basic tree showing the structure:

```
.
├── README.md
├── LICENSE
├── setup.cfg
├── setup.py
├── src
│   └── project_files
│       ├── __init__.py
│       ├── helper.py
│       └── main.py
└── tests
    ├── fixtures
    │   └── test_input.csv
    └── main_test.py
```

Per its name, you'll notice that our modules are nested under a directory called `src`.  Also notice that `src` itself is not a python package and is purposely missing the `__init__.py` file. This separates our `project_files` package and its modules from being imported directly.

Instead, we install our own package for development using an editable install in pip. The following section will walk through, briefly, how this is setup.

## Setting up an installable package

The requirements are to have our `setup.cfg` and `setup.py` filled with the minimal information for setup-tools to find our package and install it.

### setup.py

The setup.py file is on the verge of no longer being required. For now, however, we just need the following inside it:

```py
from setuptools import setup
setup()
```

### setup.cfg

This file contains everything the `setup.py` used to hold in easy to parse formats:

```ini
[metadata]
name = sample_project
version = 1.0.0
description = Module Description
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/[your repo]/[repo name]
author = [YOUR NAME]
author_email = [YOUR EMAIL]
license = MIT
license_file = LICENSE
classifiers =
    License :: OSI Approved :: MIT License
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: 3.9
    Programming Language :: Python :: 3.10
    Programming Language :: Python :: Implementation :: CPython

[options]
packages = find:
python_requires = >=3.8
package_dir =
    =src

[options.packages.find]
where = src
exclude =
    tests*
```

The `[metadata]` fills in the details about our project. The pieces that matter for our editable install are `[options]` and `[options.packages.find]`. Here we tell setup-tool that our package directory isn't the default `.` (root) but `src`. This gives the auto-discovery what it needs to discover and install the package.

Finally, to install the package we use the following `pip` command and options.

```bash
pip install --editable .
```

The `--editable` flag will tell pip to install our package in such a way that any changes we make to the source files will be immediately available in the installed package without re-installing. The `.` (period) tells pip to look for and install from the root of our project directory.

---
