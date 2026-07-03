# 242. Valid Anagram - Explanation

## Problem Statement
Given two strings `s` and `t`, return **true** if `t` is an **anagram** of `s`, and **false** otherwise.

An **anagram** means both strings contain the exact same characters with the exact same frequencies, only the order may differ.

---

## Approach Used: Character Frequency Counting

We use Python’s **Counter** from the `collections` module.

### Steps:
1. First check if lengths of both strings are equal.
   - If lengths differ, they can never be anagrams.

2. Count frequency of each character in string `s`.

3. Subtract frequency of characters from string `t`.

4. If all final frequencies become `0`, both strings are anagrams.

---

## Python Solution

```python
import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = collections.Counter(s)
        count.subtract(collections.Counter(t))
        return all(freq == 0 for freq in count.values())
```

---

## Dry Run

### Example 1
```text
s = "anagram"
t = "nagaram"
```

### Step 1: Length Check
```text
len(s) = 7
len(t) = 7
```

Lengths match → Continue.

---

### Step 2: Count characters in s

```text
a → 3
n → 1
g → 1
r → 1
m → 1
```

Counter:

```python
{'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
```

---

### Step 3: Subtract counts of t

Characters in `"nagaram"`:

```text
n → -1
a → -3
g → -1
r → -1
m → -1
```

After subtraction:

```python
{'a': 0, 'n': 0, 'g': 0, 'r': 0, 'm': 0}
```

---

### Step 4: Check all values

```python
all(freq == 0 for freq in count.values())
```

Result:

```text
True
```

So:

# Answer = True 

---

## Example 2

```text
s = "rat"
t = "car"
```

Counter of `"rat"`:

```text
r → 1
a → 1
t → 1
```

Subtract `"car"`:

```text
c reduces (not present)
a reduces
r reduces
```

Remaining:

```text
t = 1
c = -1
```

Not all values are zero.

# Answer = False 

---

## Time Complexity

Counter creation:

```text
O(N)
```

Subtraction:

```text
O(N)
```

Total:

```text
O(N)
```

where **N = length of string**

---

## Space Complexity

We store character frequencies.

```text
O(K)
```

where **K = number of unique characters**

Worst case:

```text
O(N)
```

---

## Key Concepts Learned
- Hash Map
- Character Frequency Counting
- Python Counter
- String Comparison
- Frequency Matching
