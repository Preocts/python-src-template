#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


setup(
    name="placeholder_name",
    version="0.0.0",
    license="GNU General Public License",
    description="Put a description here",
    author="Preocts",
    author_email="preocts@preocts.com",
    url="https://github.com/Preocts/",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        "console_scripts": [
            "phstart=modulename.poe:func"
        ]
    },
    include_package_data=False
)
