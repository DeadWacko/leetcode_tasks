# Решение:

## Лучший вариант:

```python
def containsDuplicate(nums: list[int]) -> bool:
    hashmap = set()

    for i in nums:
        if i in hashmap:
            return True
        hashmap.add(i)
    return False

```


### Сложность:
* Время: __O(n)__



* Пространство: __O(n)__