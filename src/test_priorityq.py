"""Test priority queue."""

import pytest


@pytest.fixture
def sample_priorityq():
    """Create sample priority queues."""
    from priorityq import Priorityq
    empty_pq = Priorityq()
    one_pq = Priorityq([(2, 3)])
    multi_pq = Priorityq([(2, 3), (4, 5), (5, 'hey'), (2, 'hello'),
                         (2, 3), (2, 2), (2, 'jordan'), (10, 50),
                         (0, -5), (5, 100)])
    return empty_pq, one_pq, multi_pq


def test_one_init_priorityq(sample_priorityq):
    """Test for length of one priorityq."""
    assert 2 in sample_priorityq[1].data.keys()


def test_multi_inti_priorityq(sample_priorityq):
    """Test for length of test priorityq."""
    assert 10 in sample_priorityq[2].data.keys()


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
