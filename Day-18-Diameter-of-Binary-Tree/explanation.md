# LeetCode 543 — Diameter of Binary Tree

## Problem Statement
Given the root of a binary tree, return the **diameter** of the tree.

The diameter of a binary tree is the length of the **longest path between any two nodes** in the tree.

Important:
- The path may or may not pass through the root.
- Path length is measured in **number of edges**, not nodes.

---

## Approach Used: DFS + Height Calculation

A brute force idea would be:
- Calculate diameter for every node separately
- Recompute subtree heights repeatedly

That becomes inefficient.

Instead, we optimize using **single DFS traversal**.

---

## Core Idea

For every node:

Diameter passing through that node =

left subtree height + right subtree height

Why?

Because the longest path through a node goes:
- deepest node in left subtree
→ current node →
- deepest node in right subtree

So at every node:
1. Compute left height
2. Compute right height
3. Update global diameter

---

## Algorithm

1. Initialize answer = 0
2. Create recursive function to calculate height
3. For each node:
   - Get left height
   - Get right height
   - Update diameter with `left + right`
4. Return maximum diameter

---

## Python Solution

```python
class Solution:
    def diameterOfBinaryTree(self, root):
        ans = 0

        def maxDepth(root):
            nonlocal ans

            if not root:
                return 0

            l = maxDepth(root.left)
            r = maxDepth(root.right)

            ans = max(ans, l + r)
            return 1 + max(l, r)

        maxDepth(root)
        return ans
```

---

## Complexity Analysis

### Time Complexity
Each node visited once:

O(n)

---

### Space Complexity
Recursive stack:

O(h)

Where:
- h = tree height

Worst case:

O(n)

Balanced tree:

O(log n)

---

## Key Learning

This problem teaches an important tree pattern:

Sometimes while calculating one property (**height**),  
you can simultaneously solve another problem (**diameter**).

Concepts practiced:
- Binary Trees
- DFS
- Recursion
- Tree Height Calculation
- Bottom-Up Traversal
