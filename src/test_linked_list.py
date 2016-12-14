"""Tests for linked_list.py."""


def test_node_init():
    """Test node class init."""
    from linked_list import Node
    new_node = Node(0, None)
    assert new_node.contents == 0 and new_node.next_node is None


def test_linkedlist_init():
    """Test for LinkedList init."""
    from linked_list import LinkedList
    new_llist = LinkedList()
    assert new_llist.length == 0
    assert new_llist.head_node is None


def test_linkedlist_push():
    """Test for LinkedList push."""
    from linked_list import LinkedList
    new_llist = LinkedList()
    new_llist.push("new")
    assert new_llist.length == 1
    assert new_llist.head_node.contents == "new"


def test_linkedlist_pop():
    """Test for LinkedList pop."""
    from linked_list import LinkedList
    new_llist = LinkedList()
    new_llist.push(34)
    new_llist.push(1)
    assert new_llist.pop().contents == 1
    assert new_llist.head_node.contents == 34
    assert new_llist.length == 1
    assert new_llist.pop().contents == 34
    assert new_llist.pop() is None


def test_linkedlist_size():
    """Test for LinkedList size."""
    from linked_list import LinkedList
    new_llist = LinkedList(('test1', 'test2', 'test3', 'test4'))
    assert new_llist.size() == 4


def test_linkedlist_search():
    """Test for LinkedList search."""
    from linked_list import LinkedList
    new_llist = LinkedList()
    new_llist.push('test1')
    new_llist.push('test2')
    new_llist.push('test3')
    new_llist.push('test4')
    assert new_llist.search('test4').contents == 'test4'
    assert new_llist.search('test2').contents == 'test2'
    assert new_llist.search('test100') is None


def test_linkedlist_remove():
    """Test for LinkedList remove."""
    from linked_list import LinkedList
    new_llist = LinkedList(('test1', 'test2', 'test3', 'test4'))
    new_llist.remove(new_llist.search('test2'))
    assert new_llist.size() == 3
    assert new_llist.search('test3').next_node.contents == 'test1'
    new_llist2 = LinkedList(('test1', 'test2', 'test3', 'test4'))
    new_llist2.remove(new_llist2.search('test4'))
    assert new_llist2.head_node.contents == 'test3'
    try:
        new_llist.remove(new_llist.search('blah'))
    except ValueError:
        assert True


def test_linkedlist_display():
    """Test for LinkedList remove."""
    from linked_list import LinkedList
    new_llist = LinkedList(('test1', 'test2', 'test3', 'test4'))
    new_llist2 = LinkedList(('test5',))
    assert new_llist.display() == ('test4', 'test3', 'test2', 'test1')
    assert new_llist2.display() == ('test5',)
