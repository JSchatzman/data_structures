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
        if '$' in check.keys():
            return True
        return False

    def size(self):
        """Return the size of the trie."""
        return self.size

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
        # import pdb; pdb.set_trace()
        if len(check.keys()) > 1:
            return
        list_deleted.insert(0, key)
        check = self.root
        prev = None
        for letter in string:
            if len(check[letter].keys()) > 1:
                prev = check[letter]
            check = check[letter]
        del prev[list_deleted[0]]

from trie import Trie
t = Trie()
t.insert("ted")
t.insert("tea")
t.insert("teabag")
t.insert("teabags")
t.insert("teabagger")
t.insert("teabaggers")
t.insert("teabagged")