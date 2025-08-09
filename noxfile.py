from __future__ import annotations

import functools
import pathlib
import shutil

import nox

# Control factors for finding pieces of the module
MODULE_NAME = "module_name"
COVERAGE_FAIL_UNDER = "100"
LINT_PATH = "./src"
TESTS_PATH = "./tests"

# What we allowed to clean (delete)
CLEANABLE_TARGETS = [
    "./dist",
    "./build",
    "./.nox",
    "./.coverage",
    "./.coverage.*",
    "./coverage.json",
    "./htmlcov",
    "./**/.mypy_cache",
    "./**/.pytest_cache",
    "./**/__pycache__",
    "./**/*.pyc",
    "./**/*.pyo",
]

# Define the default sessions run when `nox` is called on the CLI
nox.options.default_venv_backend = "uv"
nox.options.sessions = ["lint", "test"]

# All linters are run with `uv run --active`
# Ordering matters. Formatters should run before static checks.
LINTERS: list[tuple[str, ...]] = [
    (
        "isort",
        "--verbose",
        "--force-single-line-imports",
        "--profile",
        "black",
        "--add-import",
        "from __future__ import annotations",
        LINT_PATH,
        TESTS_PATH,
    ),
    ("black", "--verbose", LINT_PATH, TESTS_PATH),
    ("flake8", "--verbose", "--show-source", LINT_PATH, TESTS_PATH),
    ("mypy", "--pretty", "--no-incremental", "--package", MODULE_NAME),
    ("mypy", "--pretty", "--no-incremental", TESTS_PATH),
]


@nox.session(name="dev", python=False)
def dev_session(session: nox.Session) -> None:
    """Create a development environment. Optionally: Provide the python version to use."""
    python_version: list[str] = []
    if session.posargs:
        python_version = ["--python", session.posargs[0]]

    session.run("uv", "sync", *python_version, external=True)
    session.run("uv", "run", "pre-commit", "install", external=True)


@nox.session(name="test")
def run_tests_with_coverage(session: nox.Session) -> None:
    """Run pytest in isolated environment, display coverage. Extra arguements passed to pytest."""
    partial = "partial-coverage" in session.posargs

    session.run("uv", "sync", "--active", "--no-dev", "--group", "test")

    coverage = functools.partial(session.run, "uv", "run", "--active", "coverage")

    coverage("erase")

    if partial:
        session.posargs.remove("partial-coverage")
        coverage("run", "--parallel-mode", "--module", "pytest", *session.posargs)
    else:
        coverage("run", "--module", "pytest", *session.posargs)
        coverage("report", "--show-missing", f"--fail-under={COVERAGE_FAIL_UNDER}")
        coverage("html")


@nox.session(name="combine")
def combine_coverage(session: nox.Session) -> None:
    """Combine parallel-mode coverage files and produce reports."""
    session.run("uv", "sync", "--active", "--no-dev", "--group", "test")

    coverage = functools.partial(session.run, "uv", "run", "--active", "coverage")

    coverage("combine")
    coverage("report", "--show-missing", f"--fail-under={COVERAGE_FAIL_UNDER}")
    coverage("html")


@nox.session(name="lint")
def run_linters_and_formatters(session: nox.Session) -> None:
    """Run code formatters, linters, and type checking against all files."""
    session.run("uv", "sync", "--active", "--no-dev", "--group", "test", "--group", "lint")

    for linter_args in LINTERS:
        session.run("uv", "run", "--active", *linter_args)


@nox.session(name="build")
def build_artifacts(session: nox.Session) -> None:
    """Build a sdist and wheel."""
    session.run("uv", "build")


# update-deps
# upgrade-deps


@nox.session(python=False)
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
