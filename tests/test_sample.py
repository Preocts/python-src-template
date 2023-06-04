"""Tests for sample"""
from __future__ import annotations

import pytest

from module_name import sample


def test_main():
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
def test_squared(value_in, expected):
    assert sample.squared(value_in) == expected
