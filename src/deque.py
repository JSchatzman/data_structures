"""Implementation of Queue."""

from dll import DoublyLinkedList


class Queue(object):
    """Class implementation of queue.

    1.  Enqueue: Add new head node.
    2.  Dequeue: Remove tail node.
    3.  Peek: Display tail node,
    4.  Size: Display queue length.

    """

    def __init__(self, iterable=None):
        """Instatiate Queue."""
        self.dll = DoublyLinkedList(iterable)
        self.head_node = self.dll.head_node
        self.tail_node = self.dll.tail_node

    def enqueue(self, contents):
        """Add new head node."""
        self.dll.push(contents)
        self.head_node = self.dll.head_node
        self.tail_node = self.dll.tail_node

    def dequeue(self):
        """Remove last node."""
        old_tail_node_contents = self.dll.shift()
        self.tail_node = self.dll.tail_node
        self.head_node = self.dll.head_node
        return old_tail_node_contents

    def peek(self):
        """Display but don't remove the contents of tail node."""
        return self.dll.tail_node.contents

    def size(self):
        """Return Queue length."""
        return self.dll.length

    def append(self, contents):
        self.dll.append(contents)
        