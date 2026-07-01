# 62. Unique Paths

## Problem Statement
A robot is located at the top-left corner of an `m x n` grid.

The robot wants to reach the bottom-right corner.

It can only move:
- Right
- Down

Return the total number of unique paths.

---

## Approach: Dynamic Programming

We use a DP grid where:

`dp[i][j]` = number of unique ways to reach cell `(i, j)`

---

## Key Observation

A cell can only be reached from:

- Top → `(i-1, j)`
- Left → `(i, j-1)`

Therefore:

dp[i][j] = dp[i-1][j] + dp[i][j-1]

---

## Base Case

First row:

Only move right → exactly 1 path

First column:

Only move down → exactly 1 path

So initialize all first-row and first-column cells as 1.

---

## Python Solution

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
```

---

## Dry Run

Input:

m = 3  
n = 7  

Initial DP:

1 1 1 1 1 1 1  
1 1 1 1 1 1 1  
1 1 1 1 1 1 1  

Update:

dp[1][1] = 1 + 1 = 2  
dp[1][2] = 2 + 1 = 3  
...

Final:

1 1 1 1 1 1 1  
1 2 3 4 5 6 7  
1 3 6 10 15 21 28  

Answer = 28

---

## Complexity Analysis

**Time Complexity:** O(m × n)

Each cell is visited once.

**Space Complexity:** O(m × n)

DP matrix stores all cells.

---

## Key Learnings
- Dynamic Programming
- Grid DP
- State Transition
- Tabulation
- Path Counting
