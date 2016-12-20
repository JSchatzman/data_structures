"""Test heap.py."""


import pytest


PARENT_CHILD_INDEX = [
    [9, 4]
]


@pytest.fixture
def sample_heap():
    """Create testing heap."""
    from heap import Heap
    test_heap = Heap()
    return test_heap


@pytest.mark.parametrize('index, result', PARENT_CHILD_INDEX)
def test_find_parent_index(index, result):
    """Test function returns parent index."""
    from heap import Heap
    heap = Heap()
    assert heap.find_parent_index(index) == result


def test_push_increases_size(sample_heap):
    """Test if push increases size of heap."""
    # import pdb; pdb.set_trace()
    size = len(sample_heap.data)
    sample_heap.push(6)
    assert len(sample_heap.data) == size + 1


def test_push_sorts_order(sample_heap):
    """Test if push creates the right order of heap."""
    sample_heap.push(6)
    assert sample_heap.data == [5, 6, 11, 14, 9, 19, 21, 33, 17, 27, 18]



