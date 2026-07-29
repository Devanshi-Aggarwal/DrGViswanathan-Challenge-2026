# 994. Rotting Oranges

## Difficulty

Medium

---

## Topics

- Breadth First Search (BFS)
- Queue
- Matrix Traversal
- Multi-Source BFS
- Simulation

---

## Problem

You are given an `m × n` grid where:

- `0` → Empty Cell
- `1` → Fresh Orange
- `2` → Rotten Orange

Every minute, every fresh orange adjacent (up, down, left, right) to a rotten orange also becomes rotten.

Return the minimum number of minutes required until no fresh orange remains.

If it is impossible, return **-1**.

---

# Approach

This problem is solved using **Multi-Source Breadth First Search (BFS).**

Instead of starting BFS from one cell, we begin from **all initially rotten oranges simultaneously.**

Each BFS level represents **one minute**.

---

# Step 1 — Initialize Variables

Store the grid dimensions.

```python
m, n = len(grid), len(grid[0])
```

Maintain

- queue of rotten oranges
- count of fresh oranges

```python
cnt = 0
q = deque()
```

---

# Step 2 — Scan the Grid

Traverse every cell.

If an orange is rotten,

```python
q.append((i, j))
```

store its position.

If it is fresh,

```python
cnt += 1
```

increase the fresh orange count.

---

# Step 3 — Direction Array

Movement is allowed in four directions.

```python
dirs = (-1, 0, 1, 0, -1)
```

Using

```python
pairwise(dirs)
```

produces

```
(-1,0)
(0,1)
(1,0)
(0,-1)
```

---

# Step 4 — Perform Multi-Source BFS

While

- rotten oranges exist in the queue
- fresh oranges are still remaining

```python
while q and cnt:
```

each iteration represents one minute.

```python
ans += 1
```

---

# Step 5 — Process Current Level

Process only the oranges that were rotten at the beginning of the minute.

```python
for _ in range(len(q)):
```

Remove one rotten orange.

```python
i, j = q.popleft()
```

---

# Step 6 — Infect Adjacent Fresh Oranges

Visit all four neighboring cells.

If a neighbor contains a fresh orange,

```python
grid[x][y] = 2
```

mark it rotten,

add it to the queue,

```python
q.append((x, y))
```

and decrease the remaining fresh count.

```python
cnt -= 1
```

---

# Step 7 — Finish Early

If every fresh orange has become rotten,

```python
if cnt == 0:
    return ans
```

return the total minutes immediately.

---

# Step 8 — Final Answer

If fresh oranges still remain,

```python
return -1
```

Otherwise,

return

```python
0
```

when there were no fresh oranges initially.

---

# Example

Initial Grid

```
2 1 1
1 1 0
0 1 1
```

Minute 0

```
2 1 1
1 1 0
0 1 1
```

Minute 1

```
2 2 1
2 1 0
0 1 1
```

Minute 2

```
2 2 2
2 2 0
0 1 1
```

Minute 3

```
2 2 2
2 2 0
0 2 1
```

Minute 4

```
2 2 2
2 2 0
0 2 2
```

Answer = **4**

---

# Why Multi-Source BFS?

All rotten oranges spread infection **simultaneously**.

Processing all rotten oranges at the same BFS level perfectly models one minute passing.

---

# Complexity Analysis

### Time Complexity

O(m × n)

Each cell is processed at most once.

---

### Space Complexity

O(m × n)

The queue may contain every cell in the worst case.

---

# Key Takeaways

- Breadth First Search
- Multi-Source BFS
- Queue
- Matrix Traversal
- Simulation
- Level Order Processing
- Grid Problems

---

# Status

✅ Accepted — 307 / 307 test cases passed
