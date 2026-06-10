# LeetCode 155 - Min Stack

## Problem Statement

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

All operations must run in O(1) time complexity.

---

## Approach

I used a modified stack where each element stores:

- The actual value
- The minimum value present in the stack at that point

Instead of storing only the element, I store a pair:

```text
[value, current_min]
```

This allows the minimum element to be accessed directly from the top of the stack without traversing the entire stack.

---

## Algorithm

### Push

1. If the stack is empty, store `[value, value]`.
2. Otherwise, compare the current minimum with the new value.
3. Store `[value, min(current_min, value)]`.

### Pop

1. Remove the top element.

### Top

1. Return the value stored in the top pair.

### getMin

1. Return the minimum value stored in the top pair.

---

## Example

### Operations

```text
push(-2)
push(0)
push(-3)
getMin()
pop()
top()
getMin()
```

### Output

```text
-3
0
-2
```

### Explanation

Stack after pushes:

```text
[-2, -2]
[0, -2]
[-3, -3]
```

The minimum value is always stored alongside each element.

---

## Complexity Analysis

### Time Complexity

Push: O(1)

Pop: O(1)

Top: O(1)

getMin: O(1)

### Space Complexity

O(n)

Additional space is used to store the minimum value alongside each element.

---

## Key Learning

Sometimes storing extra information can significantly improve efficiency.

By maintaining the minimum value at every stack level, we can retrieve the minimum element in constant time without searching through the stack.

---

## Concepts Practiced

- Stack
- Design Problems
- Constant Time Operations
- Data Structures
- Space-Time Tradeoff
