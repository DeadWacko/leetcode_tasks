import pytest

from solution_1 import twoSum

def test_example_1():
    nums = [2, 7, 11, 15]
    target = 9
    assert twoSum(nums, target) == [0, 1]

def test_example_2():
    nums = [3, 2, 4]
    target = 6
    assert twoSum(nums, target) == [1, 2]

if __name__ == "__main__":
    pytest.main(['-q', '--report=f'])
