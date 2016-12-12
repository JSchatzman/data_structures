"""Tests for linked_list.py."""


def test_node_init():
    """Test node class init."""
    from linked_list import Node
    new_node = Node(1, None)
    assert new_node.contents == 1 and new_node.next_node is None


def test_linkedlist_init():
    """Test for LinkedList init."""
    from linked_list import Node, LinkedList
    new_node = Node(34, None)
    new_llist = LinkedList(new_node)
    assert new_llist.length == 1
