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
    assert new_llist.head_node == new_node


def test_linkedlist_push():
    """Test for LinkedList push."""
    from linked_list import Node, LinkedList
    new_node = Node(34, None)
    new_llist = LinkedList(new_node)
    new_llist.push(1)
    assert new_llist.length == 2
    assert new_llist.head_node.contents == 1


def test_linkedlist_pop():
    """Test for LinkedList pop."""
    from linked_list import Node, LinkedList
    new_node = Node(34, None)
    new_llist = LinkedList(new_node)
    new_llist.push(1)
    new_llist.pop()
    assert new_llist.head_node.contents == 34
    assert new_llist.length == 1


def test_linkedlist_size():
    """Test for LinkedList size."""
    from linked_list import Node, LinkedList
    new_node = Node(34, None)
    new_llist = LinkedList(new_node)
    new_llist.push(1)
    new_llist.pop()
    new_llist.push('test1')
    new_llist.push('test2')
    new_llist.push('test3')
    new_llist.push('test4')
    assert new_llist.size() == 5


def test_linkedlist_search():
    """Test for LinkedList search."""
    from linked_list import Node, LinkedList
    new_node = Node(34, None)
    new_llist = LinkedList(new_node)
    new_llist.push(1)
    new_llist.pop()
    new_llist.push('test1')
    new_llist.push('test2')
    new_llist.push('test3')
    new_llist.push('test4')
    assert new_llist.search('test4').contents == 'test4'
    assert new_llist.search('test2').contents == 'test2'
    assert new_llist.search('test100') is None


def test_linkedlist_remove():
    """Test for LinkedList remove."""
    from linked_list import Node, LinkedList
    new_node = Node('Test5', None)
    new_llist = LinkedList(new_node)
    new_llist.push('test4')
    new_llist.push('test3')
    new_llist.push('test2')
    new_llist.push('test1')
    new_llist.remove(new_llist.search('test2'))
    assert new_llist.size() == 4
    assert new_llist.search('test1').next_node.contents == 'test3'
    new_node2 = Node('Test5', None)
    new_llist2 = LinkedList(new_node2)
    new_llist2.push('test4')
    new_llist2.push('test3')
    new_llist2.push('test2')
    new_llist2.push('test1')
    new_llist2.remove(new_llist2.search('test1'))
    assert new_llist2.head_node.contents == 'test2'
    try:
        new_llist.remove(new_llist.search('blah'))
    except ValueError:
        assert True


def test_linkedlist_display():
    """Test for LinkedList remove."""
    from linked_list import Node, LinkedList
    new_node = Node('test5', None)
    new_llist = LinkedList(new_node)
    new_llist.push('test4')
    new_llist.push('test3')
    new_llist.push('test2')
    new_llist.push('test1')
    new_llist2 = LinkedList(new_node)
    assert new_llist.display() == ('test1', 'test2', 'test3', 'test4', 'test5')
    assert new_llist2.display() == ('test5',)
