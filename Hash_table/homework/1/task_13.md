## 13. Roman to Integer <span style="background-color: green; padding: 2px 4px; border-radius: 4px;">Easy</span>

[Задача](https://leetcode.com/problems/roman-to-integer/description/)

Римские цифры представлены семью различными символами:

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

Например,  2 пишется как II римскими цифрами,это просто две сложенные вместе I. 12 пишется как  XII, что просто X + II. Число 27 записывается как XXVII, то есть XX + V + II.

Римские цифры обычно пишутся слева направо от большего к меньшему. Однако цифра «четыре» — не IIII. Вместо этого цифра четыре записывается как IV. Так как единица предшествует пятерке, мы вычитаем ее и получаем четыре. Тот же принцип применим к числу девять, которое записывается как IX. Есть шесть случаев, когда используется вычитание:

I можно поставить перед V(5) и X(10), чтобы получилось 4 и 9. 
X можно поставить перед L(50) и C(100), чтобы получилось 40 и 90. 
C можно поставить перед D(500) и M(1000), чтобы получить 400 и 900.

Вам дана римская цифра. Ее необходимо преобразовать в целое число.


Пример 1:

```
Input: s = "III"
Output: 3
Explanation: III = 3.
```

Пример 2:

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```



Ограничения:

* 1 <= s.length <= 15
* s содержит только символы ('I', 'V', 'X', 'L', 'C', 'D', 'M')
* Гарантируется ,  что s это допустимая римская цифра в диапазоне [1, 3999]



