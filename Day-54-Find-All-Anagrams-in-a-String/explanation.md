# 438. Find All Anagrams in a String

## Difficulty
Medium

## Topics
- Sliding Window
- Hash Map
- Frequency Counting
- String
- Counter

## Problem

Given two strings `s` and `p`, return an array containing all the starting indices of substrings in `s` that are anagrams of `p`.

An anagram contains exactly the same characters with the same frequencies, but the characters may appear in a different order.

---

## Approach

The problem can be solved efficiently using a **Sliding Window** combined with **character frequency counting**.

Instead of generating every substring of length `len(p)` and checking whether it is an anagram, we maintain a moving window over `s`.

We use:

```python
count = collections.Counter(p)
```

to store the frequency of each character required from `p`.

We also maintain:

```python
required = len(p)
```

which represents how many characters are still required for the current window to form an anagram.

---

## Step 1: Expand the Window

We iterate through `s` using the right pointer `r`.

```python
for r, c in enumerate(s):
```

Whenever a character enters the window, its frequency is decreased:

```python
count[c] -= 1
```

If the character was still required:

```python
if count[c] >= 0:
    required -= 1
```

This means we successfully matched one of the characters needed for `p`.

---

## Step 2: Maintain the Window Size

The window must always have a maximum size of `len(p)`.

Once the right pointer moves beyond that size:

```python
if r >= len(p):
```

the leftmost character must leave the window.

Its frequency is restored:

```python
count[s[r - len(p)]] += 1
```

If the restored frequency becomes positive:

```python
if count[s[r - len(p)]] > 0:
    required += 1
```

it means the removed character was necessary for forming an anagram, so it becomes required again.

---

## Step 3: Detect an Anagram

Whenever:

```python
required == 0
```

all characters required by `p` are present in the current window.

Therefore, the current window is an anagram of `p`.

Its starting index is:

```python
r - len(p) + 1
```

and we add it to the answer:

```python
ans.append(r - len(p) + 1)
```

---

## Example

Consider:

```text
s = "cbaebabacd"
p = "abc"
```

The required window size is `3`.

Valid windows include:

```text
"cba" → index 0
"bac" → index 6
```

Both contain exactly the characters:

```text
a, b, c
```

Therefore:

```text
Output: [0, 6]
```

---

## Why Sliding Window?

A brute-force solution could examine every substring of length `len(p)` and calculate its character frequencies repeatedly.

The sliding window avoids recalculating frequencies from scratch.

When the window moves:

- One character enters.
- One character leaves.
- The frequency information is updated in constant time.

This makes the solution much more efficient.

---

## Complexity

### Time Complexity

`O(n)`

where `n` is the length of `s`.

Each character enters and leaves the sliding window at most once.

### Space Complexity

`O(k)`

where `k` is the number of distinct characters stored in the frequency counter.

Since the problem uses lowercase English letters, this is effectively constant auxiliary space.

---

## Key Takeaways

- Sliding Window
- Frequency Counting
- Hash Map / Counter
- Fixed-Size Window
- Efficient String Traversal
- Tracking Required Characters
- Avoiding Repeated Frequency Calculations

---

## Status

✅ Accepted — 65 / 65 test cases passed
