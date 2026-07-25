# 200. Number of Islands

## Problem Statement

Given an `m x n` 2D binary grid containing:

- `'1'` representing land
- `'0'` representing water

Return the **number of islands** present in the grid.

An island is formed by connecting adjacent land cells horizontally or vertically.

Diagonal cells are not considered connected.

---

## Approach

We can solve this problem using **Depth First Search (DFS)**.

The main idea is:

Whenever we encounter an unvisited land cell (`'1'`), we have discovered a new island.

We then perform DFS starting from that cell and visit every land cell connected to it.

While visiting a land cell, we change it from `'1'` to `'0'`. This marks the cell as visited and prevents us from counting the same island again.

Therefore, every time DFS is started from the main grid traversal, we increment the island count.

---

## Algorithm

1. Initialize `ans = 0` to store the number of islands.

2. Traverse every cell in the grid.

3. If the current cell contains `'1'`:
   - A new island has been discovered.
   - Perform DFS from that cell.
   - Increment `ans` by `1`.

4. During DFS:
   - Change the current land cell from `'1'` to `'0'`.
   - Check its four neighboring cells:
     - Up
     - Right
     - Down
     - Left
   - If a neighboring cell is inside the grid and contains `'1'`, recursively perform DFS on it.

5. Return `ans`.

---

## Direction Array

The following direction array is used:

```python
dirs = (-1, 0, 1, 0, -1)
```

Using consecutive pairs gives:

```text
(-1, 0) → Up
(0, 1)  → Right
(1, 0)  → Down
(0, -1) → Left
```

This allows us to explore all four neighboring cells efficiently.

---

## Example

### Input

```text
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
```

There are three separate connected groups of land:

```text
1 1 0 0 0
1 1 0 0 0

0 0 1 0 0

0 0 0 1 1
```

Therefore:

```text
Output = 3
```

---

## Why DFS Works

When DFS starts from a land cell, it explores every land cell connected to it.

All those cells belong to the same island.

By changing visited land cells from `'1'` to `'0'`, we ensure that the same island is never counted again.

Therefore, the number of times we start a new DFS represents the total number of islands.

---

## Complexity Analysis

### Time Complexity

**O(m × n)**

Every cell in the grid is visited at most once.

Here:

- `m` = number of rows
- `n` = number of columns

### Space Complexity

**O(m × n)** in the worst case.

The recursive DFS call stack may contain a large number of cells if most of the grid consists of connected land.

---

## Key Learnings

- Depth First Search (DFS)
- Graph Traversal
- Matrix Traversal
- Flood Fill
- Connected Components
- Grid Problems
- Recursive Traversal
- In-place Visited Marking
