"""Implementation of Binary Search Tree."""


class Node(object):
    """Class representation of bst node."""

    def __init__(self, contents, left_child=None, right_child=None):
        """Instantiate linked list node."""
        self.contents = contents
        self.left_child = left_child
        self.right_child = right_child


class BinarySearchTree(object):
    """Class representation of bst."""

    def __init__(self, contents=None):
        """Initialize bst with a node."""
        self.all_values = {}
        self.root = None
        self._size = 0
        if contents:
            self.root = Node(contents[0])
            for val in contents:
                self.insert(val)

    def insert(self, val):
        """Insert a new node into the bst."""
        if val not in self.all_values.keys():
            self._size += 1
        self.all_values.setdefault(val)
        check = self.root
        while check:
            if val < check.contents:
                if check.left_child:
                    check = check.left_child
                    continue
                check.left_child = Node(val)
                return
            elif val > check.contents:
                if check.right_child:
                    check = check.right_child
                    continue
                check.right_child = Node(val)
                return
            else:
                return

    def size(self):
        """Return the length of the bst."""
        return self._size

    def depth(self, root_check=None, depth_list=None):
        """Find all depths of this bst."""
        if not self.root:
            return 0
        if not root_check:
            root_check = self.root
        if not depth_list:
            depth_list = []
        if not root_check.left_child and not root_check.right_child:
            return 1
        if root_check.left_child is None:
            return self.depth(root_check.right_child) + 1
        if root_check.right_child is None:
            return self.depth(root_check.left_child) + 1
        return max(self.depth(root_check.left_child), self.depth(root_check.right_child)) + 1

    def contains(self, val):
        """Will return True if val is in the BST, False if not."""
        if val in self.all_values.keys():
            return True
        return False

    def balance(self): 
        """Will return an integer, positive or negative that represents how
        well balanced the tree is. Trees which are higher on the left than the
        right should return a positive value, trees which are higher on the
        right than the left should return a negative value. An
        ideally-balanced tree should return 0.
        """
        balance = 0
        check = self.root
        while check:
            if check.left_child:
                balance -= 1
            if check.right_child:
                balance += 1
            if check.left_child:
                check = check.left_child
                continue
            check = check.right_child
        check = self.root
        while check:
            if check.left_child:
                balance -= 1
            if check.right_child:
                balance += 1
            if check.right_child:
                check = check.right_child
                continue
            check = check.left_child
        return balance
