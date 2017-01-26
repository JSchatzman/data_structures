"""Test trie.py"""


import pytest


@pytest.fixture
def empty_trie():
    """Create empty testing trie."""
    from trie import Trie
    trie = Trie()
    return trie


@pytest.fixture
def tricky_trie():
    """Create tricky testing trie."""
    from trie import Trie
    trie = Trie()
    trie.insert('bbbbbbb')
    trie.insert('bbb')
    trie.insert('lololololol')
    trie.insert('blololololol')
    return trie


@pytest.fixture
def delete_tree():
    """A tree with branches to remove from."""
    from trie import Trie
    t = Trie()
    t.insert("ted")
    t.insert("tea")
    t.insert("teabag")
    t.insert("teabags")
    t.insert("teabagger")
    t.insert("teabaggers")
    t.insert("teabagged")
    return t


def test_empty_tree_size(empty_trie):
    """Test empty tree size is 0."""
    assert empty_trie.size() == 0


def test_insert_must_be_string(empty_trie):
    with pytest.raises(TypeError):
        empty_trie.insert(45)


def test_insert_must_be_string2(empty_trie):
    with pytest.raises(TypeError):
        empty_trie.insert((45, 54))


def test_insert_must_be_string3(empty_trie):
    with pytest.raises(TypeError):
        empty_trie.insert(True)


def test_insert_must_be_string4(empty_trie):
    with pytest.raises(TypeError):
        empty_trie.insert([])


def test_insert_must_be_string5(empty_trie):
    with pytest.raises(TypeError):
        empty_trie.insert([0])


def test_insert_must_be_string6(empty_trie):
    with pytest.raises(TypeError):
        empty_trie.insert(None)


def test_insert_must_be_string7(empty_trie):
    with pytest.raises(TypeError):
        empty_trie.insert(45.54)


def test_insert_must_be_string8(empty_trie):
    with pytest.raises(TypeError):
        empty_trie.insert(int)


def test_insert_on_empty(empty_trie):
    """Test that inserting into an empty tree works correctly."""
    empty_trie.insert('hello')
    assert 'h' in empty_trie.root.keys()
    assert empty_trie.size() == 1


def test_double_insert_on_empty(empty_trie):
    """Test double insert does not increase size."""
    empty_trie.insert('hello')
    empty_trie.insert('hello')
    assert empty_trie.size() == 1


def test_shorter_valid_string_is_contained(tricky_trie):
    """Test that searching for substring does work."""
    assert tricky_trie.contains('bbb')


def test_nonexisting_string_not_contained(tricky_trie):
    """Test that search for non existing tree returns false."""
    assert not tricky_trie.contains('no')


def test_on_tricky_trie(tricky_trie):
    """Test that size on tricky trie is correct."""
    assert tricky_trie.size() == 4


def test_remove_childless_on_delete_tree(delete_tree):
    """Test the remove function on childless Node."""
    tree_size = delete_tree.size()
    delete_tree.remove("teabaggers")
    assert delete_tree.size() == tree_size - 1


def test_remove_middle_child_on_delete_tree(delete_tree):
    """Test the remove function on a middle child."""
    tree_size = delete_tree.size()
    delete_tree.remove("teabag")
    assert delete_tree.size() == tree_size - 1


def test_remove_top_but_not_root(delete_tree):
    """Test removing a top but not the root."""
    tree_size = delete_tree.size()
    delete_tree.remove("tea")
    assert delete_tree.size() == tree_size - 1


def test_remove_childless_on_delete_tree2(delete_tree):
    """Test the remove function on childless Node."""
    delete_tree.remove("teabaggers")
    assert delete_tree.contains("teabaggers") is False


def test_remove_middle_child_on_delete_tree2(delete_tree):
    """Test the remove function on a middle child."""
    delete_tree.remove("teabag")
    assert delete_tree.contains("teabag") is False


def test_remove_top_but_not_root2(delete_tree):
    """Test removing a top but not the root."""
    delete_tree.remove("tea")
    assert delete_tree.contains("teabag") is False


def test_remove_not_in_tree_raises_error(delete_tree):
    """Removing a value not in the tree should raise an error."""
    with pytest.raises(ValueError):
        delete_tree.remove("toldyouso raise an error")