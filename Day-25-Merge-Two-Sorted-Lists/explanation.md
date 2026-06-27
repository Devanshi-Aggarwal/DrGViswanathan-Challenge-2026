# 21. Merge Two Sorted Lists

## Problem
You are given the heads of two sorted linked lists.

Merge both lists into one sorted linked list and return its head.

---

## Approach: Recursive Merge

Since both linked lists are already sorted:

- Compare current nodes
- Choose smaller node
- Recursively merge remaining nodes

This guarantees sorted order.

---

## Key Idea

At every step:

- If `list1.val <= list2.val`
  - choose `list1`
- Else
  - choose `list2`

Attach recursive result to chosen node.

---

## Base Case

If one list becomes empty:

```python
return list1 or list2
```

Return whichever list still has nodes.

---

## Python Solution

```python
class Solution:
    def mergeTwoLists(self, list1, list2):

        if list1 is None or list2 is None:
            return list1 or list2

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
```

---

## Dry Run

Input:

list1 = [1,2,4]
list2 = [1,3,4]

Comparison:

1 vs 1 → pick list1  
2 vs 1 → pick list2  
2 vs 3 → pick list1  
4 vs 3 → pick list2  
4 vs 4 → pick list1  
remaining 4 → attach

Output:

[1,1,2,3,4,4]

---

## Complexity Analysis

**Time Complexity:** O(n + m)

Each node is visited once.

**Space Complexity:** O(n + m)

Due to recursive calls.

---

## Key Learnings
- Linked List Traversal
- Recursive Merging
- Sorted Data Processing
- Divide and Merge Logic
