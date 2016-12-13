"""Tests for stack.py."""


def test_node_init():
    """Test node class init."""
    from stack import Node
    new_node = Node(1, None)
    assert new_node.contents == 1 and new_node.next_node is None


def test_stack_init():
    """Test for Stack init."""
    from stack import Node, Stack
    new_stack = Stack()
    assert new_stack.length == 0
    assert new_stack.head_node is None
    new_stack2 = Stack([1, 2, 3, 4, 5])
    assert new_stack2.head_node.contents == 5
    assert new_stack2.length == 5


def test_stack_push():
    """Test for Stack push."""
    from stack import Node, Stack
    new_stack = Stack()
    new_stack.push(34)
    assert new_stack.length == 1
    assert new_stack.head_node.contents == 34
    new_stack2 = Stack()
    new_stack2.push(None)
    assert new_stack2.head_node.contents is None


def test_stack_pop():
    """Test for Stack pop."""
    from stack import Node, Stack
    new_node = Node(34, None)
    new_llist = Stack(new_node)
    new_llist.push(1)
    new_llist.pop()
    assert new_llist.head_node.contents == 34
    assert new_llist.length == 1
