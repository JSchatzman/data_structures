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
        self.data = {}
        self.length = 0
        if val:
            for i in val:
                self.insert(i[1], i[0])

    def insert(self, value, priority=0):
        """Insert new value into priorityq."""
        if priority in self.data:
            self.data[priority].append(value)
        self.data[priority] = [value]

    def peek(self):
        """Return but don't remove the highest priority value."""
        min_priority = min(self.data.keys())
        return self.data[min_priority][-1]

    def pop(self):
        """Return and remove the highest priority value."""
        min_priority = min(self.data.keys())
        return self.data[min_priority].pop()
