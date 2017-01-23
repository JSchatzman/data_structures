"""The Hash Table module."""


class HashTable(object):
    """Implementation of a hash table."""

    def __init__(self, size, hash_type=None):
        """Initializes the hash table based on Key Word arg."""
        self.hash_type = hash_type
        self.size = size
        self.hash_table = [[] for i in range(size)]

    def get(self, key):
        """Return the value stored with the given key."""
        hash_key = self._hash(key) % self.size
        return self.hash_table[hash_key]

    def set(self, key, val):
        """Store the given val using the given key."""
        if type(key) is not str:
            raise TypeError("Hashes need to be in string format.")
        hash_key = self._hash(key) % self.size
        self.hash_table[hash_key].append(val)

    def _hash(self, key):
        """Hash the key provided."""
        hash_key = 0
        for letter in key:
            hash_key += ord(letter)
        return hash_key
