#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Basic setup file """
from setuptools import find_packages
from setuptools import setup


setup(
    name="placeholder_name",
    version="0.0.0",
    license="MIT License",
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
