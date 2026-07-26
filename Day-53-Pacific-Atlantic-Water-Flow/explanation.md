# 417. Pacific Atlantic Water Flow

## Difficulty
Medium

## Topics
- Graph
- Breadth-First Search (BFS)
- Matrix Traversal
- Multi-Source BFS
- Reverse Traversal

## Problem

We are given an `m x n` matrix `heights`, where each value represents the height of a cell.

The Pacific Ocean touches the top and left edges of the matrix, while the Atlantic Ocean touches the bottom and right edges.

Water can flow from a cell to another adjacent cell if the neighboring cell has a height less than or equal to the current cell.

The goal is to find all cells from which water can eventually flow to both the Pacific and Atlantic oceans.

---

## Approach

Instead of checking every cell individually to determine whether it can reach both oceans, we reverse the direction of the problem.

We start from the ocean boundaries and determine which cells can reach each ocean.

This allows us to use Multi-Source BFS.

We perform two separate BFS traversals:

1. BFS starting from all cells touching the Pacific Ocean.
2. BFS starting from all cells touching the Atlantic Ocean.

---

## Pacific Starting Cells

The Pacific Ocean touches:

- Top row
- Left column

Therefore, all cells along these boundaries are initially added to the Pacific queue.

```python
for i in range(m):
    qP.append((i, 0))

for j in range(n):
    qP.append((0, j))
```

---

## Atlantic Starting Cells

The Atlantic Ocean touches:

- Bottom row
- Right column

Therefore:

```python
for i in range(m):
    qA.append((i, n - 1))

for j in range(n):
    qA.append((m - 1, j))
```

---

## Reverse Water Flow

Normally, water flows from a higher or equal cell to a lower cell.

Since we are starting from the oceans and moving backwards, we can move from the current cell to a neighboring cell only when:

```python
heights[x][y] >= heights[i][j]
```

In the implementation, this is handled by skipping cells where:

```python
heights[x][y] < h
```

This allows us to find every cell from which water could have flowed toward that ocean.

---

## BFS Traversal

For every cell removed from the queue:

1. Check its four neighboring cells.
2. Ignore cells outside the grid.
3. Ignore cells already visited.
4. Ignore neighboring cells with a smaller height.
5. Mark valid cells as reachable.
6. Add them to the BFS queue.

Two visited matrices are maintained:

```python
seenP
seenA
```

`seenP[i][j]` indicates that the cell can reach the Pacific Ocean.

`seenA[i][j]` indicates that the cell can reach the Atlantic Ocean.

---

## Finding the Final Answer

After both BFS traversals, a cell belongs in the answer if it is reachable from both oceans.

```python
if seenP[i][j] and seenA[i][j]
```

Therefore, the final answer is the intersection of the Pacific-reachable and Atlantic-reachable cells.

---

## Why This Approach?

A direct approach could start BFS/DFS from every individual cell and check whether it reaches both oceans.

That would repeat a large amount of work.

Instead, starting simultaneously from the ocean boundaries allows every cell to be processed only a constant number of times.

This makes the solution much more efficient.

---

## Complexity

### Time Complexity

`O(m × n)`

Each cell is visited at most once during the Pacific BFS and once during the Atlantic BFS.

### Space Complexity

`O(m × n)`

Two visited matrices and BFS queues are maintained.

---

## Key Takeaways

- Multi-Source BFS
- Graph Traversal on a Matrix
- Reverse Traversal
- BFS Queue
- Visited Matrix
- Four-Directional Grid Traversal
- Finding Intersection of Reachable Cells

---

## Status

✅ Accepted — 114 / 114 test cases passed
