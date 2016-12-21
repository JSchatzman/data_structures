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
        if val:
            for i in val:
                self.insert(i[1], i[0])

    def insert(self, val, priority=0):
        """Insert and item into the queue."""
        self.data.append((priority, val))
        self.length += 1

    def _sort(self):
        """Helper function to sort queue based on priority."""
        self.data = sorted(self.data, key=lambda index: index[0])


q = Priorityq([(2, 3), (4, 5), (5, 'hey'), (2, 'hello'),
                        (2, 3), (2, 2), (2, 'jordan'), (10, 50), (0, -5), (5, 100)])

q._sort()
print (q.data)
