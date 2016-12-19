"""Implementation of Queue."""

from dll import DoublyLinkedList


class Deque(object):
    """Class implementation of queue.

    append(val): adds value to the end of the deque.
    appendleft(val): adds a value to the front of the deque.
    pop(): removes a value from the end of the deque and returns it
            (raises an exception if the deque is empty)
    popleft(): removes a value from the front of the deque and returns it
            (raises an exception if the deque is empty)
    peek(): returns the next value that would be returned by pop but
            leaves the value in the deque (returns None if the deque is empty)
    peekleft(): returns the next value that would be returned by popleft
            but leaves the value in the deque (returns None if the deque
            is empty)
    size(): returns the count of items in the queue (returns 0 if the
            queue is empty)

    """

    def __init__(self, iterable=None):
        """Instatiate Queue."""
        self.dll = DoublyLinkedList(iterable)
        self.head_node = self.dll.head_node
        self.tail_node = self.dll.tail_node
        self.length = self.dll.length

    def append(self, contents):
        """Add value to the end of the deque."""
        self.dll.append(contents)
        self.head_node = self.dll.head_node
        self.tail_node = self.dll.tail_node
        self.length = self.dll.length

    def appendleft(self, contents):
        """Add value to the front of the deque."""
        self.dll.push(contents)
        self.head_node = self.dll.head_node
        self.tail_node = self.dll.tail_node
        self.length = self.dll.length

    def pop(self):
        """Remove and return the current tail node."""
        return self.dll.shift()
        self.head_node = self.dll.head_node
        self.tail_node = self.dll.tail_node
        self.length = self.dll.length

    def popleft(self):
        """Remove and return the current head node."""
        return self.dll.pop()
        self.head_node = self.dll.head_node
        self.tail_node = self.dll.tail_node
        self.length = self.dll.length

    def peek(self):
        """Display but don't remove the contents of tail node."""
        return self.dll.tail_node.contents

    def peekleft(self):
        """Display but don't remove the contents of head node."""
        return self.dll.head_node.contents

    def size(self):
        """Return the count of items in the queue."""
        return self.length

