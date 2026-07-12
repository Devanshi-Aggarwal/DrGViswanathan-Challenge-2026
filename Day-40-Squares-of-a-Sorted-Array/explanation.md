# 977. Squares of a Sorted Array

## Problem Statement

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number, also sorted in non-decreasing order.

---

## Approach

This solution uses the **Two Pointer** technique.

### Key Observations

- The largest square will always come from either:
  - the leftmost (most negative) number, or
  - the rightmost (largest positive) number.
- Compare the squares of both ends.
- Append the larger square to the answer.
- Move the corresponding pointer inward.
- Since larger values are added first, reverse the final array before returning it.

This avoids sorting after squaring and achieves linear time complexity.

---

## Algorithm

1. Initialize two pointers:
   - `i` at the beginning.
   - `j` at the end.
2. Compare `nums[i]²` and `nums[j]²`.
3. Append the larger square to the answer.
4. Move the corresponding pointer.
5. Continue until both pointers meet.
6. Reverse the answer array.
7. Return the result.

---

## Example

Input:

```text
nums = [-4,-1,0,3,10]
```

Processing:

```text
Compare:

(-4)² = 16
10² = 100

Append 100

Compare:

(-4)² = 16
3² = 9

Append 16

Compare:

(-1)² = 1
3² = 9

Append 9

Compare:

(-1)² = 1
0² = 0

Append 1

Append 0

Answer before reversing:

[100,16,9,1,0]

Reverse →

[0,1,9,16,100]
```

Output:

```text
[0,1,9,16,100]
```

---

## Complexity Analysis

### Time Complexity

**O(n)**

Each element is processed exactly once.

### Space Complexity

**O(n)**

The output array stores the squared values.

---

## Key Learnings

- Two Pointer Technique
- Sorted Array Processing
- Absolute Value Comparison
- Linear Time Optimization
- Reverse Construction
- Array Traversal
