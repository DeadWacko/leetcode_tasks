# Решение:

## Лучший вариант:

```python
def twoSum( nums: list[int], target: int) -> list[int]:
    hashmap = {} # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[n] = i

    return

```


### Сложность:
* Время: __O(n)__



* Пространство: __O(n)__