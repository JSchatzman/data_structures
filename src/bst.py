"""Implementation of Binary Search Tree."""


class Node(object):
    """Class representation of bst node.
    
    Methods:
    in_order(): In Order method for Node class. Return the values in order from smallest to largest.

    pre_order(): Pre_order method for Node class. Return a generator that will return the values in the tree using pre-order traversal, one at a time.

    post_order(): Post_order method for Node class. return a generator that will return the values in the tree using post-order traversal, one at a time.

    """

    def __init__(self, contents, left_child=None, right_child=None, parent=None):
        """Instantiate linked list node."""
        self.contents = contents
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def in_order(self):
        """In order method for Node object."""
        if self.left_child:
            for yieldval in self.left_child.in_order():
                yield yieldval
        yield self.contents
        if self.right_child:
            for yieldval in self.right_child.in_order():
                yield yieldval

    def pre_order(self):
        """Pre_order method for Node object."""
        yield self.contents
        if self.left_child:
            for yieldval in self.left_child.pre_order():
                yield yieldval
        if self.right_child:
            for yieldval in self.right_child.pre_order():
                yield yieldval

    def post_order(self):
        """Post_order method for Node object."""
        if self.left_child:
            for yieldval in self.left_child.post_order():
                yield yieldval
        if self.right_child:
            for yieldval in self.right_child.post_order():
                yield yieldval
        yield self.contents


class BinarySearchTree(object):
    """Class representation of bst.

    Methods:
    insert(val): Insert a new node into the bst.

    size(): Return the length of the bst.

    depth(): Find all maximum depth of this bst.

    contains(val): Will return True if val is in the BST, False if not.

    balance(): Will return an integer, positive or negative that represents how well balanced the tree is. Trees which are higher on the left than the right should return a positive value, trees which are higher on the right than the left should return a negative value. An ideally-balanced tree should return 0.

    search(val): Return Node containing the value.

    in_order(): In Order method for Binary Search Tree class. Return the values in order from smallest to largest.

    pre_order(): Pre_order method for Binary Search Tree class. Return a generator that will return the values in the tree using pre-order traversal, one at a time.

    post_order(): Post_order method for Binary Search Tree class. return a generator that will return the values in the tree using post-order traversal, one at a time.

    breadth_first(): Post_order method for Binary Search Tree class. return a generator that will return the values in the tree using post-order traversal, one at a time.


    """

    def __init__(self, contents=None):
        """Initialize bst with a node."""
        self.all_values = {}
        self.root = None
        self._size = 0
        if contents:
            for val in contents:
                self.insert(val)

    def insert(self, val):
        """Insert a new node into the bst."""
        if val not in self.all_values.keys():
            self._size += 1
        node = Node(val)
        if not self.root:
            self.root = node
        self.all_values.setdefault(val, node)
        check = self.root
        while check:
            if val < check.contents:
                if check.left_child:
                    check = check.left_child
                    continue
                check.left_child = node
                node.parent = check
                return
            elif val > check.contents:
                if check.right_child:
                    check = check.right_child
                    continue
                check.right_child = node
                node.parent = check
                return
            else:
                return

    def search(self, val):
        """Return Node containing the value."""
        try:
            return self.all_values[val]
        except KeyError:
            return None

    def size(self):
        """Return the length of the bst."""
        return self._size

    def depth(self, root_check=None):
        """Find all maximum depth of this bst."""
        if not self.root:
            return 0
        if not root_check:
            root_check = self.root
        if not root_check.left_child and not root_check.right_child:
            return 1
        elif root_check.left_child is None:
            return self.depth(root_check.right_child) + 1
        elif root_check.right_child is None:
            return self.depth(root_check.left_child) + 1
        return max(self.depth(root_check.left_child), self.depth(root_check.right_child)) + 1

    def contains(self, val):
        """Will return True if val is in the BST, False if not."""
        if val in self.all_values.keys():
            return True
        return False

    def balance(self, root_check=None): 
        """Will return an integer, positive or negative that represents how
        well balanced the tree is. Trees which are higher on the left than the
        right should return a positive value, trees which are higher on the
        right than the left should return a negative value. An
        ideally-balanced tree should return 0.
        """

        if not self.root:
            return 0
        if not root_check:
            root_check = self.root
        if not root_check.left_child and not root_check.right_child:
            return 1
        elif root_check.left_child is None:
            return self.depth(root_check.right_child)
        elif root_check.right_child is None:
            return self.depth(root_check.left_child)
        return self.depth(root_check.right_child) - self.depth(root_check.left_child)

    def in_order(self):
        """In Order method for Binary Search Tree class. Return the values in order from smallest to largest."""

        if self.root:
            for item in self.root.in_order():
                yield item

    def pre_order(self):
        """Pre_order method for Binary Search Tree class. Return a generator that will return the values in the tree using pre-order traversal, one at a time."""

        if self.root:
            for item in self.root.pre_order():
                yield item

    def post_order(self):
        """Post_order method for Binary Search Tree class. return a generator that will return the values in the tree using post-order traversal, one at a time."""
        if self.root:
            for item in self.root.post_order():
                yield item


    def breadth_first(self):
        """Post_order method for Binary Search Tree class. return a generator that will return the values in the tree using post-order traversal, one at a time."""
        if self.root:
            from queue_ import Queue
            q = Queue()
            q.enqueue(self.root)
            while q:
                try:
                    node = q.dequeue()
                    yield node.contents
                    if node.left_child:
                        q.enqueue(node.left_child)
                    if node.right_child:
                        q.enqueue(node.right_child)
                except(IndexError):
                    break
        return

    def delete_node(self, val):
        """Delete the node whose contents are the value given."""
        if self.root:
            if val not in self.all_values.keys():
                return
            value_node = self.search(val)
            if not value_node.left_child and not value_node.right_child:
                delete_the_node = self._barren_node_delete
            elif value_node.left_child and value_node.right_child:
                pass
                #call multichild node delete func
                # delete_the_node = self.multi_child_delete
            else:
                delete_the_node = self._single_child_delete
            self._size -= 1
            return delete_the_node(value_node)

    def _single_child_delete(self, node):
        """Delete a node that has a single child."""
        if node.parent:
            parent = node.parent
            if node.right_child:
                child = node.right_child
            else:
                child = node.left_child
            if parent.right_child == node:
                parent.right_child = child
            else:
                parent.left_child = child
            return
        if node.right_child:
            self.root = node.right_child
        if node.left_child:
            self.root = node.left_child
        self.root.parent = None
        return

    def _barren_node_delete(self, node):
        """Delete a node with no children."""
        if node.parent:
            parent = node.parent
            if parent.right_child and parent.right_child == node:
                parent.right_child = None
            if parent.left_child and parent.left_child == node:
                parent.left_child = None
            return
        self.root = None
        return


# if __name__ == '__main__':
#     import timeit
#     bst = BinarySearchTree((40, 20, 50, 30, 15, 60))
#     print('Depth Time for 1000 depth function calls:',
#           timeit.timeit(stmt="bst.depth()",
#                         setup='from __main__ import bst',
#                         number=1000))
#     print('Balance Time for 1000 balance function calls:',
#           timeit.timeit(stmt="bst.balance()",
#                         setup='from __main__ import bst',
#                         number=1000))
