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
make dev-install
```

To exit the `venv`:
```bash
deactivate
```

