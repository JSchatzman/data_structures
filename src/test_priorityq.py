"""Test priority queue."""

import pytest


@pytest.fixture
def sample_priorityq():
    """Create sample priority queues."""
    from priorityq import Priorityq
    empty_pq = Priorityq()
    one_pq = Priorityq([(2, 3)])
    test_pq = Priorityq([(2, 3), (4, 5), (5, 3), (2, 4),
                        (2, 3), (2, 2), (2, 2), (10, 50), (-1, -5)])
    return empty_pq, one_pq, test_pq


def test_one_init_priorityq(sample_priorityq):
    """Test for length of one priorityq."""
    assert sample_priorityq[1].length == 1


def test_test_inti_priorityq(sample_priorityq):
    """Test for length of test priorityq."""
    assert sample_priorityq[2].length == 9



