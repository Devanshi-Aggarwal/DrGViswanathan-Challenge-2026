# LeetCode 206 - Reverse Linked List

## Problem Statement

Given the head of a singly linked list, reverse the list and return the reversed linked list.

---

## Approach

I solved this problem using **Recursion**.

The idea is:

- If the list is empty or has only one node, return it directly.
- Recursively reverse the remaining list starting from `head.next`.
- After recursion returns, reverse the connection:
  - Make the next node point back to current node.
  - Break the original forward link.

This gradually reverses the entire linked list.

---

## Algorithm

1. Check base case:
   - If list is empty or has only one node, return head.
2. Recursively reverse the rest of the list.
3. Reverse the current node’s pointer.
4. Set current node’s next to `None`.
5. Return the new head.

---

## Dry Run

Input:

1 → 2 → 3 → 4 → 5

Recursive calls go until node 5.

While returning:

- 5 → 4
- 5 → 4 → 3
- 5 → 4 → 3 → 2
- 5 → 4 → 3 → 2 → 1

Output:

5 → 4 → 3 → 2 → 1

---

## Complexity Analysis

### Time Complexity

O(n)

Each node is visited once.

### Space Complexity

O(n)

Recursive call stack stores n function calls.

---

## Key Learning

This problem strengthened my understanding of:

- Linked List pointer manipulation
- Recursive thinking
- Base cases in recursion

Reversing links carefully is the key to avoiding broken pointers.

---

## Concepts Practiced

- Linked List
- Recursion
- Pointer Manipulation
