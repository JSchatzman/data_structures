"""Test heap.py."""


import pytest


HEAP_ORDER_CHECKER = [

    [100, [5, 9, 11, 14, 18, 19, 21, 33, 17, 27, 100]],
    [0, [0, 5, 11, 14, 9, 19, 21, 33, 17, 27, 18]],
    [12, [5, 9, 11, 14, 12, 19, 21, 33, 17, 27, 18]]]

HEAP_POP_CHECKER = [
    [[5, 9, 11, 14, 18, 19, 21, 33, 17, 27], [9, 14, 11, 17, 18, 19, 21, 33, 27]],
    [[1, 4, 5, 6], [4, 6, 5]],
    [[4], []]]


@pytest.fixture
def sample_heap():
    """Create testing heap."""
    from heap import Heap
    test_heap = Heap()
    test_heap.data = [5, 9, 11, 14, 18,
                      19, 21, 33, 17, 27]
    empty_heap = Heap()
    one_heap = Heap()
    one_heap.data = [5]
    return empty_heap, one_heap, test_heap


@pytest.mark.parametrize('value, result', HEAP_ORDER_CHECKER)
def test_various_pushes(value, result):
    """Test if various pushes result in proper stack."""
    heap = sample_heap()[2]
    heap.push(value)
    assert heap.data == result


@pytest.mark.parametrize('data, result', HEAP_POP_CHECKER)
def test_various_pops(data, result):
    """Test if various pops result in proper stack."""
    heap = sample_heap()[2]
    heap.data = data
    heap.pop()
    assert heap.data == result


def test_push_empty_increases_size(sample_heap):
    """Test if push increases size of empty heap."""
    sample_heap[0].push(1)
    assert len(sample_heap[0].data) == 1
    assert sample_heap[0].data == [1]


def test_push_one_increases_size(sample_heap):
    """Test if push increases size of empty heap."""
    sample_heap[1].push(1)
    assert len(sample_heap[1].data) == 2
    assert sample_heap[1].data == [1, 5]


def test_push_test_increases_size(sample_heap):
    """Test if push increases size of empty heap."""
    sample_heap[2].push(100)
    assert len(sample_heap[2].data) == 11


def test_pop_on_empty(sample_heap):
    """Test for pop on empty heap."""
    with pytest.raises(IndexError):
        sample_heap[0].pop()
