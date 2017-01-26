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
        del_list = []
        check = self.root
        for letter in string:
            key_length = len([key for key in check.keys() if key != '$']) 
            # del_list.append((check, len(check.keys())))
            del_list.append((check, key_length))
            check = check[letter]

        del_list = del_list
        for val in range(len(del_list)):
            if del_list[val][1] > 1:
                break

        check2 = self.root
        for i in range(val):
            print(string[i])
            check2 = check2[string[i]]
        del check2[string[i + 1]]





        # check = self.root
        # # del_list = []
        # # #count = 0
        # for i, letter in enumerate(string):
        #     previous = check
        #     check = check[letter]
        #     if len(check.keys()) > 2:
        #         break
        # if (i + 1) == len(string):
        #     pass
        #     #del previous[string[i]['$']

        # import pdb; pdb.set_trace()
        # del check[string[i + 1]]
        
        






test = Trie()
test.insert('h')
test.insert('help')
test.insert('hey')
test.insert('helpp')
#test.insert('h')
import pdb; pdb.set_trace()
test.remove('hey')
import pdb; pdb.set_trace()
