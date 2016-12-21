"""Test priority queue."""

import pytest


@pytest.fixture
def sample_priorityq():
    """Create sample priority queues."""
    from priorityq import Priorityq
    empty_pq = Priorityq()
    one_pq = Priorityq([(2, 3)])
    multi_pq = Priorityq([(2, 3), (4, 5), (5, 'hey'), (2, 'hello'),
                        (2, 3), (2, 2), (2, 'jordan'), (10, 50), (0, -5), (5, 100)])
    return empty_pq, one_pq, multi_pq


def test_one_init_priorityq(sample_priorityq):
    """Test for length of one priorityq."""
    assert len(sample_priorityq[1].data) == 1


def test_multi_inti_priorityq(sample_priorityq):
    """Test for length of test priorityq."""
    assert len(sample_priorityq[2].data) == 9


def test_empty_insert_priorityq(sample_priorityq):
    """Test insert into empty priorityq."""
    sample_priorityq[0].insert(1)
    assert len(sample_priorityq[0].data) == 1


def test_one_insert_priorityq(sample_priorityq):
    sample_priorityq[1].insert(1)
    assert len(sample_priorityq[1].data) == 2


def test_multi_insert_priorityq(sample_priorityq):
    sample_priorityq[1].insert(1)
    assert len(sample_priorityq[2].data) == 2