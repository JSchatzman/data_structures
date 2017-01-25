"""Implementation of trie."""

class Node(object):
    """Individual node of tree."""

    def __init__(self, value=None):
        self.value = value
        self.pointers = ()

class Trie(object):
    """Class representation of trie."""

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """Insert a new word into the trie."""
        for letter in word:
            if letter not in self.root.pointers:
                pass
                #add logic here