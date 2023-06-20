# Решение:

## Лучший вариант:

```python
def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {} # подсчет вхождений каждого элемента
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n,c in count.items():
        freq[c].append(n) # n встречается c раз

    res = []
    for i in range(len(freq) -1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

```


### Сложность:
* Время: __O(n)__



* Пространство: __O(n)__