import pytest
from solution_205 import isIsomorphic
def test_isIsomorphic_same_string():
    assert isIsomorphic("egg", "egg") == True

def test_isIsomorphic_different_lengths():
    assert isIsomorphic("egg", "adda") == False

def test_isIsomorphic_isomorphic_strings():
    assert isIsomorphic("egg", "add") == True

def test_isIsomorphic_not_isomorphic_strings():
    assert isIsomorphic("foo", "bar") == False

def test_isIsomorphic_longer_strings():
    assert isIsomorphic("paper", "title") == True

def test_isIsomorphic_empty_strings():
    assert isIsomorphic("", "") == True

def test_isIsomorphic_single_character_strings():
    assert isIsomorphic("a", "b") == True

def test_isIsomorphic_special_characters():
    assert isIsomorphic("!@#", "$%^") == True

def test_isIsomorphic_unicode_strings():
    assert isIsomorphic("éêè", "ûùú") == True

def test_isIsomorphic_mixed_case_strings():
    assert isIsomorphic("AbC", "XyZ") == True

#Жмяк на меня
if __name__ == "__main__":
    pytest.main(['-q', '--report=f'])