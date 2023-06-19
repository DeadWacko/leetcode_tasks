import pytest
from solution_242 import isAnagram


def test_anagram_1():
    s = "anagram"
    t = "nagaram"
    assert isAnagram(s, t) == True

def test_anagram_2():
    s = "rat"
    t = "car"
    assert isAnagram(s, t) == False

def test_anagram_3():
    s = "listen"
    t = "silent"
    assert isAnagram(s, t) == True

def test_anagram_4():
    s = ""
    t = ""
    assert isAnagram(s, t) == True

def test_anagram_5():
    s = "abc"
    t = "abcd"
    assert isAnagram(s, t) == False

def test_anagram_6():
    s = "abcd"
    t = "abc"
    assert isAnagram(s, t) == False


if __name__ == "__main__":
    pytest.main(['-q', '--report=f'])

