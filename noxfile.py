from __future__ import annotations

import functools
import pathlib
import shutil

import nox

# Control factors for finding pieces of the module
MODULE_NAME = "module_name"
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
nox.options.sessions = ["lock", "format", "lint", "test"]

# All linters and formatters are run with `uv run --active`
LINTERS: list[tuple[str, ...]] = [
    ("flake8", "--show-source", LINT_PATH, TESTS_PATH),
    ("mypy", "--pretty", "--package", MODULE_NAME),
    ("mypy", "--pretty", TESTS_PATH),
]
FORMATTERS: list[tuple[str, ...]] = [
    (
        "isort",
        "--force-single-line-imports",
        "--profile",
        "black",
        "--add-import",
        "from __future__ import annotations",
        LINT_PATH,
        TESTS_PATH,
    ),
    ("black", LINT_PATH, TESTS_PATH),
]

# Default args for all uv sync calls
SYNC_ARGS = ["--frozen", "--quiet"]


@nox.session(name="dev", python=False)
def dev_session(session: nox.Session) -> None:
    """Create a development environment."""
    session.run_install("uv", "sync", *SYNC_ARGS)


@nox.session(name="test", python=False)
def run_tests_with_coverage(session: nox.Session) -> None:
    """Run pytest in isolated environment, display coverage. Extra arguements passed to pytest."""
    partial = "partial-coverage" in session.posargs
    extra: list[str] = []

    session.run_install("uv", "sync", *SYNC_ARGS, *extra)

    coverage = functools.partial(session.run, "uv", "run", *extra, "coverage")

    coverage("erase")

    if partial:
        session.posargs.remove("partial-coverage")
        coverage("run", "--parallel-mode", "--module", "pytest", *session.posargs)
    else:
        coverage("run", "--module", "pytest", *session.posargs)
        coverage("report", "--show-missing")
        coverage("html")


@nox.session(name="combine", python=False)
def combine_coverage(session: nox.Session) -> None:
    """Combine parallel-mode coverage files and produce reports."""
    session.run_install("uv", "sync", *SYNC_ARGS)

    coverage = functools.partial(session.run, "uv", "run", "coverage")

    coverage("combine")
    coverage("report", "--show-missing")
    coverage("html")
    coverage("json")


@nox.session(name="lint", python=False)
def run_linters(session: nox.Session) -> None:
    """Run code linters, and type checking against all files."""
    session.run_install("uv", "sync", "--group", "lint", *SYNC_ARGS)

    for linter_args in LINTERS:
        session.run("uv", "run", *linter_args)


@nox.session(name="format", python=False)
def run_formatters(session: nox.Session) -> None:
    """Run code formatters against all files."""
    session.run_install("uv", "sync", "--group", "format", *SYNC_ARGS)

    for formatter_args in FORMATTERS:
        session.run("uv", "run", *formatter_args)


@nox.session(name="build", python=False)
def build_artifacts(session: nox.Session) -> None:
    """Build a sdist and wheel."""
    session.run("uv", "build")


@nox.session(name="lock", python=False)
def validate_lock_file(session: nox.Session) -> None:
    """Ensure the uv.lock file exists and is aligned with dependencies."""
    session.run("uv", "lock")


@nox.session(name="upgrade", python=False)
def upgrade_dependencies(session: nox.Session) -> None:
    """Upgrade all versions of all dependencies."""
    session.run("uv", "lock", "--upgrade")


@nox.session(name="upgrade-package", python=False)
def upgrade_specific_package(session: nox.Session) -> None:
    """Upgrade specific package name given in extra args."""
    if not session.posargs:
        session.log("No package name provided, nothing to do.")

    else:
        session.run("uv", "lock", "--upgrade-package", *session.posargs)


@nox.session(name="clean", python=False)
def clean_project_files(session: nox.Session) -> None:
    """Clean cache, .pyc, .pyo, and build artifact files from project."""
    count = 0
    for searchpath in CLEANABLE_TARGETS:
        for filepath in pathlib.Path(".").glob(searchpath):
            if filepath.is_dir():
                shutil.rmtree(filepath)
            else:
                filepath.unlink()
            count += 1

    session.log(f"{count} files cleaned.")
