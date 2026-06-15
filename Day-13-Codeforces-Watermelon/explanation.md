# Codeforces 4A - Watermelon

## Problem Statement

Pete and Billy bought a watermelon of weight `w`.

They want to divide it into **two positive parts**, such that:

- Both parts have **even weights**
- Each part must have **positive weight**

We need to determine whether such a division is possible.

---

## Approach

To split the watermelon into two even positive parts:

- The total weight must be even
- The weight must be greater than 2

Why?

- 2 cannot be split into two positive even numbers
- 4 can be split into 2 + 2
- 6 can be split into 2 + 4
- 8 can be split into 2 + 6

So if `w > 2` and `w` is even, answer is **YES**.

Otherwise, answer is **NO**.

---

## Logic Used in Code

I checked whether:

- `n - 2` is even
- `n - 2 > 0`

This ensures that after giving one person 2 kg, the remaining weight is still positive and even.

If both conditions are true:

Return **YES**

Else:

Return **NO**

---

## Dry Run

### Input:
8

Possible split:

2 + 6

Both are positive and even.

Output:

YES

---

### Input:
3

Cannot split into two even parts.

Output:

NO

---

## Complexity Analysis

### Time Complexity
O(1)

Only one check is performed.

### Space Complexity
O(1)

No extra space used.

---

## Key Learning

This problem taught me:

- Competitive programming observation skills
- Importance of edge cases
- Simple math-based optimization
