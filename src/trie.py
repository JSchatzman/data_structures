"""Implementation of trie."""

# class Node(object):
#     """Individual node of tree."""

#     def __init__(self, value=None):
#         self.value = value
#         self.pointers = ()

class Trie(object):
    """Class representation of trie."""

    def __init__(self):
        self.root = {}
        self._size = 0

    def insert(self, string):
        """Insert a new word into the trie."""
        if self.contains(string):
            return
        check = self.root
        for letter in string:
            if letter not in check:
                check.setdefault(letter, {})
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
        if '$' in check:
            return True
        return False

    def size(self):
        """Return the size of the trie."""
        return self._size

    def remove(self, string):
        """Remove the string from the tree if it exists."""
        if not self.contains(string):
            raise ValueError('The trie does not contain this string.')
        check = self.root
        for letter in string:
            check = check[letter]
        if check.keys().count > 1:
            del check['END']
            return
        for letter in string.reverse():
            del check[letter]
        return





test = Trie()
test.insert('kill')
