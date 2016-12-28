"""Tests for stack.py."""

import pytest


@pytest.fixture
def sample_stack():
    """Create testing stacks."""
    from stack import Stack
    empty_stack = Stack()
    one_stack = Stack([1])
    new_stack = Stack([1, 2, 3, 4, 5])
    return (empty_stack, one_stack, new_stack)


def test_stack_empty_length(sample_stack):
    """Test for empty stack length."""
    assert sample_stack[0].length == 0


def test_stack_empty_head_node(sample_stack):
    """Test for empty stack head node."""
    assert sample_stack[0].head_node is None


def test_stack_new_length(sample_stack):
    """Test for new stack length."""
    assert sample_stack[2].length == 5


def test_stack_new_contents(sample_stack):
    """Test for new stack head node contents."""
    assert sample_stack[2].head_node.contents == 5


def test_stack_new_push(sample_stack):
    """Test for new stack head node contents."""
    sample_stack[2].push(34)
    assert sample_stack[2].head_node.contents == 34


def test_stack_one_push(sample_stack):
    """Test for new stack head node contents."""
    sample_stack[1].push(34)
    assert sample_stack[1].head_node.contents == 34


def test_stack_empty_push(sample_stack):
    """Test for empty stack head node contents."""
    sample_stack[0].push(34)
    assert sample_stack[0].head_node.contents == 34


def test_stack_new_pop(sample_stack):
    """Test that pop the new stack returns 5."""
    assert sample_stack[2].pop() == 5


def test_stack_new_pop_length(sample_stack):
    """Test that pop the new stack decreases length."""
    assert sample_stack[2].pop() == 5


def test_stack_one_pop(sample_stack):
    """Test that pop of one stack returns 1."""
    assert sample_stack[1].pop() == 1


def test_stack_one_pop_contents(sample_stack):
    """Test that pop of one stack behaves as expeted."""
    sample_stack[1].pop()
    assert sample_stack[1].head_node is None


def tst_stack_empty_pop(sample_stack):
    """Test that pop empty stack throws correct error."""
    with pytest.raises(TypeError):
        sample_stack[0].pop()
