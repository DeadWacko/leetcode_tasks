from solution_49 import groupAnagrams
import pytest

def test_anagram_groups_1():
    # Пример 1: Слова "eat", "tea", "ate" являются анаграммами, "tan" и "nat" - также.
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert groupAnagrams(strs) == expected

def test_anagram_groups_2():
    # Пример 2: Входной список содержит только одну пустую строку.
    strs = [""]
    expected = [[""]]
    assert groupAnagrams(strs) == expected

def test_anagram_groups_3():
    # Пример 3: Входной список содержит только одно слово "a".
    strs = ["a"]
    expected = [["a"]]
    assert groupAnagrams(strs) == expected

def test_anagram_groups_3():
    # Дополнительный тест: Входной список содержит две анаграммы "listen" и "silent".
    strs = ["listen", "silent"]
    expected = [["listen", "silent"]]
    assert groupAnagrams(strs) == expected

def test_anagram_groups_4():
    # Дополнительный тест: Входной список содержит анаграммы "abc", "acb", "bac" и "bca".
    strs = ["abc", "acb", "bac", "bca"]
    expected = [["abc", "acb", "bac", "bca"]]
    assert groupAnagrams(strs) == expected

def test_anagram_groups_5():
    # Дополнительный тест: Входной список содержит разные слова без анаграмм.
    strs = ["apple", "banana", "orange", "grape"]
    expected = [["apple"], ["banana"], ["orange"], ["grape"]]
    assert groupAnagrams(strs) == expected





#Тык сюдым
if __name__ == "__main__":
    pytest.main(['-q', '--report=f'])
