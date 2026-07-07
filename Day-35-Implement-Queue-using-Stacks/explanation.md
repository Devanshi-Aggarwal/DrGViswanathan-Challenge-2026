# 232. Implement Queue using Stacks

## Problem Statement

Implement a First-In-First-Out (FIFO) queue using only two stacks.

The queue should support:

- push(x)
- pop()
- peek()
- empty()

Only standard stack operations are allowed.

---

## Approach

A queue follows **FIFO (First In First Out)** while a stack follows **LIFO (Last In First Out)**.

To simulate a queue using stacks:

- Use one stack (`stk1`) for inserting elements.
- Use another stack (`stk2`) for removing elements.

Whenever `stk2` becomes empty and a pop/peek operation is requested:

- Move every element from `stk1` to `stk2`.
- This reverses the order.
- The oldest inserted element becomes the top of `stk2`.

Thus FIFO behavior is achieved.

---

## Algorithm

### Push

- Insert the new element into `stk1`.

### Pop

- If `stk2` is empty:
  - Move all elements from `stk1` to `stk2`.
- Pop the top of `stk2`.

### Peek

- If `stk2` is empty:
  - Move all elements from `stk1` to `stk2`.
- Return the top element of `stk2`.

### Empty

Return `True` if both stacks are empty.

---

## Example

Operations:

```text
push(1)
push(2)
peek()
pop()
empty()
```

Execution:

```text
stk1 = []
stk2 = []

push(1)

stk1 = [1]
stk2 = []

push(2)

stk1 = [1, 2]
stk2 = []

peek()

Move elements:

stk1 -> stk2

stk1 = []
stk2 = [2, 1]

Front = 1

pop()

Remove 1

stk2 = [2]

empty()

False
```

Output:

```text
[null, null, null, 1, 1, false]
```

---

## Complexity Analysis

- **Push:** O(1)
- **Pop:** Amortized O(1)
- **Peek:** Amortized O(1)
- **Empty:** O(1)

### Space Complexity

**O(n)**

where **n** is the number of elements stored.

---

## Key Learnings

- Queue implementation using stacks
- Lazy transfer technique
- FIFO using LIFO
- Amortized analysis
- Stack operations
- Data structure implementation
