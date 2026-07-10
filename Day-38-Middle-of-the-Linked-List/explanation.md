# 876. Middle of the Linked List

## Problem Statement

Given the `head` of a singly linked list, return the **middle node** of the linked list.

If there are two middle nodes, return the **second middle node**.

---

## Approach

This solution uses the **Fast & Slow Pointer** technique.

- Initialize two pointers:
  - `slow`
  - `fast`
- Both start from the head.
- Move:
  - `slow` one step at a time.
  - `fast` two steps at a time.
- When `fast` reaches the end of the list, `slow` will be positioned at the middle node.

If the list contains an even number of nodes, this naturally returns the **second middle node**, as required.

---

## Algorithm

1. Initialize both `slow` and `fast` at the head.
2. While `fast` and `fast.next` exist:
   - Move `slow` one node forward.
   - Move `fast` two nodes forward.
3. Return `slow`.

---

## Example

Input:

```text
1 → 2 → 3 → 4 → 5
```

Traversal:

```text
Step 1:
slow → 2
fast → 3

Step 2:
slow → 3
fast → 5

fast reaches the end.
```

Output:

```text
3 → 4 → 5
```

---

## Complexity Analysis

### Time Complexity

**O(n)**

The list is traversed only once.

### Space Complexity

**O(1)**

Only two pointers are used.

---

## Key Learnings

- Linked List
- Fast & Slow Pointer
- Two Pointer Technique
- One Pass Traversal
- Middle Node Detection
- Constant Space Optimization
