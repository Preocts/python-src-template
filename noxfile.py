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
nox.options.sessions = ["format", "lint", "test"]

# All linters and formatters are run with `uv run --active`
LINTERS: list[tuple[str, ...]] = [
    ("flake8", "--verbose", "--show-source", LINT_PATH, TESTS_PATH),
    ("mypy", "--pretty", "--no-incremental", "--package", MODULE_NAME),
    ("mypy", "--pretty", "--no-incremental", TESTS_PATH),
]
FORMATTERS: list[tuple[str, ...]] = [
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
]


@nox.session(name="dev", python=False)
def dev_session(session: nox.Session) -> None:
    """Create a development environment. Optionally: Provide the python version to use."""
    python_version: list[str] = []
    if session.posargs:
        python_version = ["--python", session.posargs[0]]

    session.run_install("uv", "sync", "--frozen", "--all-groups", *python_version, external=True)
    session.run_install("uv", "run", "pre-commit", "install", external=True)


@nox.session(name="test")
def run_tests_with_coverage(session: nox.Session) -> None:
    """Run pytest in isolated environment, display coverage. Extra arguements passed to pytest."""
    print_standard_logs(session)

    partial = "partial-coverage" in session.posargs
    extra: list[str] = []
    if "no-config" in session.posargs:
        session.posargs.remove("no-config")
        extra = ["--no-config"]

    session.run_install("uv", "sync", "--frozen", "--active", "--group", "test", *extra)

    coverage = functools.partial(session.run, "uv", "run", "--active", *extra, "coverage")

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
    print_standard_logs(session)

    session.run_install("uv", "sync", "--frozen", "--active", "--group", "test")

    coverage = functools.partial(session.run, "uv", "run", "--active", "coverage")

    coverage("combine")
    coverage("report", "--show-missing", f"--fail-under={COVERAGE_FAIL_UNDER}")
    coverage("html")
    coverage("json")


@nox.session(name="lint")
def run_linters(session: nox.Session) -> None:
    """Run code linters, and type checking against all files."""
    print_standard_logs(session)

    session.run_install("uv", "sync", "--frozen", "--active", "--group", "test", "--group", "lint")

    for linter_args in LINTERS:
        session.run("uv", "run", "--active", *linter_args)


@nox.session(name="format")
def run_formatters(session: nox.Session) -> None:
    """Run code formatters against all files."""
    print_standard_logs(session)

    session.run_install("uv", "sync", "--frozen", "--active", "--group", "format")

    for formatter_args in FORMATTERS:
        session.run("uv", "run", "--active", *formatter_args)


@nox.session(name="build")
def build_artifacts(session: nox.Session) -> None:
    """Build a sdist and wheel."""
    print_standard_logs(session)

    session.run("uv", "build")


@nox.session(name="upgrade")
def upgrade_dependencies(session: nox.Session) -> None:
    """Upgrade all versions of all dependencies."""
    print_standard_logs(session)

    session.run("uv", "lock", "--upgrade")


@nox.session(name="upgrade-package")
def upgrade_specific_package(session: nox.Session) -> None:
    """Upgrade specific package name given in extra args."""
    print_standard_logs(session)

    if not session.posargs:
        session.log("No package name provided, nothing to do.")

    else:
        session.run("uv", "lock", "--upgrade-package", *session.posargs)


@nox.session(python=False)
def clean(session: nox.Session) -> None:
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


def print_standard_logs(session: nox.Session) -> None:
    """Reusable output for monitoring environment factors."""
    version = session.run("python", "--version", silent=True)
    session.log(f"Running from: {session.bin}")
    session.log(f"Running with: {version}")
