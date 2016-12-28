"""Implementation of Linked_List data type."""


class LinkedList(object):
    """Class representation of linked list."""

    def __init__(self, iterable=None):
        """Instantiate linked list."""
        self.head_node = None
        self.length = 0
        try:
            for item in iterable:
                self.push(item)
        except TypeError:
            if iterable:
<<<<<<< HEAD
                return "Please only enter iterable values"
=======
                raise TypeError("Please only enter iterable values")
>>>>>>> dc108d412a8573f34ccce20cb471d8f2ed2f1fcd

    def push(self, contents):
        """Add node to this linked list."""
        self.head_node = Node(contents, self.head_node)
        self.length += 1

    def pop(self):
        """Remove and return the current head node."""
        if not self.head_node:
<<<<<<< HEAD
            return "Linked list is already empty"
=======
            raise IndexError("List is already empty")
>>>>>>> dc108d412a8573f34ccce20cb471d8f2ed2f1fcd
        old_head_node = self.head_node
        self.head_node = self.head_node.next_node
        self.length -= 1
        return old_head_node.contents

    def size(self):
        """Return the current size of this linked list."""
        return self.length

    def search(self, search_value):
        """Return the node with the searched contents if found."""
        if self.length:
            if search_value == self.head_node.contents:
                return self.head_node
            current_node = self.head_node
            while current_node.contents != search_value:
                if current_node.next_node is None:
                    return None
                current_node = current_node.next_node
            return current_node
        else:
            return None

    def remove(self, remove_value):
        """Remove a node from linked list."""
        last_node = None
        current_node = self.head_node
        while current_node:
            if current_node.contents == remove_value:
                if last_node:
                    last_node.next_node = current_node.next_node
                else:
                    self.head_node = current_node.next_node
                self.length -= 1
                return
            last_node = current_node
            current_node = current_node.next_node

    def display(self):
        """Return the tuple of all values in linked list."""
        if self.length == 0:
            return None
        else:
            new_list = [self.head_node.contents]
            current_node = self.head_node
            while current_node.next_node is not None:
                current_node = current_node.next_node
                new_list.append(current_node.contents)
<<<<<<< HEAD
            return tuple(new_list)
=======
            return str(tuple(new_list))
>>>>>>> dc108d412a8573f34ccce20cb471d8f2ed2f1fcd


class Node(object):
    """Class representation of linked list node."""

    def __init__(self, contents, next_node):
        """Instantiate linked list node."""
        self.contents = contents
        self.next_node = next_node
