# 733. Flood Fill

## Problem
You are given a 2D grid representing an image.

Each cell contains a pixel color value.

Starting from pixel `(sr, sc)`, change that pixel and all connected pixels having the same original color into `newColor`.

Connected means:
- Up
- Down
- Left
- Right

Diagonal cells are **not connected**.

---

## Approach: Depth First Search (DFS)

We perform DFS starting from the source pixel.

### Steps:
1. Store original color of starting pixel
2. Recursively visit neighboring cells
3. Only process cells if:
   - inside boundaries
   - same as original color
   - not visited before
4. Paint them with `newColor`

---

## Key Idea

This problem is basically:

**Find connected component → recolor it**

DFS is ideal for exploring connected regions in grids.

---

## Python Solution

```python
class Solution:
    def floodFill(self, image: list[list[int]], 
                  sr: int, sc: int, newColor: int) -> list[list[int]]:
        startColor = image[sr][sc]
        seen = set()

        def dfs(i, j):
            if i < 0 or i == len(image) or j < 0 or j == len(image[0]):
                return

            if image[i][j] != startColor or (i, j) in seen:
                return

            image[i][j] = newColor
            seen.add((i, j))

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        dfs(sr, sc)
        return image
```

---

## Dry Run

Input:

image =  
[[1,1,1],  
 [1,1,0],  
 [1,0,1]]

sr = 1  
sc = 1  
newColor = 2  

Starting color = 1

DFS recolors all connected `1`s.

Final image:

[[2,2,2],  
 [2,2,0],  
 [2,0,1]]

---

## Complexity Analysis

**Time Complexity:** O(m × n)

Each cell is visited at most once.

**Space Complexity:** O(m × n)

For recursion stack and visited set.

---

## Key Learnings
- Graph Traversal
- DFS on Grid
- Matrix Boundary Checking
- Connected Component Detection
- Recursive Flood Fill
