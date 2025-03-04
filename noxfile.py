from __future__ import annotations

import functools
import pathlib
import shutil

import nox

# Control factors for finding pieces of the module
MODULE_NAME = "module_name"
TESTS_PATH = "tests"
COVERAGE_FAIL_UNDER = 50
DEFAULT_PYTHON_VERSION = None
PYTHON_MATRIX = ["3.9", "3.10", "3.11", "3.12", "3.13"]
VENV_BACKEND = "uv"

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
nox.options.sessions = [
    "version_coverage",
    "coverage_combine",
    "mypy",
]


@nox.session(python=PYTHON_MATRIX, venv_backend=VENV_BACKEND)
def version_coverage(session: nox.Session) -> None:
    """Run unit tests with coverage saved to partial file."""
    print_standard_logs(session)
    uv_run = functools.partial(session.run, "uv", "run", "--active")

    session.run("uv", "sync", "--active", "--no-dev", "--group", "test")
    uv_run("coverage", "run", "-p", "-m", "pytest", TESTS_PATH)


@nox.session(python=DEFAULT_PYTHON_VERSION, venv_backend=VENV_BACKEND)
def coverage_combine(session: nox.Session) -> None:
    """Combine all coverage partial files and generate JSON report."""
    print_standard_logs(session)
    uv_run = functools.partial(session.run, "uv", "run", "--active")

    session.run("uv", "sync", "--active", "--no-dev", "--group", "test")
    uv_run("coverage", "combine")
    uv_run("coverage", "report", "-m", f"--fail-under={COVERAGE_FAIL_UNDER}")
    uv_run("coverage", "json")


@nox.session(python=DEFAULT_PYTHON_VERSION, venv_backend=VENV_BACKEND)
def mypy(session: nox.Session) -> None:
    """Run mypy against package and all required dependencies."""
    print_standard_logs(session)
    uv_run = functools.partial(session.run, "uv", "run", "--active")

    session.run("uv", "sync", "--active", "--no-dev", "--group", "lint")
    uv_run("mypy", "-p", MODULE_NAME, "--no-incremental")


@nox.session(python=DEFAULT_PYTHON_VERSION, venv_backend=VENV_BACKEND)
def coverage(session: nox.Session) -> None:
    """Generate a coverage report. Does not use a venv."""
    print_standard_logs(session)
    uv_run = functools.partial(session.run, "uv", "run", "--active")

    session.run("uv", "sync", "--active", "--no-dev", "--group", "test")
    uv_run("coverage", "erase")
    uv_run("coverage", "run", "-m", "pytest", TESTS_PATH)
    uv_run("coverage", "report", "-m")
    uv_run("coverage", "html")


@nox.session(python=False, venv_backend=VENV_BACKEND)
def build(session: nox.Session) -> None:
    """Generate sdist and wheel."""
    session.run("uv", "build")


@nox.session(python=False, venv_backend=VENV_BACKEND)
def clean(session: nox.Session) -> None:
    """Clean cache, .pyc, .pyo, and test/build artifact files from project."""
    count = 0
    for searchpath in CLEANABLE_TARGETS:
        for filepath in pathlib.Path(".").glob(searchpath):
            if filepath.is_dir():
                shutil.rmtree(filepath)
            else:
                filepath.unlink()
            count += 1

    session.log(f"{count} files cleaned.")


def print_standard_logs(session: nox.Session) -> None:
    """Reusable output for monitoring environment factors."""
    version = session.run("python", "--version", silent=True)
    session.log(f"Running from: {session.bin}")
    session.log(f"Running with: {version}")
