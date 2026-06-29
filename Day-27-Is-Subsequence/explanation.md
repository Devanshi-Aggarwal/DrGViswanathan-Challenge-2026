# 392. Is Subsequence

## Problem
Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, otherwise return `false`.

A subsequence is formed by deleting some (or no) characters from a string without changing the order of the remaining characters.

---

## Approach: Two Pointer Traversal

We use one pointer to track string `s`.

Then we scan through `t`:

- If current character matches `s[i]`, move pointer in `s`
- Continue scanning `t`
- If all characters of `s` are matched, return `True`

---

## Key Idea

Subsequence means:

- Order matters ✅
- Continuity does NOT matter ❌

Example:

`abc` is a subsequence of `ahbgdc`

Because:
- a found
- b found later
- c found later

Order is preserved.

---

## Python Solution

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        i = 0

        for c in t:
            if s[i] == c:
                i += 1
                if i == len(s):
                    return True

        return False
```

---

## Dry Run

Input:

s = "abc"  
t = "ahbgdc"

Traversal:

a → match → i=1  
h → skip  
b → match → i=2  
g → skip  
d → skip  
c → match → i=3  

All characters matched.

Output:

True

---

## Complexity Analysis

**Time Complexity:** O(len(t))

We traverse `t` once.

**Space Complexity:** O(1)

Only one pointer is used.

---

## Key Learnings
- Two Pointer Technique
- String Traversal
- Subsequence Matching
- Ordered Character Validation
