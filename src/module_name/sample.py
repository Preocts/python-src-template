"""This is just a sample file"""

from __future__ import annotations

import requests


def main() -> bool:
    """Main"""
    print("The squared of 2 is", squared(2))
    return True


def squared(value: int) -> int:
    """Returns the squared value"""
    return value * value


def isodd(value: int) -> bool:
    """Return if value is odd."""
    return bool(value % 2)


def health_check() -> bool:
    """Returns true when github.com is accessible."""
    return requests.get("https://github.com").ok
