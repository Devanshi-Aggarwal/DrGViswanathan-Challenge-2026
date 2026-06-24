# 19. Remove Nth Node From End of List

## Problem
Given the head of a linked list, remove the nth node from the end and return the head.

---

## Approach: Fast and Slow Pointer

We use two pointers:
- `fast`
- `slow`

### Key Idea
Maintain a gap of `n` nodes between fast and slow.

When fast reaches the last node:
- slow will stand right before the node to remove.

---

## Steps
1. Initialize slow and fast at head.
2. Move fast pointer n steps ahead.
3. If fast becomes null, remove head.
4. Move both pointers together.
5. Stop when fast reaches last node.
6. Remove target node using:
   slow.next = slow.next.next

---

## Python Solution

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
