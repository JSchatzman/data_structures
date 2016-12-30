"""Test methods of the deque data structure."""

import pytest


@pytest.fixture
def sample_deque():
    """Create sample deque."""
    from deque import Deque
    new_queue = Deque([1, 2, 3, 4, 5])
    return new_queue


@pytest.fixture
def single_deque():
    """Create one length deque."""
    from deque import Deque
    one_queue = Deque(["one"])
    return one_queue


@pytest.fixture
def empty_deque():
    """Create empty deque."""
    from deque import Deque
    empty_queue = Deque()
    return empty_queue


def test_deque_empty_init(empty_deque):
    """Test for empty deque init."""
    assert empty_deque.dll.head_node is None
    assert empty_deque.dll.tail_node is None


def test_deque_one_init(single_deque):
    """Test for one item deque init."""
    assert single_deque.dll.head_node.contents == "one"
    assert single_deque.dll.tail_node.contents == "one"


def test_deque_init(sample_deque):
    """Test for new deque init."""
    assert sample_deque.dll.head_node.contents == 5
    assert sample_deque.dll.tail_node.contents == 1


def test_deque_appendleft(sample_deque):
    """Test for appendleft on new deque."""
    sample_deque.appendleft("hey")
    assert sample_deque.dll.head_node.contents == "hey"


def test_deque_appendleft_on_empty(empty_deque):
    """Test for appendleft on empty deque."""
    empty_deque.appendleft("hey")
    assert empty_deque.dll.head_node.contents == "hey"


def test_deque_appendleft_on_one(single_deque):
    """Test for appendleft on single deque."""
    single_deque.appendleft("hey")
    assert single_deque.dll.head_node.contents == "hey"


def test_deque_append(sample_deque):
    """Test for append on new deque."""
    sample_deque.append("hey")
    assert sample_deque.dll.tail_node.contents == "hey"


def test_deque_append_on_empty(empty_deque):
    """Test for append on empty deque."""
    empty_deque.append("hey")
    assert empty_deque.dll.tail_node.contents == "hey"


def test_deque_append_on_one(single_deque):
    """Test for append on single deque."""
    single_deque.append("hey")
    assert single_deque.dll.tail_node.contents == "hey"


def test_deque_pop(sample_deque):
    """Test for pop on new deque."""
    assert sample_deque.pop() == 1


def test_deque_pop_on_empty(empty_deque):
    """Test for pop on empty deque."""
    with pytest.raises(AttributeError):
        empty_deque.pop()


def test_deque_pop_on_one(single_deque):
    """Test for pop on single deque."""
    assert single_deque.pop() == 'one'


def test_deque_popleft(sample_deque):
    """Test for popleft on new deque."""
    assert sample_deque.popleft() == 5


def test_deque_popleft_on_empty(empty_deque):
    """Test for popleft on empty deque."""
    with pytest.raises(AttributeError):
        empty_deque.popleft()


def test_deque_popleft_on_one(single_deque):
    """Test for popleft on single deque."""
    assert single_deque.popleft() == 'one'


def test_deque_peek(sample_deque):
    """Test for peek on new deque."""
    assert sample_deque.peek() == 1


def test_deque_peek_on_empty(empty_deque):
    """Test for peek on empty deque."""
    assert not empty_deque.peek()


def test_deque_peek_on_one(single_deque):
    """Test for peek on single deque."""
    assert single_deque.peek() == 'one'


def test_deque_peekleft(sample_deque):
    """Test for peekleft on new deque."""
    assert sample_deque.peekleft() == 5


def test_deque_peekleft_on_empty(empty_deque):
    """Test for peekleft on empty deque."""
    assert not empty_deque.peekleft()


def test_deque_peekleft_on_one(single_deque):
    """Test for peekleft on single deque."""
    assert single_deque.peekleft() == 'one'


def test_deque_size(sample_deque):
    """Test for size on new deque."""
    assert sample_deque.size() == 5


def test_deque_size_on_empty(empty_deque):
    """Test for size on empty deque."""
    assert empty_deque.size() == 0


def test_deque_size_on_one(single_deque):
    """Test for size on single deque."""
    assert single_deque.size() == 1


def test_deque_size_increase(sample_deque):
    """Test that size increases after appending."""
    testing_deque = sample_deque
    testing_deque.append('test')
    testing_deque.appendleft('test2')
    assert testing_deque.size() == 7


def test_deque_size_decrease(sample_deque):
    """Test that size decreases after appending."""
    testing_deque = sample_deque
    testing_deque.pop()
    testing_deque.popleft()
    assert testing_deque.size() == 3
