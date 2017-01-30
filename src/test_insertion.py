"""Test insertion sort."""

from insertion import insertion_sort
import pytest
import sys

INSERT_NUM_TABLE = [
    ([2, 1, 3], [1, 2, 3]),
    ([2, 4, 1, 3, 7, 9], [1, 2, 3, 4, 7, 9]),
    ([2, 4, 7, 9, 1, 3, 5, 11, 8, 6], [1, 2, 3, 4, 5, 6, 7, 8, 9, 11])
]

INSERT_STR_TABLE = [
    (["A", "C", "B"], ["A", "B", "C"]),
    (["D", "C", "B"], ["B", "C", "D"]),
    (["A", "D", "C", "F", "E", "B"], ["A", "B", "C", "D", "E", "F"]),
    (["A", "D", "C", "F", "E", "B", "d", "c", "b", "a"], ["A", "B", "C", "D", "E", "F", "a", "b", "c", "d"]),
    (["alpha", "charlie", "bravo", ], ['alpha', 'bravo', 'charlie']),
    (["alpha", "charlie", "bravo", "zulu", "yankee", "x-ray", "victor"], ['alpha', 'bravo', 'charlie', "victor", "x-ray", "yankee", "zulu"])
]

INSERT_MIX_TABLE = [
    (["A", 1, "B", "D", "F"], [1, 'A', 'B', 'D', 'F']),
    (["A", 1, "B", "D", "F", 2, 5], [1, 2, 5, 'A', 'B', 'D', 'F']),
    (["F", "E", "D", "C", "B", "a", 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 'B', 'C', 'D', 'E', 'F', 'a']),
    (["F", "E", "D", "C", "B", "e", "f", "d", "b", "c", "a", 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']),
]


@pytest.mark.parametrize("input, result", INSERT_NUM_TABLE)
def test_insert_with_num(input, result):
    """Numbers should be sorted high to low."""
    assert insertion_sort(input) == result


@pytest.mark.parametrize("input, result", INSERT_STR_TABLE)
def test_insert_with_str(input, result):
    """Letters should be sorted Alphabetically with Caps first."""
    assert insertion_sort(input) == result


@pytest.mark.parametrize("input, result", INSERT_MIX_TABLE)
def test_insert_with_mixed_vals(input, result):
    """Numbers should be sorted high to low."""
    if sys.version[0] == '2':
        assert insertion_sort(input) == result
    else:
        with pytest.raises(TypeError):
            insertion_sort(input)