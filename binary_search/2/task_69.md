## 69. Sqrt(x) <span style="background-color: green; padding: 2px 4px; border-radius: 4px;">Easy</span>
[Задача](https://leetcode.com/problems/sqrtx/description/)

Учитывая неотрицательное целое число x, вернуть квадратный корень из xокругленного вниз до ближайшего целого числа . Возвращаемое целое число также должно быть неотрицательным .

Вы **НЕ ДОЛЖНЫ** использовать какие-либо встроенные экспонентные функции или операторы.

###### Например, не используйте x ** 0.5python.

Пример 1:

```python
x = 4 # функция вернет 2

#Объяснение: Квадратный корень из 4 равен 2, поэтому мы возвращаем 2.
```


Пример 2:
```python
x = 8 # функция вернет 2

# Объяснение: Квадратный корень из 8 равен 2,82842..., и, поскольку мы округляем его до ближайшего целого числа, возвращается 2.
```


Ограничения:

* 0 <= x <= 231 - 1