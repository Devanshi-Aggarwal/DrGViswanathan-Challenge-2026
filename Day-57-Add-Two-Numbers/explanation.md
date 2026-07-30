# 2. Add Two Numbers

## Difficulty

Medium

---

## Topics

- Linked List
- Simulation
- Carry Handling
- Math
- Iteration

---

## Problem

You are given two non-empty linked lists representing two non-negative integers.

- The digits are stored in **reverse order**.
- Each node contains a single digit.
- Return the sum as a linked list in the same reverse order.

---

# Approach

The solution simulates the way we perform addition by hand.

We traverse both linked lists simultaneously while maintaining a **carry** value from the previous digit.

A dummy node is used to simplify construction of the resulting linked list.

---

# Step 1 — Create a Dummy Node

A dummy node serves as the head of the answer list.

```python
dummy = ListNode(0)
curr = dummy
```

All new nodes are attached after this node.

---

# Step 2 — Initialize Carry

Initially,

```python
carry = 0
```

There is no carry.

---

# Step 3 — Traverse Both Lists

Continue while

- first list has nodes
- second list has nodes
- or a carry still exists

```python
while carry or l1 or l2:
```

This also handles the final carry automatically.

---

# Step 4 — Add Current Digits

If the first list still has nodes,

```python
carry += l1.val
```

Move to the next node.

```python
l1 = l1.next
```

Do the same for the second list.

---

# Step 5 — Create New Digit

The current digit is

```python
carry % 10
```

Create a new node.

```python
curr.next = ListNode(carry % 10)
```

---

# Step 6 — Update Carry

The remaining carry becomes

```python
carry //= 10
```

This is either 0 or 1.

---

# Step 7 — Move Forward

Advance the answer pointer.

```python
curr = curr.next
```

Repeat until both lists and carry are exhausted.

---

# Step 8 — Return Answer

The first node is a dummy.

Return

```python
dummy.next
```

---

# Example

Input

```
l1 = 2 → 4 → 3
l2 = 5 → 6 → 4
```

Step-by-step

```
2 + 5 = 7

4 + 6 = 10
Digit = 0
Carry = 1

3 + 4 + 1 = 8
```

Output

```
7 → 0 → 8
```

---

# Why Dummy Node?

Without a dummy node,

the first insertion requires special handling.

A dummy node keeps the implementation clean and avoids edge cases.

---

# Complexity Analysis

### Time Complexity

O(max(n, m))

where

- n = length of first list
- m = length of second list

Each node is visited exactly once.

---

### Space Complexity

O(max(n, m))

Only the output linked list occupies extra space.

---

# Key Takeaways

- Linked List Traversal
- Carry Handling
- Simulation
- Dummy Node
- Digit-by-Digit Addition
- Iteration

---

# Status

✅ Accepted — 1569 / 1569 test cases passed
