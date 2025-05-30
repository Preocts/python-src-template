from __future__ import annotations

import os
import pathlib
import shutil
import sys

import nox

# Control factors for finding pieces of the module
MODULE_NAME = "module_name"
TESTS_PATH = "tests"
COVERAGE_FAIL_UNDER = 50
DEFAULT_PYTHON = "3.12"
PYTHON_MATRIX = ["3.9", "3.10", "3.11", "3.12", "3.13"]
VENV_PATH = ".venv"
REQUIREMENTS_PATH = "./requirements"

# What we allowed to clean (delete)
CLEANABLE_TARGETS = [
    "./dist",
    "./build",
    "./.nox",
    "./.coverage",
    "./.coverage.*",
    "./coverage.json",
    "./**/.mypy_cache",
    "./**/.pytest_cache",
    "./**/__pycache__",
    "./**/*.pyc",
    "./**/*.pyo",
]

# Define the default sessions run when `nox` is called on the CLI
nox.options.default_venv_backend = "uv|virtualenv"
nox.options.sessions = [
    "version_coverage",
    "coverage_combine",
    "mypy",
]


@nox.session(python=False)
def dev(session: nox.Session) -> None:
    """Setup a development environment by creating the venv and installs dependencies."""
    # Use the active environement if it exists, otherwise create a new one
    venv_path = os.environ.get("VIRTUAL_ENV", VENV_PATH)

    if sys.platform == "win32":
        py_command = "py"
        venv_path = f"{venv_path}/Scripts"
        activate_command = f"{venv_path}/activate"
    else:
        py_command = f"python{DEFAULT_PYTHON}"
        venv_path = f"{venv_path}/bin"
        activate_command = f"source {venv_path}/activate"

    if not os.path.exists(VENV_PATH):
        session.run(py_command, "-m", "venv", VENV_PATH, "--upgrade-deps")

    python = f"{venv_path}/python"
    requirement_files = get_requirement_files()

    session.run(python, "-m", "pip", "install", "-e", ".")
    for requirement_file in requirement_files:
        session.run(python, "-m", "pip", "install", "-r", requirement_file)

    session.run(python, "-m", "pip", "install", "pre-commit")
    session.run(f"{venv_path}/pre-commit", "install")

    if not os.environ.get("VIRTUAL_ENV"):
        session.log(f"\n\nRun '{activate_command}' to enter the virtual environment.\n")


@nox.session(python=PYTHON_MATRIX)
def version_coverage(session: nox.Session) -> None:
    """Run unit tests with coverage saved to partial file."""
    print_standard_logs(session)

    session.install(".")
    session.install("-r", "requirements/requirements.txt")
    session.install("-r", "requirements/requirements-test.txt")
    session.run("coverage", "run", "-p", "-m", "pytest", TESTS_PATH)


@nox.session(python=DEFAULT_PYTHON)
def coverage_combine(session: nox.Session) -> None:
    """Combine all coverage partial files and generate JSON report."""
    print_standard_logs(session)

    fail_under = f"--fail-under={COVERAGE_FAIL_UNDER}"

    session.install(".")
    session.install("-r", "requirements/requirements.txt")
    session.install("-r", "requirements/requirements-test.txt")
    session.run("python", "-m", "coverage", "combine")
    session.run("python", "-m", "coverage", "report", "-m", fail_under)
    session.run("python", "-m", "coverage", "json")


@nox.session(python=DEFAULT_PYTHON)
def mypy(session: nox.Session) -> None:
    """Run mypy against package and all required dependencies."""
    print_standard_logs(session)

    session.install(".")
    session.install("-r", "requirements/requirements.txt")
    session.install("-r", "requirements/requirements-dev.txt")
    session.run("mypy", "-p", MODULE_NAME, "--no-incremental")


@nox.session(python=False)
def coverage(session: nox.Session) -> None:
    """Generate a coverage report. Does not use a venv."""
    session.run("coverage", "erase")
    session.run("coverage", "run", "-m", "pytest", TESTS_PATH)
    session.run("coverage", "report", "-m")


@nox.session(python=DEFAULT_PYTHON)
def build(session: nox.Session) -> None:
    """Build distribution files."""
    print_standard_logs(session)

    session.install("build")
    session.run("python", "-m", "build")


@nox.session(python=DEFAULT_PYTHON, name="update-deps")
def update_deps(session: nox.Session) -> None:
    """Process requirement*.txt files, updating only additions/removals."""
    print_standard_logs(session)

    requirement_files = get_requirement_files()

    session.install("pip-tools")
    session.run(
        "pip-compile",
        "--no-annotate",
        "--no-emit-index-url",
        "--output-file",
        f"{REQUIREMENTS_PATH}/constraints.txt",
        *requirement_files,
    )


@nox.session(python=DEFAULT_PYTHON, name="upgrade-deps")
def upgrade_deps(session: nox.Session) -> None:
    """Process requirement*.txt files and upgrade all libraries as possible."""
    print_standard_logs(session)

    requirement_files = get_requirement_files()

    session.install("pip-tools")
    session.run(
        "pip-compile",
        "--no-annotate",
        "--no-emit-index-url",
        "--upgrade",
        "--output-file",
        f"{REQUIREMENTS_PATH}/constraints.txt",
        *requirement_files,
    )


@nox.session(python=False)
def clean(_: nox.Session) -> None:
    """Clean cache, .pyc, .pyo, and test/build artifact files from project."""
    count = 0
    for searchpath in CLEANABLE_TARGETS:
        for filepath in pathlib.Path(".").glob(searchpath):
            if filepath.is_dir():
                shutil.rmtree(filepath)
            else:
                filepath.unlink()
            count += 1

    print(f"{count} files cleaned.")


def print_standard_logs(session: nox.Session) -> None:
    """Reusable output for monitoring environment factors."""
    version = session.run("python", "--version", silent=True)
    session.log(f"Running from: {session.bin}")
    session.log(f"Running with: {version}")


def get_requirement_files() -> list[pathlib.Path]:
    """Get a list of requirement files matching "requirements*.txt"."""
    glob = pathlib.Path(REQUIREMENTS_PATH).glob("requirements*.txt")
    return [path for path in glob]
