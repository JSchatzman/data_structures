"""Tests for dll.py."""


def test_node_init():
    """Test node class init."""
    from dll import Node
    new_node = Node(0, None, None)
    assert new_node.contents == 0
    assert new_node.next_node is None
    assert new_node.previous_node is None


def test_dll_init():
    """Test for LinkedList init."""
    from dll import DoublyLinkedList
    new_dll = DoublyLinkedList()
    assert new_dll.length == 0
    assert new_dll.head_node is None
    assert new_dll.tail_node is None


def test_linkedlist_push():
    """Test for LinkedList push."""
    from dll import DoublyLinkedList
    new_dll = DoublyLinkedList()
    new_dll.push("new")
    assert new_dll.length == 1
    assert new_dll.head_node.contents == "new"
    new_dll.push("second")
    assert new_dll.length == 2
    assert new_dll.head_node.contents == "second"


def test_linkedlist_append():
    """Test for LinkedList push."""
    from dll import DoublyLinkedList
    new_dll = DoublyLinkedList()
    new_dll.append("new")
    assert new_dll.length == 1
    assert new_dll.tail_node.contents == "new"
    new_dll.append("second")
    assert new_dll.length == 2
    assert new_dll.tail_node.contents == "second"


def test_linkedlist_pop():
    """Test for LinkedList pop."""
    from dll import DoublyLinkedList
    new_dll = DoublyLinkedList([1, 2, 3, 4, 5])
    assert new_dll.pop().contents == 5
