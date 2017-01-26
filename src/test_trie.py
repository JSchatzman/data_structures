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


def test_empty_tree_size(empty_trie):
    """Test empty tree size is 0."""
    assert empty_trie.size() == 0


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