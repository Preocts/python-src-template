from __future__ import annotations

import dataclasses
import os
import re
from collections.abc import Callable
from functools import wraps
from pathlib import Path
from typing import Any

PLACEHOLDER_FILES = [
    Path("src/module_name/sample_data/sample.csv"),
    Path("src/module_name/sample_data/sample.json"),
    Path("src/module_name/sample.py"),
    Path("tests/test_sample.py"),
]
PLACEHOLDER_DIR = [Path("src/module_name/sample_data")]
PYPROJECT_TARGET = Path("pyproject.toml")
README_TARGET = Path("README.md")
ALT_FILE_DIR = Path("alt_files")
REQUIREMENTS_DIR = Path("requirements")
ORG = "Preocts"
REPO = r"python\-src\-template"


@dataclasses.dataclass
class ProjectData:
    name: str = "module-name"
    module: str = "module_name"
    version: str = "0.1.0"
    description: str = "Module Description"
    author_email: str = "yourname@email.invalid"
    author_name: str = "[YOUR NAME]"
    org_name: str = "[ORG NAME]"
    repo_name: str = "[REPO NAME]"


def bookends(label: str) -> Callable[..., Callable[..., None]]:
    """Add start/stop print statements to functoin calls."""

    def dec_bookends(func: Callable[..., Any]) -> Callable[..., None]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> None:
            print(f"{label}...")
            func(*args, **kwargs)
            print("Done.\n")

        return wrapper

    return dec_bookends


@bookends("Deleting placeholder files")
def delete_placeholder_files() -> None:
    """Delete placeholder files."""
    for file in PLACEHOLDER_FILES:
        if file.exists():
            os.remove(file)


@bookends("Deleting placeholder directories")
def delete_placeholder_directories() -> None:
    """Remove placeholder directories."""
    for directory in PLACEHOLDER_DIR:
        if directory.exists():
            os.rmdir(directory)


def get_input(prompt: str) -> str:
    """Extract input for ease of testing."""
    return input(prompt)


def select_project_type() -> None:
    """Select whether alt_files should be used."""
    user_input = get_input("Switch to dependencies in pyproject.toml? (y/N) : ")
    if user_input.lower() == "y":
        for file in ALT_FILE_DIR.iterdir():
            file.replace(file.name)

        # Remove requirements directory and all contents
        for file in REQUIREMENTS_DIR.iterdir():
            os.remove(file)
        os.rmdir(REQUIREMENTS_DIR)

    # Remove alt_files directory and all contents
    for file in ALT_FILE_DIR.iterdir():
        os.remove(file)
    os.rmdir(ALT_FILE_DIR)


def get_project_data() -> ProjectData:
    """Query user for details on the project. This is the quiz."""
    data = ProjectData()
    data.name = os.path.basename(os.getcwd())
    data.module = data.name.replace("-", "_")
    data.repo_name = os.path.basename(os.getcwd())
    for key, value in dataclasses.asdict(data).items():
        user_input = get_input(f"Enter {key} (default: {value}) : ")
        if user_input:
            setattr(data, key, user_input)
    data.module = data.name.replace("-", "_")
    return data


@bookends("Updating pyproject.toml values")
def replace_pyproject_values(data: ProjectData) -> None:
    """Update pyproject values."""
    pyproject = PYPROJECT_TARGET.read_text()
    for key, value in dataclasses.asdict(ProjectData()).items():
        pattern = re.compile(re.escape(value))
        pyproject = pattern.sub(getattr(data, key), pyproject)

    PYPROJECT_TARGET.write_text(pyproject)


@bookends("Updating badges in README.md")
def replace_readme_values(data: ProjectData) -> None:
    """Update badge urls and placeholders in README.md"""
    readme = README_TARGET.read_text()
    default = ProjectData()

    readme = re.sub(ORG, data.org_name, readme)
    readme = re.sub(REPO, data.repo_name, readme)
    readme = re.sub(re.escape(default.org_name), data.org_name, readme)
    readme = re.sub(re.escape(default.repo_name), data.repo_name, readme)

    README_TARGET.write_text(readme)


@bookends("Renaming src/module_name folder")
def rename_module_folder(name: str) -> None:
    """Rename module folder."""
    name = name.replace("-", "_")
    os.rename("src/module_name", f"src/{name}")


if __name__ == "__main__":
    print("Eggcellent template setup:\n")

    select_project_type()

    project_data = get_project_data()

    replace_pyproject_values(project_data)
    replace_readme_values(project_data)

    rename_module_folder(project_data.name)

    delete_placeholder_files()
    delete_placeholder_directories()
