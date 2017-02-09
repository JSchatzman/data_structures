"""Test Suite for Radix.py."""

import pytest

SORT_LISTS = [
    (55, 79, 5000, 2522, 33, 1),
    [7988, 25, 3, 2, 1],
    (9, 8, 7, 6, 5, 4, 3, 2, 1),
    [1, 2, 3, 5, 6, 3, 2, 33, 22, 5, 77, 111111],
]


@pytest.mark.parametrize("input_lists", SORT_LISTS)
def test_radix(input_lists):
    """Test radix sort works."""
    from radix import radix_sort
    assert radix_sort(input_lists) == sorted(input_lists)
