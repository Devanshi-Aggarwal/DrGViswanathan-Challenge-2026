# 744. Find Smallest Letter Greater Than Target

## Problem Statement

Given a sorted array of characters `letters` and a target character `target`, return the smallest character in the array that is lexicographically greater than the target.

If such a character does not exist, return the first character in the array (the letters wrap around).

---

## Approach

This solution uses **Binary Search** with Python's `bisect_right()` function.

### Key Observations

- The array is already sorted.
- We need the first element strictly greater than the target.
- `bisect_right()` directly returns the insertion position after all occurrences of the target.
- If the insertion index reaches the end of the array, we wrap around using the modulo operator.

---

## Algorithm

1. Perform `bisect_right()` on the sorted array.
2. Obtain the insertion index for the target.
3. Apply modulo with the array length to handle wrap-around.
4. Return the character at the computed index.

---

## Example

Input

```text
letters = ["c","f","j"]
target = "c"
```

Binary Search returns index:

```text
2
```

Answer:

```text
letters[1] = "f"
```

Output

```text
"f"
```

---

## Complexity Analysis

### Time Complexity

**O(log n)**

Binary Search is performed once.

### Space Complexity

**O(1)**

Only a constant amount of extra space is used.

---

## Key Learnings

- Binary Search
- Python bisect_right()
- Sorted Array Search
- Upper Bound Search
- Wrap-around using Modulo
- Logarithmic Search Optimization
