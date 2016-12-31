"""Implementation of heap."""


class Heap(object):
    """Create heap class.

    push(): puts a new value into the heap,
    pop(): removes the top value in the heap,
    """

    def __init__(self, val=''):
        """Instantiate a heap."""
        self.data = []
        try:
            for item in val:
                self.push(item)
        except TypeError:
            if type(val) == bool or val == Exception:
                raise TypeError('Incorrect datatype for Heap object.')
            self.data.append(val)

    def push(self, val):
        """Add value to the end of the data."""
        self.data.append(val)
        self._swap_nodes_up(len(self.data) - 1)

    def pop(self):
        """Remove head of the heap."""
        if len(self.data) == 0:
            raise IndexError('Cannot pop a empty heap!')
        val = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self._swap_nodes_down(0)
        return val

    def _swap_nodes_up(self, idx):
        """Swap parent and child nodes if greater."""
        if idx == 0:
            return 0
        parent_index = (idx - 1) // 2
        if self.data[idx] < self.data[parent_index]:
            self.data[idx], self.data[parent_index] = self.data[parent_index], self.data[idx]
            self._swap_nodes_up(parent_index)

    def _swap_nodes_down(self, idx):
        """Swap nodes up until meets minheap."""
        child1 = (2 * idx) + 1
        if child1 >= len(self.data):
            return 0
        child2 = child1 + 1
        try:
            lowest_child = child1 if self.data[child1] < self.data[child2] else child2
        except IndexError:
            lowest_child = child1
        if self.data[idx] > self.data[lowest_child]:
            self.data[idx], self.data[lowest_child] = self.data[lowest_child], self.data[idx]
            self._swap_nodes_down(lowest_child)
