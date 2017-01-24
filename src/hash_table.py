"""The Hash Table module."""


class HashTable(object):
    """Implementation of a hash table."""

    def __init__(self, size, hash_type='naive'):
        """Initializes the hash table based on Key Word arg."""
        if hash_type not in ('bern', 'naive'):
            raise NameError("Hash type must be 'naive' or 'bern'.")
        self.hash_type = hash_type
        self.size = size
        self.hash_table = [[] for i in range(size)]

    def get(self, key):
        """Return the value stored with the given key."""
        hash_key = self.fun_chooser(key) % self.size
        value = self.hash_table[hash_key]
        for val, a_key in value:
            if a_key == key:
                return val

    def set(self, key, val):
        """Store the given val using the given key."""
        if type(key) is not str:
            raise TypeError("Hashes need to be in string format.")
        hash_key = self.fun_chooser(key) % self.size
        self.hash_table[hash_key].append((val, key))

    def _naive(self, key):
        """Hash the key provided naively."""
        hash_key = 0
        for letter in key:
            hash_key += ord(letter)
        return hash_key

    def _bernstein(self, string):
        """Hash the key using bernstein's method."""
        h = 3313  # arbitrary prime number
        for char in string:
            h = ((h << 5) + h) + ord(char)
        return int(int(h) % int(self.size))

    def fun_chooser(self, key):
        """Control which hash method to use."""
        if self.hash_type == 'naive':
            return self._naive(key)
        else:
            return self._bernstein(key)
