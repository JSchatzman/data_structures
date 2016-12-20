"""Implementation of heap."""


class Heap(object):
    """Create heap class."""

    def __init__(self, iterable=None):
        """Instantiate a heap."""
        self.data = [5, 9, 11, 14, 18,
                     19, 21, 33, 17, 27]

    def find_parent_index(self, index):
        """Find parent index of given index."""
        if index == 0:
            return None
        if index % 2 == 0:
            return index // 2 - 1
        else:
            return index // 2

    def swap_nodes(self, index, parent_index):
        """Swap parent and child nodes if greater."""
        parent_index = self.find_parent_index(index)
        old_parent = self.data[parent_index]
        self.data[parent_index] = self.data[index]
        self.data[index] = old_parent
        return parent_index

    def push(self, contents):
        """Add value to the end of the data."""
        self.data.append(contents)
        index = len(self.data) - 1
        parent_index = self.find_parent_index(index)
        while self.data[index] < self.data[parent_index]:
            index = self.swap_nodes(index, parent_index)
            parent_index = self.find_parent_index(index)
