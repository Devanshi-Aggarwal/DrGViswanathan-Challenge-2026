# 3. Longest Substring Without Repeating Characters — Explanation

## Problem Statement

Given a string `s`, return the **length of the longest substring without repeating characters**.

A **substring** consists of consecutive characters.

---

## Approach Used: Sliding Window + Hash Map (Counter)

We maintain a sliding window using two pointers:

- `l` → Left pointer
- `r` → Right pointer

We also use a **Counter** to store the frequency of characters currently inside the window.

Whenever a duplicate character appears, we keep moving the left pointer until the duplicate is removed.

Throughout the traversal, we continuously update the maximum window size.

---

## Python Solution

```python
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = Counter()
        ans = l = 0

        for r, c in enumerate(s):
            cnt[c] += 1

            while cnt[c] > 1:
                cnt[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```

---

# Dry Run

### Example

```text
Input:

s = "abcabcbb"
```

---

### Step 1

Window:

```text
[a]
```

Unique characters.

Length = 1

Maximum = 1

---

### Step 2

Window:

```text
[a b]
```

Length = 2

Maximum = 2

---

### Step 3

Window:

```text
[a b c]
```

Length = 3

Maximum = 3

---

### Step 4

Next character = a

Window becomes

```text
[a b c a]
```

Duplicate found.

Move left pointer.

Remove first 'a'

Window becomes

```text
[b c a]
```

Length = 3

Maximum remains 3

---

### Step 5

Next character = b

Window:

```text
[b c a b]
```

Duplicate again.

Move left pointer.

Window becomes

```text
[c a b]
```

Length = 3

---

### Step 6

Next character = c

Window

```text
[c a b c]
```

Duplicate.

Move left pointer.

Window becomes

```text
[a b c]
```

Length = 3

---

### Step 7

Next character = b

Window

```text
[a b c b]
```

Duplicate.

Move left pointer.

Window becomes

```text
[c b]
```

---

### Step 8

Next character = b

Window

```text
[c b b]
```

Duplicate.

Move left pointer twice.

Window becomes

```text
[b]
```

---

Longest window encountered:

```text
abc
```

Length:

```text
3
```

Therefore,

# Answer = 3 ✅

---

## Time Complexity

Each character enters and leaves the sliding window at most once.

```text
O(N)
```

where **N = length of string**

---

## Space Complexity

Counter stores at most all unique characters.

```text
O(K)
```

where **K = number of distinct characters**

Worst case:

```text
O(N)
```

---

## Key Concepts Learned

- Sliding Window
- Two Pointers
- Hash Map
- Python Counter
- Character Frequency Counting
- Window Shrinking
- Duplicate Removal
- Longest Substring
