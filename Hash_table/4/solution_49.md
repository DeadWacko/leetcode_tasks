# Решение:

## Лучший вариант:

```python
from collections import defaultdict


def groupAnagrams(strs: list[str]):
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26  # a ... z

        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)

    return list(res.values())

```


### Сложность:
* Время: __O(n)__



* Пространство: __O(n)__