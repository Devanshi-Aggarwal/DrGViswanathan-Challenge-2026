# LeetCode 167 - Two Sum II: Input Array Is Sorted

## Problem Statement
Given a **1-indexed sorted array** of integers `numbers`, find two numbers such that they add up to a specific target.

Return the indices of the two numbers (1-indexed).

Constraints:
- Exactly one solution exists
- Cannot use the same element twice
- Must use constant extra space

---

## Approach Used: Binary Search

Since the array is already sorted, we can use that property to search efficiently.

For each number:
1. Compute the required complement:
   target - current_number

2. Use binary search on the remaining right portion of the array.

3. If found, return indices.

---

## Algorithm

1. Traverse the array using index `i`.
2. Calculate:
   complement = target - numbers[i]
3. Binary search in the range `i+1` to `n-1`.
4. If complement exists:
   return indices (1-indexed)

---

## Python Solution

```python
from bisect import bisect_left

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n - 1):
            x = target - numbers[i]
            j = bisect_left(numbers, x, lo=i + 1)

            if j < n and numbers[j] == x:
                return [i + 1, j + 1]
```

---

## Complexity Analysis

### Time Complexity
O(n log n)

- Loop runs n times
- Binary search takes log n

Total = O(n log n)

### Space Complexity
O(1)

Only constant extra variables used.

---

## Key Learning

Whenever a problem says:
- Array is sorted
- Need to search values quickly

Think about:
- Binary Search
- Two Pointers

Using sorted properties often reduces brute-force complexity significantly.
