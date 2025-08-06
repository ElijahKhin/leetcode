# test_sort_template.py
import pytest

from sort import sort as sort_func

def test_empty():
    assert sort_func([]) == []


def test_single():
    assert sort_func([1]) == [1]


def test_sorted():
    arr = [1, 2, 3, 4, 5]
    assert sort_func(arr.copy()) == [1, 2, 3, 4, 5]


def test_reverse():
    assert sort_func([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_random():
    assert sort_func([3, 1, 4, 5, 2]) == [1, 2, 3, 4, 5]


def test_duplicates():
    assert sort_func([2, 3, 2, 1, 3, 1]) == [1, 1, 2, 2, 3, 3]


def test_all_equal():
    assert sort_func([7, 7, 7, 7]) == [7, 7, 7, 7]
