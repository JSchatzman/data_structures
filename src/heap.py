"""Implementation of heap."""


class Heap(object):
    """Create heap class.

    push(): puts a new value into the heap,
    pop(): removes the top value in the heap,
    """

    def __init__(self, val=None):
        """Instantiate a heap."""
        self.data = []
        if val:
            for item in val:
                self.push(val)
    # def find_parent_index(self, index):
    #     """Find parent index of given index."""
    #     if index == 0:
    #         return None
    #     if index % 2 == 0:
    #         return index // 2 - 1
    #     else:
    #         return index // 2

    # def swap_nodes(self, index, parent_index):
    #     """Swap parent and child nodes if greater."""
    #     parent_index = self.find_parent_index(index)
    #     old_parent = self.data[parent_index]
    #     self.data[parent_index] = self.data[index]
    #     self.data[index] = old_parent
    #     return parent_index

    # def push(self, contents):
    #     """Add value to the end of the data."""
    #     if len(self.data) < 1:
    #         return self.data.append(contents)
    #     self.data.append(contents)
    #     index = len(self.data) - 1
    #     parent_index = self.find_parent_index(index)
    #     while (self.data[index] < self.data[parent_index]) and ((index // 2) > 0):
    #         index = self.swap_nodes(index, parent_index)
    #         parent_index = self.find_parent_index(index)
    #     if index in (1, 2) and self.data[index] < self.data[0]:
    #         self.swap_nodes(index, 0)

    # def pop(self):
    #     """Remove head of the heap."""
    #     if len(self.data) == 0:
    #         raise IndexError('Cannot pop a empty heap!')
    #     val = self.data[0]
    #     self.data[0] = self.data[len(self.data) - 1]
    #     self.data.pop()
    #     index = 0
    #     while (index * 2 + 1) < len(self.data):
    #         min_child = self.find_min_child(index)
    #         if self.data[index] > self.data[min_child]:
    #             old_parent = self.data[index]
    #             self.data[index] = self.data[min_child]
    #             self.data[min_child] = old_parent
    #         index = min_child
    #     return val

    # def find_min_child(self, index):
    #     """Find minimum child."""
    #     if index * 2 + 1 > len(self.data):
    #         return index * 2
    #     else:
    #         if self.data[index * 2 + 1] < self.data[index * 2 + 2]:
    #             return index * 2 + 1
    #         else:
    #             return index * 2 + 2

    def sort_heap_up(self):
        """Organize the binary heap according to the heaps rules.

        Min heap: Parent nodes must be less than child nodes.
        Notes:  Last index number is (container length -1).
                Parent index is (container length - 2) / 2 floored.
        """
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
            self.sort_heap_up()

    # def pop(self):
    #     """Remove value from list."""
    #     if not len(self.data):
    #         raise IndexError('Cannot pop a empty heap!')
    #     return_val = self.data[0]
    #     self.data[0], self.data[-1] = self.data[-1], self.data[0]
    #     self.data.pop()
    #     if len(self.data) > 1:
    #         self.sort_heap_down()
    #     return return_val

    def pop(self):
        """Pop it."""
        if not len(self.data):
            raise IndexError('Cannot pop a empty heap!')
        self.data.pop(0)
        if len(self.data) > 1:
            self.sort_heap_up()

    # def sort_heap_down(self):
    #     """Sort down from top."""
    #     index_parent = 0
    #     index_child = index_parent * 2 + 1
    #     try:
    #         while self.data[index_child] < self.data[index_parent]:
    #             self.data[index_parent], self.data[index_child] = self.data[index_child], self.data[index_parent]
    #             index_parent, index_child = index_child, index_parent * 2 + 2
    #             if self.data[index_child] == self.data[-1]:
    #                 break
    #     except IndexError:
    #         pass
