## 49.Group Anagrams <span style="background-color: yellow; padding: 2px 4px; border-radius: 4px;">Medium</span>

[Задача](https://leetcode.com/problems/group-anagrams/description/)

Учитывая массив строк strs, сгруппируйте анаграммы вместе. Вы можете вернуть ответ в любом порядке .

Анаграмма — это слово или фраза, образованная путем перестановки букв другого слова или фразы, обычно с использованием всех исходных букв ровно один раз .

 

Пример 1:

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

Пример 2:
```
Input: strs = [""]
Output: [[""]]
```
Пример 3:
```
Input: strs = ["a"]
Output: [["a"]]
```
Ограничения:

* 1 <= strs.length <= 10^4
* 0 <= strs[i].length <= 100
* strs[i] состоит из строчных английских букв
