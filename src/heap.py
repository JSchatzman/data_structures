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
            self.data.append(val)


    def sort(self):
        """Organize the binary heap according to the heaps rules."""
        index_child = -1
        index_parent = (len(self.data) - 2) // 2
        while self.data[index_child] < self.data[index_parent]:
            self.data[index_child], self.data[index_parent] = self.data[index_parent], self.data[index_child]
            index_child, index_parent = index_parent, (index_parent - 1) // 2
            if self.data[index_child] == self.data[0]:
                break

    def push(self, val):
        """Push add new value to list."""
        self.data.append(val)
        if len(self.data) > 1:
            self.sort()

    def pop(self):
        """Pop it."""
        if not len(self.data):
            raise IndexError('Cannot pop a empty heap!')
        val = self.data.pop(0)
        if len(self.data) > 1:
            self.sort()
        return val
