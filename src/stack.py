"""Implementation of Stack data type."""

from linked_list import LinkedList


class Stack(object):
    """Class representation of a stack."""

    def __init__(self, iterable=None):
        """Instantiate stack."""
        self.linked_list = LinkedList(iterable)
        self.length = self.linked_list.length
        self.head_node = self.linked_list.head_node

    def push(self, contents):
        """Add node to this stack."""
        self.linked_list.push(contents)
        self.head_node = self.linked_list.head_node

    def pop(self):
        """Remove and return the current head node."""
        old_head_node_value = self.linked_list.pop()
        self.head_node = self.linked_list.head_node
        return old_head_node_value

test = Stack([1,2,3])
print (test.pop())
print (test.pop())
print (test.pop())
print (test.pop())
