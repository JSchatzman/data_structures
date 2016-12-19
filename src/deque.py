"""Implementation of Queue."""

from dll import DoublyLinkedList


class Deque(object):
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

    def append(self, contents):
        """Add value to the end of the deque."""
        self.dll.append(contents)

    def appendleft(self, contents):
        """Add value to the front of the deque."""
        self.dll.push(contents)

    def pop(self):
        """Remove and return the current tail node."""
        return self.dll.shift()

    def popleft(self):
        """Remove and return the current head node."""
        return self.dll.pop()

    def peek(self):
        """Display but don't remove the contents of tail node."""
        return self.dll.tail_node.contents

    def peekleft(self):
        pass
