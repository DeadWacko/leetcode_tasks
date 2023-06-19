import pytest

from solution_347 import topKFrequent


def test_top_k_frequent_elements_1():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    expected = [1, 2]
    assert topKFrequent(nums, k) == expected


def test_top_k_frequent_elements_2():
    nums = [1]
    k = 1
    expected = [1]
    assert topKFrequent(nums, k) == expected


def test_top_k_frequent_elements_3():
    nums = [4, 1, -1, 2, -1, 2, 3]
    k = 2
    expected = [-1, 2]
    assert topKFrequent(nums, k) == expected





def test_top_k_frequent_elements_4():
    nums = [9, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1]
    k = 5
    expected = [9, 8, 7, 6, 5]
    assert topKFrequent(nums, k) == expected


def test_top_k_frequent_elements_5():
    nums = [-2, -2, 1, 1, 4, 4, 5, 5, 5, 5, 5]
    k = 3
    expected = [5, -2, 1]
    assert topKFrequent(nums, k) == expected


if __name__ == "__main__":
    pytest.main(['-q', '--report=f'])
