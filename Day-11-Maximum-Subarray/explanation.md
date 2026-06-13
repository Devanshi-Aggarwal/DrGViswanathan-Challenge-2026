# LeetCode 53 - Maximum Subarray

## Problem Statement

Given an integer array `nums`, find the contiguous subarray with the largest sum and return its sum.

---

## Approach

I used **Kadane’s Algorithm**, an efficient greedy approach for solving maximum subarray problems.

While traversing the array, I maintain:

- `summ` → Maximum sum of subarray ending at current index
- `ans` → Overall maximum subarray sum found so far

At each step, I decide whether to:

- Start a new subarray from the current element
or
- Extend the previous subarray

This ensures the best possible sum is tracked in one pass.

---

## Algorithm

1. Initialize `ans` as negative infinity.
2. Initialize running sum `summ` as 0.
3. Traverse through the array.
4. Update running sum using:
   - current element alone, or
   - current element + previous sum
5. Update global maximum.
6. Return the answer.

---

## Complexity Analysis

### Time Complexity

O(n)

The array is traversed exactly once.

### Space Complexity

O(1)

Only constant extra space is used.

---

## Key Learning

Kadane’s Algorithm is a classic example of dynamic programming combined with greedy thinking.

Instead of checking all possible subarrays, we keep only the best subarray ending at each index, reducing complexity from O(n²) to O(n).

---

## Concepts Practiced

- Arrays
- Dynamic Programming
- Kadane’s Algorithm
- Greedy Approach
- Optimization
