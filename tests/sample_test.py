"""Tests for sample"""

from __future__ import annotations

import pytest

from module_name import sample


def test_main() -> None:
    """Main test"""
    assert sample.main()


@pytest.mark.parametrize(
    ("value_in", "expected"),
    (
        (2, 4),
        (4, 16),
        (16, 256),
    ),
)
def test_squared(value_in: int, expected: int) -> None:
    assert sample.squared(value_in) == expected


def test_health_check() -> None:
    assert sample.health_check()
