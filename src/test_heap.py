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


def test_push(sample_heap):
    """Test if push moves item."""
    # import pdb; pdb.set_trace()
    size = len(sample_heap.heap)
    sample_heap.push(6)
    assert len(sample_heap.heap) == size + 1
