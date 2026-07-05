# LeetCode 463. Island Perimeter - Explanation

## Problem Statement

Given a grid where:

- `1` represents land
- `0` represents water

Return the perimeter of the island.

There is exactly one island.

---

## Intuition

Every land cell has **4 edges**.

Whenever two land cells touch, they share one edge.

That shared edge removes **2 sides** from the total perimeter.

So instead of counting exposed edges individually, we calculate:

```
Perimeter = (Land Cells × 4) − (Shared Edges × 2)
```

---

## Dry Run

### Input

```
grid =

[
 [0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]
]
```

---

### Step 1

Count all land cells.

```
Total land cells = 7
```

Contribution:

```
7 × 4 = 28
```

---

### Step 2

Count shared edges.

We only check **Right** and **Down** neighbors.

Shared edges are:

```
(0,1) ↕ (1,1)

(1,0) → (1,1)

(1,1) → (1,2)

(1,1) ↕ (2,1)

(2,1) ↕ (3,1)

(3,0) → (3,1)
```

Total shared edges:

```
6
```

---

### Step 3

Each shared edge removes two sides.

```
Perimeter

= 28 − (6 × 2)

= 16
```

---

## Output

```
16
```

---

## Why only check Right and Down?

If we checked all four directions, every shared edge would be counted twice.

Checking only:

- Right
- Down

ensures every shared edge is counted exactly once.

---

## Complexity Analysis

### Time Complexity

```
O(m × n)
```

Every cell is visited once.

---

### Space Complexity

```
O(1)
```

No extra data structures are used.

---

## Key Concepts Learned

- Matrix Traversal
- Grid Problems
- Geometry-Based Counting
- Neighbor Detection
- Constant Space Solution
- Optimization by Avoiding Double Counting
