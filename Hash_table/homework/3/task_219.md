## 219. Contains Duplicate II <span style="background-color: green; padding: 2px 4px; border-radius: 4px;">Easy</span>

[Задача](https://leetcode.com/problems/contains-duplicate-ii/description/)

Учитывая целочисленный массив nums и целое число k, возвращает true если есть два различных индекса i и j в массиве, такие что nums[i] == nums[j]и abs(i - j) <= k .


Пример 1:

```
Input: nums = [1,2,3,1], k = 3
Output: true
```

Пример 2:

```
Input: nums = [1,0,1,1], k = 1
Output: true
```
Пример 3:
```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```



Ограничения:

* 1 <= nums.length <= 10^5
* -10^9 <= nums[i] <= 10^9
* 0 <= k <= 10^5



