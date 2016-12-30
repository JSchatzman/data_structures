"""Test priority queue."""

import pytest


@pytest.fixture
def sample_priorityq():
    """Create sample priority queues."""
    from priorityq import Priorityq
    empty_pq = Priorityq()
    one_pq = Priorityq([(3, 2)])
    multi_pq = Priorityq([(3, 2), (5, 4), ('hey', 5), ('hello', 2),
                         (3, 2), (2, 2), ('jordan', 2), (50, 10),
                         (-5, 0), (100, 5)])
    return empty_pq, one_pq, multi_pq


def test_one_init_priorityq(sample_priorityq):
    """Test for length of one priorityq."""
    assert 2 in sample_priorityq[1].data.keys()


def test_multi_inti_priorityq(sample_priorityq):
    """Test for length of test priorityq."""
    assert 10 in sample_priorityq[2].data.keys()


def test_init_priorityq():
    """Test priorityq is initiliazed with prority and values."""
    from priorityq import Priorityq
    p = Priorityq([('val1', 0), ('val2', 0)])
    assert p.data == {0: ['val1', 'val2']}


def test_empty_insert_priorityq(sample_priorityq):
    """Test insert into empty priorityq."""
    sample_priorityq[0].insert(2)
    sample_priorityq[0].insert(1, 3)
    assert 1 in sample_priorityq[0].data[3]
    assert 2 in sample_priorityq[0].data[0]


def test_one_insert_priorityq(sample_priorityq):
    """Test insert into queue of 1."""
    sample_priorityq[1].insert(1, 3)
    sample_priorityq[1].insert(2)
    assert 1 in sample_priorityq[1].data[3]
    assert 2 in sample_priorityq[1].data[0]


def test_multi_insert_priorityq(sample_priorityq):
    """Test insert into larger queue."""
    sample_priorityq[2].insert(1, 3)
    sample_priorityq[2].insert(2)
    assert 2 in sample_priorityq[2].data[0]
    assert 1 in sample_priorityq[2].data[3]


def test_empty_pop_priorityq(sample_priorityq):
    """Test pop empty priorityq."""
    with pytest.raises(IndexError):
        sample_priorityq[0].pop()


def test_one_pop_priorityq(sample_priorityq):
    """Test pop data of one."""
    return_val = sample_priorityq[1].pop()
    assert return_val == 3


def test_multi_pop_priorityq(sample_priorityq):
    """Test pop data on long queue."""
    return_val = sample_priorityq[2].pop()
    assert return_val == 50


def test_multi_pop_priorityq_multiple_times(sample_priorityq):
    """Test pop data on long queue."""
    pq = sample_priorityq[2]
    pq.pop()
    pq.pop()
    pq.pop()
    assert pq.pop() == 5


def test_multi_peek_priorityq(sample_priorityq):
    """Test peek data on long queue."""
    assert sample_priorityq[2].peek() == 50


def test_one_peek_priorityq(sample_priorityq):
    """Test peek data on one queue."""
    assert sample_priorityq[1].peek() == 3


def test_empty_peek_priorityq(sample_priorityq):
    """Test peek data on empty queue."""
    assert sample_priorityq[0].peek() is None


def test_priorityq_fifo():
    """Test pop on priority q returns first in."""
    from priorityq import Priorityq
    pq = Priorityq([('val1', 0), ('val2', 0), ('val3', 1), ('val4', 5)])
    pq.pop()
    pq.pop()
    assert pq.pop() == 'val1'
