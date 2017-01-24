# -*- coding: utf-8 -*-

import pytest
import io

file = io.open('/etc/dictionaries-common/words')
words = file.read()
WORD_LIST = words.split('\n')


@pytest.fixture
def small_table_naive():
    """A small Hash Table with a basic Hash algo."""
    from hash_table import HashTable
    return HashTable(8)


@pytest.fixture
def small_table_bern():
    """A small Hash Table with a Bernstein Hash algo."""
    from hash_table import HashTable
    return HashTable(8, 'bern')


@pytest.fixture
def medium_table_naive():
    """A medium Hash Table with a basic Hash algo."""
    from hash_table import HashTable
    return HashTable(150)


@pytest.fixture
def medium_table_bern():
    """A medium Hash Table with a Bernstein Hash algo."""
    from hash_table import HashTable
    return HashTable(150, 'bern')


@pytest.fixture
def large_table_naive():
    """A medium Hash Table with a basic Hash algo."""
    from hash_table import HashTable
    return HashTable(500)


@pytest.fixture
def large_table_bern():
    """A medium Hash Table with a Bernstein Hash algo."""
    from hash_table import HashTable
    return HashTable(500, 'bern')


def test_basic_hash_table_exists():
    from hash_table import HashTable
    rocket_appliances = HashTable(8)
    assert rocket_appliances.size == 8


def test_basic_hash_table_exists_with_empty_table():
    from hash_table import HashTable
    rocket_appliances = HashTable(8)
    assert rocket_appliances.hash_table == [[], [], [], [], [], [], [], []]


def test_bern_hash_table_exists(small_table_bern):
    assert small_table_bern.size == 8


def test_bern_hash_table_exists_with_empty_table(small_table_bern):
    assert small_table_bern.hash_table == [[], [], [], [], [], [], [], []]


def test_collision_on_basic_small_hash(small_table_naive):
    small_table_naive.set("a", "Nobody wants to admit they ate nine cans of ravioli")
    small_table_naive.set("i", "It's basically just supply and command.")
    assert small_table_naive.get("a") == "Nobody wants to admit they ate nine cans of ravioli"


def test_collision_on_bern_small_hash(small_table_bern):
    small_table_bern.set("a", "Nobody wants to admit they ate nine cans of ravioli")
    small_table_bern.set("i", "It's basically just supply and command.")
    assert small_table_bern.get("a") == "Nobody wants to admit they ate nine cans of ravioli"


def test_collision_on_medium_basic_hash(medium_table_naive):
    for word in WORD_LIST:
        medium_table_naive.set(str(word), str(word))
    assert medium_table_naive.get('Alberto') == "Alberto"


def test_collision_on_medium_bern_hash(medium_table_bern):
    for word in WORD_LIST:
        medium_table_bern.set(str(word), str(word))
    assert medium_table_bern.get('versed') == "versed"