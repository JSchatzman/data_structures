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
    [[40, 20, 50, 30], -1],
    [(40, 20, 50, 30, 15), -1],
    [(40, 20, 50, 30, 15, 60), 0],
    ([1, 2, 3, 4, 5, 6], 5)
]

PRE_ORDER_TABLE = [
    ([40, 30, 75, 200, 76, 50], [40, 30, 75, 50, 200, 76]),
    ([80, 25, 76, 888, 95, 10, 11], [80, 25, 10, 11, 76, 888, 95]),
    ([50, 100, 12, 30, 58, 79, 51, 42], [50, 12, 30, 42, 100, 58, 51, 79])
]

POST_ORDER_TABLE = [
    ([40, 30, 75, 200, 76, 50], [30, 50, 76, 200, 75, 40]),
    ([80, 25, 76, 888, 95, 10, 11], [11, 10, 76, 25, 95, 888, 80]),
    ([50, 100, 12, 30, 58, 79, 51, 42], [42, 30, 12, 51, 79, 58, 100, 50])
]

IN_ORDER_TABLE = [
    ([40, 30, 75, 200, 76, 50], [30, 40, 50, 75, 76, 200]),
    ([80, 25, 76, 888, 95, 10, 11], [10, 11, 25, 76, 80, 95, 888]),
    ([50, 100, 12, 30, 58, 79, 51, 42], [12, 30, 42, 50, 51, 58, 79, 100])
]

BREADTH_ORDER_TABLE = [
    ([40, 30, 75, 200, 76, 50], [40, 30, 75, 50, 200, 76]),
    ([80, 25, 76, 888, 95, 10, 11], [80, 25, 888, 10, 76, 95, 11]),
    ([50, 100, 12, 30, 58, 79, 51, 42], [50, 12, 100, 30, 58, 42, 51, 79])
]

DELETE_SINGLE_VALUE_TABLE = [
    ([40, 30, 75, 200, 76, 50], 200),
    ([80, 25, 76, 888, 95, 10, 11], 888),
    ([80, 25, 76, 888, 95, 10, 11], 10),
    ([50, 100, 12, 30, 58, 79, 51, 42], 30),
    ([50, 100, 12, 30, 58, 79, 51, 42], 79),
    ([40, 50], 40),
    ([40, 10], 40)

]

DELETE_SINGLE_VALUE_TABLE2 = [
    ([80, 25, 76, 888, 95, 10, 11], [888, 10]),
    ([50, 100, 12, 30, 58, 79, 51, 42], [30, 79]),
]

DELETE_BARREN_VALUE_TABLE = [
    ([40, 30, 75, 200, 76, 50], 50),
    ([80, 25, 76, 888, 95, 10, 11], 76),
    ([80, 25, 76, 888, 95, 10, 11], 95),
    ([50, 100, 12, 30, 58, 79, 51, 42], 42),
    ([50, 100, 12, 30, 58, 79, 51, 42], 51),
    ([40, 50], 50),
    ([40, 10], 10)
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


def test_in_order_on_empty(bst_empty):
    """Should raise error on next of empty tree."""
    in_order = bst_empty.in_order()
    with pytest.raises(StopIteration):
        assert next(in_order)


def test_in_order_on_full(bst_filled):
    """Test that in order accurately returns nodes in order."""
    assert [node for node in bst_filled.in_order()] == [15, 20, 30, 40, 50, 60]


def test_error_after_first_iteration_of_single_tree(bst_single):
    """Test that the second iteration of single tree yields an error."""
    in_order = bst_single.in_order()
    next(in_order)
    with pytest.raises(StopIteration):
        assert next(in_order)


def test_pre_order_on_empty(bst_empty):
    """Test that stop iteration raises on empty tree."""
    order = bst_empty.pre_order()
    with pytest.raises(StopIteration):
        assert next(order)


def test_post_order_on_empty(bst_empty):
    """Test that stop iteration raises on empty tree."""
    order = bst_empty.post_order()
    with pytest.raises(StopIteration):
        assert next(order)


def test_pre_order_on_full(bst_filled):
    """Test that in order accurately returns nodes in order."""
    assert [node for node in bst_filled.pre_order()] == [40, 20, 15, 30, 50, 60]


def test_post_order_on_full(bst_filled):
    """Test that in order accurately returns nodes in order."""
    assert [node for node in bst_filled.post_order()] == [15, 30, 20, 60, 50, 40]


def test_error_after_first_iteration_of_single_tree_pre_order(bst_single):
    """Test that the second iteration of single tree yields an error."""
    order = bst_single.pre_order()
    next(order)
    with pytest.raises(StopIteration):
        assert next(order)


def test_error_after_first_iteration_of_single_tree_post_order(bst_single):
    """Test that the second iteration of single tree yields an error."""
    order = bst_single.post_order()
    next(order)
    with pytest.raises(StopIteration):
        assert next(order)


@pytest.mark.parametrize("input_table, result", IN_ORDER_TABLE)
def test_in_order_parametrize(input_table, result):
    """Test a bunch of values on in order."""
    from bst import BinarySearchTree
    bst = BinarySearchTree(input_table)
    assert [node for node in bst.in_order()] == result


@pytest.mark.parametrize("input_table, result", PRE_ORDER_TABLE)
def test_pre_order_parametrize(input_table, result):
    """Test a bunch of values on pre order."""
    from bst import BinarySearchTree
    bst = BinarySearchTree(input_table)
    assert [node for node in bst.pre_order()] == result


@pytest.mark.parametrize("input_table, result", POST_ORDER_TABLE)
def test_post_order_parametrize(input_table, result):
    """Test a bunch of values on post order."""
    from bst import BinarySearchTree
    bst = BinarySearchTree(input_table)
    assert [node for node in bst.post_order()] == result


def test_breadth_first_on_empty(bst_empty):
    """Test first value returned from breadth on empty table should be StopIteration."""
    gen = bst_empty.breadth_first()
    with pytest.raises(StopIteration):
        next(gen)


@pytest.mark.parametrize("input_table, result", BREADTH_ORDER_TABLE)
def test_breadth_order_parametrize(input_table, result):
    """Test a bunch of values on pre order."""
    from bst import BinarySearchTree
    bst = BinarySearchTree(input_table)
    assert [node for node in bst.breadth_first()] == result


def test_delete_single_child(bst_filled):
    bst_filled.delete_node(50)
    assert 50 not in [node for node in bst_filled.in_order()]


def test_delete_single_child_updates_size(bst_filled):
    size_before_delete = bst_filled.size()
    bst_filled.delete_node(50)
    assert bst_filled.size() == size_before_delete - 1


@pytest.mark.parametrize("input_table, result", DELETE_SINGLE_VALUE_TABLE)
def test_delete_single_child_parametrize(input_table, result):
    """Delete a variety of single tree nodes."""
    from bst import BinarySearchTree
    bst = BinarySearchTree(input_table)
    bst.delete_node(result)
    assert result not in [node for node in bst.in_order()]


@pytest.mark.parametrize("input_table, result", DELETE_SINGLE_VALUE_TABLE)
def test_delete_single_child_parametrize_updates_size(input_table, result):
    """Delete a variety of single tree nodes."""
    from bst import BinarySearchTree
    bst = BinarySearchTree(input_table)
    size_before_delete = bst.size()
    bst.delete_node(result)
    assert bst.size() == size_before_delete - 1


@pytest.mark.parametrize("input_table, result", DELETE_SINGLE_VALUE_TABLE2)
def test_delete_single_child_parametrize_twice(input_table, result):
    """Delete a variety of single tree nodes."""
    from bst import BinarySearchTree
    bst = BinarySearchTree(input_table)
    bst.delete_node(result[0])
    bst.delete_node(result[1])
    assert result[0] not in [node for node in bst.in_order()]
    assert result[1] not in [node for node in bst.in_order()]


@pytest.mark.parametrize("input_table, result", DELETE_SINGLE_VALUE_TABLE2)
def test_delete_single_child_parametrize_twice_updates_size(input_table, result):
    """Delete a variety of single tree nodes."""
    from bst import BinarySearchTree
    bst = BinarySearchTree(input_table)
    size_before_delete = bst.size()
    bst.delete_node(result[0])
    bst.delete_node(result[1])
    assert bst.size() == size_before_delete - 2


def test_delete_barren_nodes(bst_filled):
    """A barren node's child where the node was should be empty."""
    bst_filled.delete_node(60)
    node = bst_filled.search(50)
    assert not node.right_child


def test_delete_barren_nodes_updates_size(bst_filled):
    """A barren node's child where the node was should be empty."""
    size_before_delete = bst_filled.size()
    bst_filled.delete_node(60)
    assert bst_filled.size() == size_before_delete - 1


def test_delete_barren_nodes2(bst_filled):
    """A barren node's child where the node was should be empty."""
    bst_filled.delete_node(15)
    node = bst_filled.search(20)
    assert not node.left_child


@pytest.mark.parametrize("input_table, result", DELETE_BARREN_VALUE_TABLE)
def test_delete_barren_nodes_parametrize(input_table, result):
    """A barren node's child where the node was should be empty."""
    from bst import BinarySearchTree
    bst = BinarySearchTree(input_table)
    node = bst.search(result)
    parent = node.parent
    bst.delete_node(result)
    if parent.right_child:
        assert not parent.left_child
    if parent.left_child:
        assert not parent.right_child


def test_delete_barren_root(bst_single):
    """Deleting a barren root should remove it from the tree."""
    bst_single.delete_node(1)
    assert 1 not in [node for node in bst_single.in_order()]


def test_delete_barren_root_updates_size(bst_single):
    """Deleting a barren root should make size 0."""
    bst_single.delete_node(1)
    assert bst_single.size() == 0
