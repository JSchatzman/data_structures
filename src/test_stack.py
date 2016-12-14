"""Tests for stack.py."""


def test_stack_init():
    """Test for Stack init."""
    from stack import Stack
    new_stack = Stack()
    assert new_stack.length == 0
    assert new_stack.head_node is None
    new_stack2 = Stack([1, 2, 3, 4, 5])
    assert new_stack2.head_node.contents == 5


def test_stack_push():
    """Test for Stack push."""
    from stack import Stack
    new_stack = Stack()
    new_stack.push(34)
    assert new_stack.head_node.contents == 34
    new_stack2 = Stack()
    new_stack2.push(None)
    assert new_stack2.head_node.contents is None


def test_stack_pop():
    """Test for Stack pop."""
    from stack import Stack
    new_stack = Stack(['a', 'b', 'c', 'd'])
    assert new_stack.length == 4
    assert new_stack.head_node
    assert new_stack.pop()
    assert new_stack.head_node.contents == 'c'
    empty_stack = Stack()
    try:
        empty_stack.pop()
    except TypeError:
        assert True
    one_stack = Stack([1])
    assert one_stack.head_node.next_node is None
    one_stack.pop()
    assert one_stack.head_node is None
