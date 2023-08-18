from __future__ import annotations

import nox

MODULE_NAME = "module_name"
COVERAGE_FAIL_UNDER = "--fail-under=50"


@nox.session(
    python=["3.8", "3.9", "3.10", "3.11", "3.12"],
)
def tests_with_coverage(session: nox.Session) -> None:
    """Run unit tests with coverage saved to partial file."""
    print_standard_logs(session)

    session.install(".[test]")
    session.run("coverage", "run", "-p", "-m", "pytest", "tests/")


@nox.session()
def coverage_combine_and_report(session: nox.Session) -> None:
    """Combine all coverage partial files and generate JSON report."""
    print_standard_logs(session)

    session.install(".[test]")
    session.run("python", "-m", "coverage", "combine")
    session.run("python", "-m", "coverage", "report", "-m", COVERAGE_FAIL_UNDER)
    session.run("python", "-m", "coverage", "json")


@nox.session()
def mypy_check(session: nox.Session) -> None:
    """Run mypy against package and all required dependencies."""
    print_standard_logs(session)

    session.install(".")
    session.install("mypy")
    session.run("mypy", "-p", MODULE_NAME, "--no-incremental")


def print_standard_logs(session: nox.Session) -> None:
    """Reusable output for monitoring environment factors."""
    version = session.run("python", "--version", silent=True)
    session.log(f"Running from: {session.bin}")
    session.log(f"Running with: {version}")
