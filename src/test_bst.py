"""Testing module for Binary Search Tree."""
import pytest

BST_INSERT_TABLE = [
    (40, 20),
    [40, 20, 50],
    [40, 20, 50, 30],
    (40, 20, 50, 30, 15),
    (40, 20, 50, 30, 15, 60),
]


@pytest.fixture
def newNode():
    from bst import Node
    return Node(4, 2, 8)

@pytest.fixture
def BST_empty():
    from bst import BinarySearchTree
    return BinarySearchTree()

@pytest.fixture
def BST_Filled():
    from bst import BinarySearchTree
    return BinarySearchTree(BST_INSERT_TABLE[4])

def test_node_makes_stuff(newNode):
    assert newNode.contents == 4


def test_node_has_left_child(newNode):
    assert newNode.left_child == 2


def test_node_has_right_child(newNode):
    assert newNode.right_child == 8


def test_empty_BST_exists(BST_empty):
    """A new BST should have an empty root."""
    assert BST_empty.root is None


def test_filled_BST_has correct_route(BST_Filled):
    """Filled BST should have correct root."""
    assert BST_Filled.root == BST_INSERT_TABLE[0]


@pytest.mark.parametrize("vals", BST_INSERT_TABLE)
def test_insert_on_empty_BST(vals, BST_empty):
    """Inserting should increase BST size."""
    for val in vals:
        BST_empty.insert(val)
    assert BST_empty.size() == len(vals)


def test_init_with_vals_on_BST(BST_Filled):
    """Initializing with values should increase size."""
    assert BST_Filled.size() == len(BST_INSERT_TABLE[4])


def test_insert_on_filled_table(BST_Filled):
    """Inserting should increment the size.
    This also tests that the size function works."""
    BST_Filled.insert(29)
    assert BST_Filled.size() == len(BST_INSERT_TABLE[-1]) + 1


