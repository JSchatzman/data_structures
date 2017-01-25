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
        self.size = 0

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
        self.size += 1

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





test = Trie()
test.insert('kill')
