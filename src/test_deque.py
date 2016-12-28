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


def test_deque_appendleft(sample_deque):
    """Test for appendleft on new deque."""
    sample_deque[2].appendleft("hey")
    assert sample_deque[2].head_node.contents == "hey"


def test_deque_appendleft_on_empty(sample_deque):
    """Test for appendleft on empty deque."""
    sample_deque[1].appendleft("hey")
    assert sample_deque[1].head_node.contents == "hey"


def test_deque_appendleft_on_one(sample_deque):
    """Test for appendleft on empty deque."""
    sample_deque[0].appendleft("hey")
    assert sample_deque[0].head_node.contents == "hey"


def test_deque_append(sample_deque):
    """Test for append on new deque."""
    sample_deque[2].append("hey")
    assert sample_deque[2].tail_node.contents == "hey"


def test_deque_append_on_empty(sample_deque):
    """Test for append on empty deque."""
    sample_deque[1].append("hey")
    assert sample_deque[1].tail_node.contents == "hey"


def test_deque_append_on_one(sample_deque):
    """Test for append on empty deque."""
    sample_deque[0].append("hey")
    assert sample_deque[0].tail_node.contents == "hey"


def test_deque_pop(sample_deque):
    """Test for pop on new deque."""
    assert sample_deque[2].pop() == 1


def test_deque_pop_on_empty(sample_deque):
    """Test for pop on empty deque."""
    with pytest.raises(ValueError):
        sample_deque[1].pop()


def test_deque_pop_on_one(sample_deque):
    """Test for pop on empty deque."""
    assert sample_deque[0].pop() == 'one'


def test_deque_popleft(sample_deque):
    """Test for popleft on new deque."""
    assert sample_deque[2].popleft() == 5


def test_deque_popleft_on_empty(sample_deque):
    """Test for popleft on empty deque."""
    with pytest.raises(ValueError):
        sample_deque[1].popleft()


def test_deque_popleft_on_one(sample_deque):
    """Test for popleft on empty deque."""
    assert sample_deque[0].popleft() == 'one'


def test_deque_peek(sample_deque):
    """Test for peek on new deque."""
    assert sample_deque[2].peek() == 1


def test_deque_peek_on_empty(sample_deque):
    """Test for peek on empty deque."""
    with pytest.raises(AttributeError):
        sample_deque[1].peek()


def test_deque_peek_on_one(sample_deque):
    """Test for peek on empty deque."""
    assert sample_deque[0].peek() == 'one'


def test_deque_peekleft(sample_deque):
    """Test for peekleft on new deque."""
    assert sample_deque[2].peekleft() == 5


def test_deque_peekleft_on_empty(sample_deque):
    """Test for peekleft on empty deque."""
    with pytest.raises(AttributeError):
        sample_deque[1].peekleft()


def test_deque_peekleft_on_one(sample_deque):
    """Test for peekleft on empty deque."""
    assert sample_deque[0].peekleft() == 'one'


def test_deque_size(sample_deque):
    """Test for size on new deque."""
    assert sample_deque[2].size() == 5


def test_deque_size_on_empty(sample_deque):
    """Test for size on empty deque."""
    assert sample_deque[1].size() == 0


def test_deque_size_on_one(sample_deque):
    """Test for size on empty deque."""
    assert sample_deque[0].size() == 1
