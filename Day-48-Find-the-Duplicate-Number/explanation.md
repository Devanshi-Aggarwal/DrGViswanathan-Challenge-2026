# 287. Find the Duplicate Number

## Problem Statement

You are given an array `nums` containing `n + 1` integers where each integer is in the range `[1, n]`.

There is only one repeated number, but it may appear multiple times.

Return the duplicate number **without modifying the array** and **using only constant extra space**.

---

## Approach

This problem can be solved using **Floyd's Tortoise and Hare (Cycle Detection) Algorithm**.

Think of every value in the array as a pointer to the next index.

Example:

nums = [1,3,4,2,2]

```text
0 → 1 → 3 → 2 → 4
          ↑     ↓
          └─────┘
```

Since one number is duplicated, a cycle is formed.

The duplicate number is exactly the **starting point of the cycle**.

---

## Algorithm

### Phase 1: Detect the Cycle

- Initialize two pointers:
  - Slow moves one step.
  - Fast moves two steps.
- Continue until both pointers meet.

This guarantees that a cycle exists.

---

### Phase 2: Find the Cycle Entrance

- Reset the slow pointer to the beginning.
- Move both pointers one step at a time.
- The node where they meet again is the duplicate number.

---

## Example

Input

```text
nums = [1,3,4,2,2]
```

Traversal

```text
0 → 1 → 3 → 2 → 4
          ↑     ↓
          └─────┘
```

Cycle begins at **2**.

Output

```text
2
```

---

## Complexity Analysis

### Time Complexity

**O(n)**

Both phases together traverse the array only a constant number of times.

### Space Complexity

**O(1)**

Only two pointers are used.

---

## Key Learnings

- Floyd's Cycle Detection Algorithm
- Two Pointers
- Cycle Detection
- Linked List Interpretation of Arrays
- Constant Space Algorithms
- Mathematical Observation
