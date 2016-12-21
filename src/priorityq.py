"""Implement the priorityq data structure in python."""


class Priorityq(object):
    """Initialise priorityq data structure.

    Priorityq has the following methods:
    insert(item): inserts an item into the queue.
    pop(): removes the most important item from the queue.
    peek(): returns the most important item without removing it from the queue.
    """

    def __init__(self, val=None, priority=None):
        """Initialize the priorityq."""
        self.data = [(priority, val)]
        self.length = 0

    def insert(self, val, priority=None):
        """Insert and item into the queue."""
        self.data.append((priority, val))
