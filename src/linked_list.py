"""Implementation of Linked_List data type."""


class LinkedList(object):
    """Class representation of linked list."""

    def __init__(self, head_node):
        """Instantiate linked list."""
        self.head_node = head_node
        self.length = 1

    def push(self, contents):
        """Add node to this linked list."""
        self.head_node = Node(contents, self.head_node)
        self.length += 1

    def pop(self):
        """Remove and return the current head node."""
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
