"""Test methods of the deque data structure."""

import pytest


@pytest.fixture
def sample_deque():
    """Create deques to test."""
    from deque import Deque
    one_deque = Deque(["one"])
    empty_deque = Deque()
    new_deque = Deque([1, 2, 3, 4, 5])
    return one_deque, empty_deque, new_deque


def test_deque_empty_init(sample_deque):
    """Test for empty deque init."""
    assert sample_deque[1].head_node is None
    assert sample_deque[1].tail_node is None


def test_deque_one_init(sample_deque):
    """Test for one item deque init."""
    assert sample_deque[0].head_node.contents == "one"
    assert sample_deque[0].tail_node.contents == "one"


def test_deque_init(sample_deque):
    """Test for new deque init."""
    assert sample_deque[2].head_node.contents == 5
    assert sample_deque[2].tail_node.contents == 1


def test_queue_appendleft(sample_deque):
    """Test for appendleft on new deque."""
    sample_deque[2].appendleft("hey")
    assert sample_deque[2].head_node.contents == "hey"


def test_queue_appendleft_on_empty(sample_deque):
    """Test for appendleft on empty queue."""
    sample_deque[1].appendleft("hey")
    assert sample_deque[1].head_node.contents == "hey"
