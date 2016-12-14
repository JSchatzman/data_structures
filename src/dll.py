"""Implementation of Doubly Linked List data type."""


class DoublyLinkedList(object):
    """Class representation of doubly linked list."""

    def __init__(self, iterable=None):
        """Instantiate linked list."""
        self.head_node = None
        self.tail_node = None
        self.length = 0
        try:
            for item in iterable:
                self.push(item)
        except TypeError:
            if iterable:
                print("Please only enter iterable values")

    def push(self, contents):
        """Add node to this dll."""
        if self.length == 0:
            self.head_node = Node(contents, None, None)
            self.tail_node = self.head_node
        else:
            self.head_node = Node(contents, self.head_node, None)
        self.length += 1

    def append(self, contents):
        """Add node to this dll."""
        if self.length == 0:
            self.tail_node = Node(contents, None, None)
            self.head_node = self.tail_node
        else:
            self.tail_node = Node(contents, None, self.tail_node)
        self.length += 1

    def pop(self):
        """Remove and return the current head node."""
        if not self.head_node:
            print("Linked list is already empty")
            return
        old_head_node = self.head_node
        self.head_node = self.head_node.next_node
        self.length -= 1
        return old_head_node

class Node(object):
    """Class representation of doubly linked list node."""

    def __init__(self, contents, next_node, previous_node):
        """Instantiate doubly linked list node."""
        self.contents = contents
        self.next_node = next_node
        self.previous_node = previous_node
