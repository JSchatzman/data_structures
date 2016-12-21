"""Implement the priorityq data structure in python."""


class Priorityq(object):
    """Initialize priorityq data structure.

    Priorityq has the following methods:
    insert(item): inserts an item into the queue.
    pop(): removes the most important item from the queue.
    peek(): returns the most important item without removing it from the queue.
    """

    def __init__(self, val=None):
        """Initialize the priorityq."""
        self.data = []
        self.length = 0
        for i in val:
            self.data.insert(i)

    def insert(self, val, priority=None):
        """Insert and item into the queue."""
        self.data.append((priority, val))
        self.length += 1

    def _sort(self):
        """Helper function to sort queue based on priority."""
        self.data = sorted(self.data, key=lambda index: index[0])
