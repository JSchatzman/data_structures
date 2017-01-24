# -*- coding: utf-8 -*-

import pytest
import io
import sys
import random

file = io.open('/etc/dictionaries-common/words')
words = file.read()

if sys.version[0] == "2":
    words = words.encode("utf8")

WORD_LIST = words.split('\n')

WORD_LIST = WORD_LIST[0:2000]


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
    """Test instantiation of a HashTable with default hash type."""
    from hash_table import HashTable
    rocket_appliances = HashTable(8)
    assert rocket_appliances.size == 8


def test_basic_hash_table_exists_with_empty_table():
    """A new HashTable should have a list of empty lists."""
    from hash_table import HashTable
    rocket_appliances = HashTable(8)
    assert rocket_appliances.hash_table == [[], [], [], [], [], [], [], []]


def test_bern_hash_table_exists(small_table_bern):
    """Test creation of a Bernstein HashTable."""
    assert small_table_bern.size == 8


def test_bern_hash_table_exists_with_empty_table(small_table_bern):
    """A new HashTable should have a list of empty lists."""
    assert small_table_bern.hash_table == [[], [], [], [], [], [], [], []]


def test_collision_on_basic_small_hash(small_table_naive):
    """Collision on table should be accessible because handled by keypair."""
    small_table_naive.set("a", "Nobody wants to admit they ate nine cans of ravioli")
    small_table_naive.set("i", "It's basically just supply and command.")
    assert small_table_naive.get("a") == "Nobody wants to admit they ate nine cans of ravioli"


def test_collision_on_bern_small_hash(small_table_bern):
    """Collision on table should be accessible because handled by keypair."""
    small_table_bern.set("a", "Nobody wants to admit they ate nine cans of ravioli")
    small_table_bern.set("i", "It's basically just supply and command.")
    assert small_table_bern.get("a") == "Nobody wants to admit they ate nine cans of ravioli"


def test_collision_on_medium_basic_hash(medium_table_naive):
    """Test collisions on a grander scale."""
    for word in WORD_LIST:
        medium_table_naive.set(str(word), str(word))
    word = WORD_LIST[random.randint(0, 2000)]
    assert medium_table_naive.get(word) == word


def test_collision_on_medium_bern_hash(medium_table_bern):
    """Test collisions on a grander scale."""
    for word in WORD_LIST:
        medium_table_bern.set(str(word), str(word))
    word = WORD_LIST[random.randint(0, 2000)]
    assert medium_table_bern.get(word) == word


def test_error_when_hash_type_invalid():
    """An invalid HashTable hash_type should raise an error."""
    from hash_table import HashTable
    with pytest.raises(NameError):
        HashTable(18, hash_type='Invalid')


def test_error_when_non_string_passed_to_set1(medium_table_bern):
    """Passing a non-string value for the key should raise error."""
    with pytest.raises(TypeError):
        medium_table_bern.set(18, 19)


def test_error_when_non_string_passed_to_set2(medium_table_bern):
    """Passing a non-string value for the key should raise error."""
    with pytest.raises(TypeError):
        medium_table_bern.set([18], [19])


def test_error_when_non_string_passed_to_set3(medium_table_bern):
    """Passing a non-string value for the key should raise error."""
    with pytest.raises(TypeError):
        medium_table_bern.set(True, 18)


def test_error_when_non_string_passed_to_set4(medium_table_bern):
    """Passing a non-string value for the key should raise error."""
    with pytest.raises(TypeError):
        medium_table_bern.set(True, "18")


def test_error_when_non_string_passed_to_set_naive1(small_table_naive):
    """Passing a non-string value for the key should raise error."""
    with pytest.raises(TypeError):
        small_table_naive.set(18, 19)


def test_error_when_non_string_passed_to_set_naive2(small_table_naive):
    """Passing a non-string value for the key should raise error."""
    with pytest.raises(TypeError):
        small_table_naive.set([18], [19])


def test_error_when_non_string_passed_to_set_naive3(small_table_naive):
    """Passing a non-string value for the key should raise error."""
    with pytest.raises(TypeError):
        small_table_naive.set(True, 18)


def test_error_when_non_string_passed_to_set_naive4(small_table_naive):
    """Passing a non-string value for the key should raise error."""
    with pytest.raises(TypeError):
        small_table_naive.set(True, "18")


def test_values_can_be_anything_bern_1(large_table_bern):
    """The value stored should be able to be anything."""
    large_table_bern.set("a", 18)
    assert large_table_bern.get("a") == 18


def test_values_can_be_anything_bern_2(large_table_bern):
    """The value stored should be able to be anything."""
    large_table_bern.set("a", [18])
    assert large_table_bern.get("a") == [18]


def test_values_can_be_anything_bern_3(large_table_bern):
    """The value stored should be able to be anything."""
    large_table_bern.set("a", (18,))
    assert large_table_bern.get("a") == (18,)


def test_values_can_be_anything_bern_4(large_table_bern):
    """The value stored should be able to be anything."""
    large_table_bern.set("a", True)
    assert large_table_bern.get("a") is True


def test_values_can_be_anything_naive_1(large_table_naive):
    """The value stored should be able to be anything."""
    large_table_naive.set("a", 18)
    assert large_table_naive.get("a") == 18


def test_values_can_be_anything_naive_2(large_table_naive):
    """The value stored should be able to be anything."""
    large_table_naive.set("a", [18])
    assert large_table_naive.get("a") == [18]


def test_values_can_be_anything_naive_3(large_table_naive):
    """The value stored should be able to be anything."""
    large_table_naive.set("a", (18,))
    assert large_table_naive.get("a") == (18,)


def test_values_can_be_anything_naive_4(large_table_naive):
    """The value stored should be able to be anything."""
    large_table_naive.set("a", True)
    assert large_table_naive.get("a") is True
