# 141. Linked List Cycle

## Problem

Given the `head` of a linked list, determine whether the linked list contains a cycle.

A cycle exists if some node can be reached again by continuously following the `next` pointer.

---

## Approach: Hash Set

We use a **set** to store all visited nodes.

### Steps

1. Initialize an empty set.
2. Traverse the linked list.
3. Check whether current node already exists in the set.

   * If yes → cycle detected.
4. Otherwise add node to set.
5. Continue traversal.
6. If traversal reaches `None`, no cycle exists.

---

## Why This Works

* In a normal linked list, every node appears only once.
* In a cyclic linked list, some node repeats.
* Repeated node means we entered a loop.

---

## Python Solution

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()

        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next

        return False
```

---

## Complexity Analysis

**Time Complexity:** `O(n)`
Each node is visited once.

**Space Complexity:** `O(n)`
Set stores visited nodes.

---

## Key Learning

* Cycle detection in linked lists
* Hashing for repeated node detection
* Linked list traversal
