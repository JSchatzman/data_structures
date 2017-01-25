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

    def insert(self, word):
        """Insert a new word into the trie."""
        check = self.root
        for letter in word:
            if letter not in check:
                check.setdefault(letter, {})
            check = check[letter]

        check['$'] = 'END'






test = Trie()
test.insert('kill')
