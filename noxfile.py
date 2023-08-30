from __future__ import annotations

import pathlib
import shutil

import nox

# Control factors for finding pieces of the module
MODULE_NAME = "module_name"
TESTS_PATH = "tests"
COVERAGE_FAIL_UNDER = 50
REQUIREMENT_IN_FILES = [
    pathlib.Path("requirements/requirements.in"),
    pathlib.Path("requirements/requirements-dev.in"),
    pathlib.Path("requirements/requirements-test.in"),
]

# What we allowed to clean (delete)
CLEANABLE_TARGETS = [
    "./**/__pycache__",
    "./**/.mypy_cache",
    "./**/.pytest_cache",
    "./**/.coverage",
    "./**/.nox",
    "./**/dist",
    "./**/build",
    "./**/*.pyc",
    "./**/*.pyo",
    "./**/coverage.json",
    "./**/.coverage.*",
]


# Define the default sessions run when `nox` is called on the CLI
nox.options.sessions = [
    "tests_with_coverage",
    "coverage_combine_and_report",
    "mypy_check",
]


@nox.session(
    python=["3.8", "3.9", "3.10", "3.11", "3.12"],
)
def tests_with_coverage(session: nox.Session) -> None:
    """Run unit tests with coverage saved to partial file."""
    print_standard_logs(session)

    session.install(".[test]")
    session.run("coverage", "run", "-p", "-m", "pytest", TESTS_PATH)


@nox.session()
def coverage_combine_and_report(session: nox.Session) -> None:
    """Combine all coverage partial files and generate JSON report."""
    print_standard_logs(session)

    fail_under = f"--fail-under={COVERAGE_FAIL_UNDER}"

    session.install(".[test]")
    session.run("python", "-m", "coverage", "combine")
    session.run("python", "-m", "coverage", "report", "-m", fail_under)
    session.run("python", "-m", "coverage", "json")


@nox.session()
def mypy_check(session: nox.Session) -> None:
    """Run mypy against package and all required dependencies."""
    print_standard_logs(session)

    session.install(".")
    session.install("mypy")
    session.run("mypy", "-p", MODULE_NAME, "--no-incremental")


@nox.session(python=False)
def coverage(session: nox.Session) -> None:
    """Generate a coverage report. Does not use a venv."""
    session.run("coverage", "erase")
    session.run("coverage", "run", "-m", "pytest", TESTS_PATH)
    session.run("coverage", "report", "-m")


@nox.session(python=False)
def docker(session: nox.Session) -> None:
    """Run tests in a docker container. Requires docker damon running."""
    session.run("docker", "build", "-t", "pydocker-test", ".")
    session.run("docker", "run", "-it", "--rm", "pydocker-test")


@nox.session()
def build(session: nox.Session) -> None:
    """Build distrobution files."""
    print_standard_logs(session)

    session.install("build")
    session.run("python", "-m", "build")


@nox.session()
def update(session: nox.Session) -> None:
    """Process requirement*.in files, updating only additions/removals."""
    print_standard_logs(session)

    session.install("pip-tools")
    for filename in REQUIREMENT_IN_FILES:
        session.run("pip-compile", "--no-emit-index-url", str(filename))


@nox.session()
def upgrade(session: nox.Session) -> None:
    """Process requirement*.in files and upgrade all libraries as possible."""
    print_standard_logs(session)

    session.install("pip-tools")
    for filename in REQUIREMENT_IN_FILES:
        session.run("pip-compile", "--no-emit-index-url", "--upgrade", str(filename))


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
