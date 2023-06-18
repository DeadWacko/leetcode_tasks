## 347. Top K Frequent Elements <span style="background-color: yellow; padding: 2px 4px; border-radius: 4px;">Medium</span>  

[Задача](https://leetcode.com/problems/top-k-frequent-elements/)

Учитывая целочисленный массив numsи целое число k, вернуть наиболее k часто встречающиеся элементы . Вы можете вернуть ответ в любом порядке .

Пример 1:

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

Пример 2:
```
Input: nums = [1], k = 1
Output: [1]
```

Ограничения:

* 1 <= nums.length <= 10^5
* -10^4 <= nums[i] <= 10^4
* kнаходится в диапазоне [1, the number of unique elements in the array]
* Гарантируется , что ответ единственный .

Дополнение: временная сложность вашего алгоритма должна быть лучше, чем O(n log n), где n — размер массива.