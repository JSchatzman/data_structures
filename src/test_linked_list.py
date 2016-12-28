"""Tests for linked_list.py."""

import pytest


@pytest.fixture
def sample_linked_list():
    """Create testing linked list."""
    from linked_list import LinkedList
    one_llist = LinkedList([1])
    empty_llist = LinkedList()
    new_llist = LinkedList([1, 2, 3, 4, 5])
    return (empty_llist, one_llist, new_llist)


def test_node_init():
    """Test node class init."""
    from linked_list import Node
    new_node = Node(0, None)
    assert new_node.contents == 0 and new_node.next_node is None


def test_linkedlist_init_empty_size(sample_linked_list):
    """Test for empty LinkedList init."""
    assert sample_linked_list[0].length == 0


def test_linkedlist_init_empty_head(sample_linked_list):
    """Test head in empty LinkedList init."""
    assert sample_linked_list[0].head_node is None


def test_linkedlist_init_one_size(sample_linked_list):
    """Test for LinkedList init single item."""
    assert sample_linked_list[1].length == 1


def test_linkedlist_init_one_head(sample_linked_list):
    """Test head in LinkedList init single item."""
    assert sample_linked_list[1].head_node.contents == 1


def test_linkedlist_init_list_size(sample_linked_list):
    """Test for LinkedList init with list."""
    assert sample_linked_list[2].length == 5


def test_linkedlist_init_list_head(sample_linked_list):
    """Test head in LinkedList init with list."""
    assert sample_linked_list[2].head_node.contents == 5


def test_linkedlist_push_size(sample_linked_list):
    """Test for LinkedList size after push."""
    test_linkedlist = sample_linked_list[2]
    test_linkedlist.push("new")
    assert test_linkedlist.length == 6


def test_linkedlist_push_val(sample_linked_list):
    """Test for LinkedList head value after push."""
    test_linkedlist = sample_linked_list[2]
    test_linkedlist.push("new")
    assert test_linkedlist.head_node.contents == 'new'


def test_linkedlist_pop_empty(sample_linked_list):
    """Test for Linked List pop on empty."""
    with pytest.raises(IndexError):
        sample_linked_list[0].pop()


def test_linkedlist_pop_one(sample_linked_list):
    """Test for Linked List pop on list with one item."""
    assert sample_linked_list[1].pop() == 1


def test_linkedlist_pop_list(sample_linked_list):
    """Test for Linked List pop on multi-item list."""
    assert sample_linked_list[2].pop() == 5


def test_linkedlist_search_list(sample_linked_list):
    """Test for LinkedList search list."""
    assert sample_linked_list[2].search(2).contents == 2


def test_linkedlist_search_empty(sample_linked_list):
    """Test for LinkedList search empty list."""
    assert sample_linked_list[1].search(2) is None


def test_linkedlist_search_list_false(sample_linked_list):
    """Test for LinkedList search list when search value is not in list."""
    assert sample_linked_list[2].search(100) is None


def test_linkedlist_remove(sample_linked_list):
    """Test that removed value is gone after remove()."""
    sample_linked_list[2].remove(3)
    assert sample_linked_list[2].search(3) is None


def test_linkedlist_remove_pointers(sample_linked_list):
    """Test that previous node points to correct node after remove()."""
    sample_linked_list[2].remove(3)
    assert sample_linked_list[2].search(4).next_node.contents == 2


def test_linkedlist_remove_head(sample_linked_list):
    """Test LinkedList remove() the head on a list."""
    sample_linked_list[2].remove(5)
    assert sample_linked_list[2].head_node.contents == 4


def test_linkedlist_remove_empty(sample_linked_list):
    """Test LinkedList remove() on an empty linked list."""
    sample_linked_list[1].remove(5) is None


def test_linkedlist_display(sample_linked_list):
    """Test for LinkedList display."""
    assert sample_linked_list[2].display() == '(5, 4, 3, 2, 1)'


def test_linkedlist_display_one(sample_linked_list):
    """Test for LinkedList display on single item list."""
    assert sample_linked_list[1].display() == '(1,)'


def test_linkedlist_display_empty(sample_linked_list):
    """Test for LinkedList display on empty list."""
    assert sample_linked_list[0].display() is None
