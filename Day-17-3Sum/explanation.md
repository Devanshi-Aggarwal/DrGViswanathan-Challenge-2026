# LeetCode 15 - 3Sum

## Problem Statement
Given an integer array `nums`, return all unique triplets:

`[nums[i], nums[j], nums[k]]`

such that:
- i ≠ j
- i ≠ k
- j ≠ k
- nums[i] + nums[j] + nums[k] = 0

The solution set must not contain duplicate triplets.

---

## Approach Used: Sorting + Two Pointers

A brute force approach would check all triplets.

That would take:

O(n³)

Too slow.

Instead, we optimize using:
- Sorting
- Two Pointers

---

## Core Idea

1. Sort the array
2. Fix one element at index `i`
3. Use two pointers:
   - Left = i + 1
   - Right = end of array
4. Check sum of three numbers

Cases:
- Sum = 0 → valid triplet found
- Sum < 0 → move left pointer right
- Sum > 0 → move right pointer left

---

## Handling Duplicates

Duplicates must be avoided.

We skip duplicates:
- For fixed element `i`
- For left pointer
- For right pointer

This ensures unique triplets only.

---

## Algorithm

1. Sort array
2. Loop through each index `i`
3. Skip duplicate values of `i`
4. Initialize:
   - `l = i + 1`
   - `r = len(nums) - 1`
5. While `l < r`:
   - Calculate sum
   - If 0 → store triplet
   - Move pointers accordingly
6. Return answer

---

## Python Solution

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []

        ans = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                summ = nums[i] + nums[l] + nums[r]

                if summ == 0:
                    ans.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1

                elif summ < 0:
                    l += 1
                else:
                    r -= 1

        return ans
```

---

## Complexity Analysis

### Time Complexity
Sorting:
O(n log n)

Two pointer traversal:
O(n²)

Final:
O(n²)

---

### Space Complexity
O(1) extra space  
(ignoring output array)

---

## Key Learning

This problem is a classic example of reducing:
- O(n³) brute force  
to  
- O(n²) optimized solution

Major concepts practiced:
- Sorting
- Two Pointers
- Duplicate handling
- Optimization thinking
