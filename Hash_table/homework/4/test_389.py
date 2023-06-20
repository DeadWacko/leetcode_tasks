import pytest
from solution_389 import findTheDifference




# Тесты

def test_example_1():
    s = "abcd"
    t = "abcde"
    assert findTheDifference(s, t) == "e"

def test_example_2():
    s = ""
    t = "y"
    assert findTheDifference(s, t) == "y"

def test_single_letter():
    s = "a"
    t = "ab"
    assert findTheDifference(s, t) == "b"



def test_repeated_letter():
    s = "aaabbbccc"
    t = "bbbaaaccce"
    assert findTheDifference(s, t) == "e"



def test_empty_string():
    s = ""
    t = "x"
    assert findTheDifference(s, t) == "x"



def test_different_order():
    s = "abcde"
    t = "edcbae"
    assert findTheDifference(s, t) == "e"




#Жмяк на меня
if __name__ == "__main__":
    pytest.main(['-q', '--report=f'])