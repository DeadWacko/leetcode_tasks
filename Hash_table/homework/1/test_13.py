from solution_13 import romanToInt

import pytest


def test_roman_to_int_1():
    assert romanToInt("III") == 3

def test_roman_to_int_2():
    assert romanToInt("LVIII") == 58

def test_roman_to_int_3():
    assert romanToInt("MCMXCIV") == 1994

def test_roman_to_int_4():
    assert romanToInt("IV") == 4

def test_roman_to_int_5():
    assert romanToInt("IX") == 9

def test_roman_to_int_6():
    assert romanToInt("XL") == 40

def test_roman_to_int_7():
    assert romanToInt("XC") == 90

def test_roman_to_int_8():
    assert romanToInt("CD") == 400

def test_roman_to_int_9():
    assert romanToInt("CM") == 900

def test_roman_to_int_10():
    assert romanToInt("MMMCMXCIX") == 3999


#Жмяк на меня
if __name__ == "__main__":
    pytest.main(['-q', '--report=f'])
