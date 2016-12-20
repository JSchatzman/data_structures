"""Implementation of heap."""


class Heap(object):
    """Create heap class."""

    def __init(self, iterable=None):
        """Instantiate a heap."""
        self.heap = [5, 9, 11, 14, 18,
                     19, 21, 33, 17, 27, 2]

    def find_parent_index(self, index):
        """Find parent index of given index."""
        if index == 0:
            return None
        if index % 2 == 0:
            return index // 2 - 1
        else:
            return index // 2

    def swap_nodes(self, index):
        """Swap parent and child nodes if greater."""
        parent_index = self.find_parent_index(index)
        if self.heap[index] < self.heap[parent_index]:
            old_parent = self.heap[parent_index]
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = old_parent


