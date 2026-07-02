# 112. Path Sum

## Problem Statement
Given the root of a binary tree and an integer `targetSum`, determine if the tree has a **root-to-leaf path** such that the sum of node values equals `targetSum`.

A leaf node is a node with no children.

---

## Approach: Depth First Search (DFS)

We use DFS to explore every root-to-leaf path.

At each node:
1. Add current node value to running sum
2. If node is a leaf:
   - Check if running sum equals targetSum
3. Otherwise recursively explore left and right subtrees

---

## Key Observation

We need to check **complete root-to-leaf paths**, not partial paths.

That means:
- Reaching target sum before leaf node does **not** count.

---

## Python Solution

```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, s):
            if root is None:
                return False

            s += root.val

            if root.left is None and root.right is None and s == targetSum:
                return True

            return dfs(root.left, s) or dfs(root.right, s)

        return dfs(root, 0)
```

---

## Dry Run

Input:

Tree:
        5
       / \
      4   8
     /   / \
   11   13  4
   / \        \
  7   2        1

targetSum = 22

Path checked:

5 → 4 → 11 → 2

Sum:

5 + 4 + 11 + 2 = 22

Since this is a root-to-leaf path, answer is:

True

---

## Complexity Analysis

**Time Complexity:** O(n)

Every node is visited once.

**Space Complexity:** O(h)

Where h is tree height due to recursion stack.

Worst case skewed tree → O(n)

Balanced tree → O(log n)

---

## Key Learnings
- Tree DFS
- Root-to-Leaf Traversal
- Running Sum Technique
- Recursive Backtracking
- Leaf Node Validation
