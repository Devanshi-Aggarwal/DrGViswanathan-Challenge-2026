# 33. Search in Rotated Sorted Array

## Problem

Given a rotated sorted array and a target value, return the index of the target if it exists; otherwise return `-1`.

The solution must run in **O(log n)** time.

---

## Approach: Modified Binary Search

Normal binary search works on fully sorted arrays.

Here, the array is rotated, so we modify binary search.

### Key Observation

At every step, **at least one half is always sorted**:

* Left half sorted OR
* Right half sorted

We identify the sorted half and check whether the target lies inside it.

---

## Steps

1. Initialize `left` and `right`.
2. Compute middle.
3. If middle equals target → return index.
4. Check whether left half is sorted.
5. If target lies inside sorted half, search there.
6. Otherwise search the other half.
7. Continue until search space ends.

---

## Python Solution

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
```

---

## Complexity Analysis

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

---

## Key Learning

* Rotated arrays
* Modified Binary Search
* Search space reduction
* Sorted-half identification
