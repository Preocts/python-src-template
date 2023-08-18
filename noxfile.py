from __future__ import annotations

import nox

MODULE_NAME = "module_name"
COVERAGE_FAIL_UNDER = "--fail-under=50"


@nox.session(
    python=["3.8", "3.9", "3.10", "3.11", "3.12"],
)
def tests_with_coverage(session: nox.Session) -> None:
    session.log(f"Running from: {session.bin}")
    session.log(f"Running with: {session.python}")
    session.install(".[test]")
    session.run("coverage", "run", "-p", "-m", "pytest", "tests/")


@nox.session()
def coverage_combine_and_report(session: nox.Session) -> None:
    version = session.run("python", "--version", silent=True)
    session.log(f"Running from: {session.bin}")
    session.log(f"Running with: {version}")

    session.install(".[test]")
    session.run("python", "-m", "coverage", "combine")
    session.run("python", "-m", "coverage", "report", "-m", COVERAGE_FAIL_UNDER)
    session.run("python", "-m", "coverage", "json")


@nox.session()
def mypy_check(session: nox.Session) -> None:
    version = session.run("python", "--version", silent=True)
    session.log(f"Running from: {session.bin}")
    session.log(f"Running with: {version}")

    session.install(".")
    session.install("mypy")
    session.run("mypy", "-p", MODULE_NAME, "--no-incremental")
