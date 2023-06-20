## 205 . Isomorphic Strings <span style="background-color: green; padding: 2px 4px; border-radius: 4px;">Easy</span>

[Задача](https://leetcode.com/problems/isomorphic-strings/description/)

Даны две строки sи t, определите, изоморфны ли они .

Две строки sи tизоморфны, если символы в sможно заменить, чтобы получить t.

Все вхождения символа должны быть заменены другим символом с сохранением порядка символов. Никакие два символа не могут отображаться на один и тот же символ, но символ может отображаться на самого себя.



Пример 1:

```
Input: s = "egg", t = "add"
Output: true
```

Пример 2:

```
Input: s = "foo", t = "bar"
Output: false
```
Пример 3:
```
Input: s = "paper", t = "title"
Output: true
```



Ограничения:

* 1 <= s.length <= 5 * 10^4
* t.length == s.length
* s и t состоят из любого допустимого символа ascii.



