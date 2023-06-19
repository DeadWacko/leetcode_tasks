from solution_217 import containsDuplicate

import pytest


def test_duplicates_exist():
    nums = [1, 2, 3, 1]
    assert containsDuplicate(nums) == True

    nums = [1, 1, 1, 1]
    assert containsDuplicate(nums) == True

    nums = [1, 2, 3, 2]
    assert containsDuplicate(nums) == True

def test_no_duplicates():
    nums = [1, 2, 3, 4]
    assert containsDuplicate(nums) == False

    nums = [5, 6, 7, 8]
    assert containsDuplicate(nums) == False

    nums = []
    assert containsDuplicate(nums) == False

def test_empty_array():
    nums = []
    assert containsDuplicate(nums) == False

def test_single_element():
    nums = [1]
    assert containsDuplicate(nums) == False

    nums = [5]
    assert containsDuplicate(nums) == False


if __name__ == "__main__":
    pytest.main(['-q', '--report=f'])

