# 383. Ransom Note

## Problem
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed using letters from `magazine`, otherwise return `false`.

Each letter in `magazine` can only be used once.

---

## Approach: Frequency Counting using Counter

We count how many times each character appears in:
- `ransomNote`
- `magazine`

Then we compare frequencies.

If any required character appears more times in `ransomNote` than in `magazine`, construction is impossible.

---

## Steps
1. Count characters in `ransomNote`.
2. Count characters in `magazine`.
3. Compare frequency of each lowercase character.
4. Return `False` if any frequency is insufficient.
5. Otherwise return `True`.

---

## Python Solution

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1 = collections.Counter(ransomNote)
        count2 = collections.Counter(magazine)
        return all(count1[c] <= count2[c] for c in string.ascii_lowercase)
```

---

## Complexity Analysis

**Time Complexity:** O(n + m)  
where:
- n = length of ransomNote
- m = length of magazine

**Space Complexity:** O(1)  
Only 26 lowercase English letters are stored.

---

## Key Learnings
- Hash Maps
- Frequency Counting
- Python Counter
- Character comparison
- Efficient lookup using dictionaries
