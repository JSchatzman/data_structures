"""Implementation of Stack data type."""


class Stack(object):
    """Class representation of a stack."""

    def __init__(self, iterable=None):
        """Instantiate stack."""
        self.head_node = None
        self.length = 0
        if iterable:
            for item in iterable:
                self.push(item)

    def push(self, contents):
        """Add node to this stack."""
        if self.head_node:
            self.head_node = Node(contents, self.head_node)
        else:
            self.head_node = Node(contents, None)
        self.length += 1


    def pop(self):
        """Remove and return the current head node."""
        if not self.head_node:
            raise NameError('Stack is empty, cannot pop!')
        old_head_node = self.head_node
        self.head_node = self.head_node.next_node
        self.length -= 1
        return old_head_node


class Node(object):
    """Class representation of linked list node."""

    def __init__(self, contents, next_node):
        """Instantiate linked list node."""
        self.contents = contents
        self.next_node = next_node
