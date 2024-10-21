"""Utils Test: Unit Tests"""

from exercises.ex05.utils import only_evens, sub, add_at_index

import pytest

"""Only Evens Tests"""


def test_return_only_evens() -> None:
    """Tests that the correct value is returned"""
    test_list: list[int] = [15, 17, 34, 46, 25]
    assert only_evens(test_list) == [34, 46]  # assert what will be true


def test_mutation_only_evens() -> None:
    """Tests correct mutation (no mutation at all)"""
    test_list: list[int] = [15, 17, 34, 46, 25]
    only_evens(test_list)
    assert test_list == [15, 17, 34, 46, 25]


def test_edge_only_evens() -> None:
    """Tests an edge case"""
    test_list: list[int] = []
    assert only_evens(test_list) == []


"""Sub Tests"""


def test_return_sub() -> None:
    """Tests that the correct value is returned"""
    test_list: list[int] = [15, 17, 34, 46, 25]
    assert sub(test_list, 1, 3) == [17, 34]


def test_mutation_sub() -> None:
    """Tests correct mutation (no mutation at all)"""
    test_list: list[int] = [15, 17, 34, 46, 25]
    sub(test_list, 1, 3)
    assert test_list == [15, 17, 34, 46, 25]


def test_edge_sub() -> None:
    """Tests an edge case"""
    test_list: list[int] = [15, 17, 34, 46, 25]
    assert sub(test_list, -1, 3) == [15, 17, 34]


"""Add At Index Tests"""


def test_return_add_at_index() -> None:
    """Tests that the correct value is returned"""
    test_list: list[int] = [15, 17, 34, 46, 25]
    assert add_at_index(test_list, 27, 2) == None


def test_mutate_add_at_index() -> None:
    """Tests that the list was mutated"""
    test_list: list[int] = [15, 17, 34, 46, 25]
    add_at_index(test_list, 27, 2)
    assert test_list == [15, 17, 27, 34, 46, 25]


def test_edge_add_at_index() -> None:
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        add_at_index([15, 17, 34, 46, 25], 27, 45)
    # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num>
    # that is greater than the length of our <list_object>
