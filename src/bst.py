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
        if contents:
            self.root = Node(contents[0])
            for val in contents[1:]:
                self.insert(Node(val))

    def insert(self, val):
        """Insert a new node into the bst."""
        self.all_values.setdefault(val)
        check = self.root
        while check:
            if val < check.contents:
                print('hello1')
                if check.left_child:
                    check = check.left_child
                    continue
                check.left_child = Node(val)
                return
            elif val > check.contents:
                print('hello2')
                if check.right_child:
                    check = check.right_child
                check.right_child = Node(val)
                return


bst = BinarySearchTree([40])
bst.insert(20)
bst.insert(50)
bst.insert(30)



