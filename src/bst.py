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
            for val in contents[1:]:
                self.insert(val)

    def insert(self, val):
        """Insert a new node into the bst."""
        self.all_values.setdefault(val)
        check = self.root
        while check:
            if val < check.contents:
                #print('hello1')
                if check.left_child:
                    check = check.left_child
                    continue
                check.left_child = Node(val)
                self._size += 1
                return
            elif val > check.contents:
                #print('hello2')
                if check.right_child:
                    check = check.right_child
                    continue
                check.right_child = Node(val)
                self._size += 1
                return
            else:
                return

    def size(self):
        """Return the length of the bst."""
        return self._size

    # def depth(self, root, depth=0, base_root=None):
    #     # if not base_root:
    #     #     root
    #     if root is None:
    #         return depth
    #     return max(self.depth(root.left, depth + 1),
    #                self.depth(root.right, depth + 1))

    def depth(self, root_check=None, depth_list=None):
        """Find all depths of this bs
        t."""
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

#bst = BinarySearchTree([40, 20, 50, 30, 15, 70, 75])
bst = BinarySearchTree([40, 20, 50, 30, 5, 4])

#bst = BinarySearchTree([40])


print(bst.depth())


