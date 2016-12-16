"""Tests for queue.py."""

import pytest


@pytest.fixture
def sample_queue():
    """Create testing queues."""
    from queue import Queue
    one_queue = Queue(["one"])
    empty_queue = Queue()
    new_queue = Queue([1, 2, 3, 4, 5])
    return one_queue, empty_queue, new_queue


def test_queue_empty_init():
    """Test for empty queue init."""
    one_queue, empty_queue, new_queue = sample_queue()
    assert empty_queue.head_node is None
    assert empty_queue.tail_node is None


def test_queue_one_init():
    """Test for one item queue init."""
    one_queue, empty_queue, new_queue = sample_queue()
    assert one_queue.head_node.contents == "one"
    assert one_queue.tail_node.contents == "one"


def test_queue_init():
    """Test for queue init."""
    one_queue, empty_queue, new_queue = sample_queue()
    assert new_queue.head_node.contents == 5
    assert new_queue.tail_node.contents == 1


def test_queue_init_head():
    """Test for empty queue head node."""
    one_queue, empty_queue, new_queue = sample_queue()
    assert new_queue.head_node.contents == 5


def test_queue_init_tail():
    """Test for empty queue tail node."""
    one_queue, empty_queue, new_queue = sample_queue()
    assert new_queue.tail_node.contents == 1


def test_queue_enqueue():
    """Test for enqueue on queue."""
    one_queue, empty_queue, new_queue = sample_queue()
    new_queue.enqueue("hey")
    assert new_queue.head_node.contents == "hey"


def test_queue_enqueue_on_empty():
    """Test for enqueue on empty queue."""
    one_queue, empty_queue, new_queue = sample_queue()
    empty_queue.enqueue("hey")
    assert empty_queue.head_node.contents == "hey"


def test_queue_dequeue():
    """Test for enqueue on queue."""
    one_queue, empty_queue, new_queue = sample_queue()
    assert new_queue.dequeue() == 1


def test_queue_dequeue_on_empty():
    """Test for enqueue on empty queue."""
    one_queue, empty_queue, new_queue = sample_queue()
    with pytest.raises(ValueError):
        empty_queue.dequeue()


def test_queue_one_dequeue():
    """Test dequeue when queue has one item."""
    one_queue, empty_queue, new_queue = sample_queue()
    assert one_queue.dequeue() == "one"
    assert one_queue.tail_node is None
    assert one_queue.head_node is None


def test_queue_peek():
    """Test peek on queue."""
    one_queue, empty_queue, new_queue = sample_queue()
    assert new_queue.peek() == 1


def test_one_queue_peek():
    """Test peek on queue with one item."""
    one_queue, empty_queue, new_queue = sample_queue()
    assert one_queue.peek() == "one"


def test_empty_queue_peek():
    """Test peek on queue."""
    one_queue, empty_queue, new_queue = sample_queue()
    with pytest.raises(AttributeError):
        empty_queue.peek()
