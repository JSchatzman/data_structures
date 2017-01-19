"""Testing module for Binary Search Tree."""
import pytest

BST_INSERT_TABLE = [
    (40, 20),
    [40, 20, 50],
    [40, 20, 50, 30],
    (40, 20, 50, 30, 15),
    (40, 20, 50, 30, 15, 60),
    [1]
]

BST_BALANCE_TABLE = [
    ([40, 20], 1),
    [(40, 20, 50), 0],
    [[40, 20, 50, 30], 1],
    [(40, 20, 50, 30, 15), 1],
    [(40, 20, 50, 30, 15, 60), 0],
    ([1, 2, 3, 4, 5, 6], 5)
]


@pytest.fixture
def newnode():
    from bst import Node
    return Node(4, 2, 8)

@pytest.fixture
def bst_empty():
    from bst import BinarySearchTree
    return BinarySearchTree()

@pytest.fixture
def bst_filled():
    from bst import BinarySearchTree
    return BinarySearchTree(BST_INSERT_TABLE[4])

@pytest.fixture
def bst_single():
    from bst import BinarySearchTree
    return BinarySearchTree(BST_INSERT_TABLE[5])

def test_node_makes_stuff(newnode):
    assert newnode.contents == 4


def test_node_has_left_child(newnode):
    assert newnode.left_child == 2


def test_node_has_right_child(newnode):
    assert newnode.right_child == 8


def test_empty_bst_exists(bst_empty):
    """A new BST should have an empty root."""
    assert bst_empty.root is None


def test_filled_bst_has_correct_route(bst_filled):
    """Filled BST should have correct root."""
    assert bst_filled.root.contents == BST_INSERT_TABLE[4][0]


@pytest.mark.parametrize("vals", BST_INSERT_TABLE)
def test_insert_on_empty_bst(vals, bst_empty):
    """Inserting should increase BST size."""
    for val in vals:
        bst_empty.insert(val)
    assert bst_empty.size() == len(vals)


def test_init_with_vals_on_bst(bst_filled):
    """Initializing with values should increase size."""
    assert bst_filled.size() == len(BST_INSERT_TABLE[4])


def test_insert_on_filled_table(bst_filled):

    """Inserting should increment the size.
    This also tests that the size function works."""
    bst_filled.insert(29)
    assert bst_filled.size() == len(BST_INSERT_TABLE[4]) + 1


def test_depth_on_empty_bst(bst_empty):
    """Test that depth on empty bst returns 0."""
    assert bst_empty.depth() == 0


def test_depth_on_single_bst(bst_single):
    """Test that depth on single bst returns 1."""
    assert bst_single.depth() == 1


def test_depth_on_filled_bst(bst_filled):
    """Test that depth on filled bst returns 0."""
    assert bst_filled.depth() == 3


def test_balance_on_empty_tree(bst_empty):
    """Should return 0 for an empty tree."""
    assert bst_empty.balance() == 0


@pytest.mark.parametrize("vals, result", BST_BALANCE_TABLE)
def test_balance_on_filled_tree(vals, result, bst_empty):
    """Should return result for Table in tree."""
    for val in vals:
        bst_empty.insert(val)
    assert bst_empty.balance() == result


def test_balance_on_single_tree(bst_single):
    """Should return 1 for a tree with just a root."""
    assert bst_single.balance() == 1


def test_contains_method_on_empty(bst_empty):
    """Should return false for any value."""
    assert bst_empty.contains("asdfsaf") is False


def test_contains_method_on_filled(bst_filled):
    """Check that values are in the filled bst."""
    assert bst_filled.contains(15) is True


def test_search_method_on_empty_bst(bst_empty):
    """Should return none on empty bst."""
    assert bst_empty.search(0) is None


def test_search_method_on_filled_bst(bst_filled):
    """Should return a Node when found."""
    from bst import Node
    assert isinstance(bst_filled.search(15), Node)


def test_search_method_on_filled_bst_where_val_not_there(bst_filled):
    """Should return none on because Node not found."""
    assert bst_filled.search(0) is None