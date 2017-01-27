"""Implementation of trie."""

from collections import OrderedDict

class Trie(object):
    """Class representation of trie.

    insert(string): Insert a new word into the trie.
    contains(self, string): Return true if the string is in trie else false.
    size(self): Return the size of the trie.
    remove(self, string): Remove the string from the tree if it exists.
    """

    def __init__(self):
        self.root = OrderedDict()
        self._size = 0

    def insert(self, string):
        """Insert a new word into the trie."""
        if not isinstance(string, str):
            raise TypeError("Value input must be a string")
        if self.contains(string):
            return
        check = self.root
        for letter in string:
            if letter not in check:
                check.setdefault(letter, OrderedDict())
            check = check[letter]
        check['$'] = 'END'
        self._size += 1

    def contains(self, string):
        """Return true if the string is in trie else false."""
        check = self.root
        for letter in string:
            if letter not in check:
                return False
            check = check[letter]
        return "$" in check.keys()

    @property
    def size(self):
        """Return the size of the trie."""
        return self._size

    def remove(self, string):
        """Remove the string from the tree if it exists."""
        if not self.contains(string):
            raise ValueError('The trie does not contain this string.')
        check = self.root
        list_deleted = []
        prev = None
        for letter in string:
            check = check[letter]
            if prev and len(prev.keys()) > 1:
                list_deleted.insert(0, letter)
            prev = check
        del check['$']
        if len(check.keys()) > 0:
            self._size -= 1
            return
        check = self.root
        prev = self.root
        for letter in string:
            if len(check[letter].keys()) > 1:
                prev = check[letter]
            check = check[letter]
        if len(list_deleted) > 0:
            del prev[list_deleted[0]]
        else:
            del self.root[string[0]]
        self._size -= 1

    def _traversal_start(self, start=None):
        """Return the node in trie corresponding to the input string if exists."""
        if start:
            try:
                check = self.root
                for letter in start:
                    check = check[letter]
            except KeyError:
                raise KeyError('The input string is not in the trie.')
            return check
        return self.root

    def traversal(self, start=None):
        """Perform a depth traversal of the string."""
        check = self._traversal_start(start)
        if isinstance(check, OrderedDict):
            for letter in check.keys():
                if letter != "$":
                    yield letter
                if start:
                    newstart = start + letter
                else:
                    newstart = letter
                for item in self.traversal(newstart):
                    if item != "$":
                        yield item
