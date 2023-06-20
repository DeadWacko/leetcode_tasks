import pytest
from solution_219 import containsNearbyDuplicate
import pytest

def test_containsNearbyDuplicate_duplicate_within_range():
    nums = [1, 2, 3, 1]
    k = 3
    assert containsNearbyDuplicate(nums, k) == True

def test_containsNearbyDuplicate_duplicate_within_range_multiple():
    nums = [1, 2, 3, 1, 2]
    k = 4
    assert containsNearbyDuplicate(nums, k) == True

def test_containsNearbyDuplicate_duplicate_within_range_repeated():
    nums = [1, 0, 1, 1]
    k = 1
    assert containsNearbyDuplicate(nums, k) == True

def test_containsNearbyDuplicate_duplicate_at_boundary():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    k = 10
    assert containsNearbyDuplicate(nums, k) == True

def test_containsNearbyDuplicate_duplicate_outside_range():
    nums = [1, 2, 3, 4, 5]
    k = 2
    assert containsNearbyDuplicate(nums, k) == False

def test_containsNearbyDuplicate_no_duplicates():
    nums = [1, 2, 3, 4, 5]
    k = 3
    assert containsNearbyDuplicate(nums, k) == False

def test_containsNearbyDuplicate_single_element():
    nums = [1]
    k = 0
    assert containsNearbyDuplicate(nums, k) == False

def test_containsNearbyDuplicate_empty_array():
    nums = []
    k = 2
    assert containsNearbyDuplicate(nums, k) == False

def test_containsNearbyDuplicate_negative_numbers():
    nums = [-1, 2, -3, 1, 2, -3]
    k = 2
    assert containsNearbyDuplicate(nums, k) == False

def test_containsNearbyDuplicate_large_range():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 100
    assert containsNearbyDuplicate(nums, k) == False

#Жмяк на меня
if __name__ == "__main__":
    pytest.main(['-q', '--report=f'])