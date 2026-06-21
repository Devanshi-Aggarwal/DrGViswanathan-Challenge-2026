# LeetCode 704 - Binary Search

## Problem Statement
Given a sorted array `nums` and an integer `target`, return the index of `target` if it exists in the array.

Otherwise, return `-1`.

The algorithm must run in:

O(log n)

---

## Approach Used: Binary Search

Since the array is already sorted, binary search is the best approach.

Instead of checking every element one by one, we repeatedly divide the search space into half.

This reduces time complexity significantly.

---

## Core Idea

At each step:

1. Find middle element
2. Compare with target

Cases:

- If middle == target → answer found
- If middle < target → search right half
- If middle > target → search left half

This cuts search space in half every iteration.

---

## Python Shortcut Used

I used Python's built-in `bisect_left()`.

`bisect_left(nums, target)` returns:
- the leftmost position where target should be inserted

Then:
- If target exists at that index → return index
- Else → return -1

---

## Algorithm

1. Use `bisect_left()` to find insertion position
2. Check if index is valid
3. Check whether value at index equals target
4. Return index or -1

---

## Python Solution

```python
import bisect

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i = bisect.bisect_left(nums, target)
        return -1 if i == len(nums) or nums[i] != target else i
```

---

## Complexity Analysis

### Time Complexity
Binary Search:

O(log n)

---

### Space Complexity
O(1)

---

## Key Learning

Binary Search is one of the most important algorithms in DSA.

Main concepts practiced:
- Sorted arrays
- Divide and conquer
- Logarithmic search
- Python bisect module
