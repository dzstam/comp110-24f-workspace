__author__: str = "730461334"

from CQs.cq07.find_max import find_and_remove_max


def test_returns_find_and_remove_max() -> None:
    """Use Case: Returns"""
    assert find_and_remove_max([15, 1, 2, 10, 15]) == 15  # assert what will be true


def test_mutate_find_and_remove_max() -> None:
    """Use Case: Mutate"""
    test_list: list[int] = [15, 1, 2, 10, 15]
    find_and_remove_max(test_list)
    assert test_list == [1, 2, 10]


def test_edge_find_and_remove_max() -> None:
    """Edge Case"""
    test_list: list[int] = []
    assert find_and_remove_max(test_list) == -1
