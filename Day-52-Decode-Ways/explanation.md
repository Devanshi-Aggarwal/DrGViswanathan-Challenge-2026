# 91. Decode Ways

## Difficulty
Medium

## Topics
- Dynamic Programming
- String
- DP Array
- State Transition

## Problem

A message containing letters from `A` to `Z` is encoded using the following mapping:

- `1` → `A`
- `2` → `B`
- ...
- `25` → `Y`
- `26` → `Z`

Given a string `s` containing only digits, the task is to return the number of different ways in which the string can be decoded.

A `0` cannot be decoded individually. It can only appear as part of a valid two-digit number such as `10` or `20`.

---

## Approach

I used Dynamic Programming to calculate the number of valid decoding combinations.

Let:

`f[i]` = number of ways to decode the first `i` characters of the string.

Initially:

```python
f = [1] + [0] * n
```

Here, `f[0] = 1` represents one way to decode an empty string.

For every character, there are two possibilities.

### 1. Single Digit Decoding

If the current character is not `0`, it can be decoded individually.

Therefore:

```python
f[i] = f[i - 1]
```

For example:

`2` can represent `B`.

---

### 2. Two Digit Decoding

We also check whether the current character and the previous character together form a valid number between `10` and `26`.

The conditions are:

```python
i > 1
s[i - 2] != "0"
int(s[i - 2:i]) <= 26
```

If the two-digit number is valid:

```python
f[i] += f[i - 2]
```

This adds all decoding possibilities that existed before these two digits.

---

## Example

For:

```text
s = "12"
```

There are two possible decodings:

```text
1 + 2 → A + B → AB
12    → L
```

Therefore:

```text
Output = 2
```

---

## Why Dynamic Programming?

At every position, the number of decoding possibilities depends on previously calculated states.

A character can either:

- form a valid single-digit decoding, or
- combine with the previous character to form a valid two-digit decoding.

Instead of repeatedly calculating the same possibilities, Dynamic Programming stores the results for previous positions and reuses them.

---

## Complexity

### Time Complexity

`O(n)`

The string is traversed once.

### Space Complexity

`O(n)`

A DP array of size `n + 1` is used to store the number of decoding possibilities.

---

## Key Takeaways

- Dynamic Programming
- String Processing
- State Transition
- Handling Edge Cases involving `0`
- Single-Digit and Two-Digit Decoding
- Reusing Previously Computed Results

---

## Status

✅ Accepted — 269 / 269 test cases passed
