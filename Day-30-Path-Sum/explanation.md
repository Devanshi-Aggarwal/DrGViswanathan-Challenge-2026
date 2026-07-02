# 112. Path Sum — Explanation

## Problem Statement
Given the `root` of a binary tree and an integer `targetSum`, return **true** if the tree has a **root-to-leaf path** such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no left or right child.

---

## Approach Used: Depth First Search (DFS)

We use **DFS (Depth First Search)** with **recursion** to explore every possible root-to-leaf path.

At each node:
1. Add current node’s value to the running sum.
2. Check if current node is a leaf node.
3. If it is a leaf and sum equals `targetSum`, return `True`.
4. Otherwise, recursively check left and right subtrees.

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

### Input
```text
root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
targetSum = 22
```

### Tree Representation

```text
        5
       / \
      4   8
     /   / \
   11   13  4
   / \        \
  7   2        1
```

---

### Traversal

Start with sum = 0

#### Visit Node 5
```text
sum = 0 + 5 = 5
```

#### Visit Node 4
```text
sum = 5 + 4 = 9
```

#### Visit Node 11
```text
sum = 9 + 11 = 20
```

#### Visit Node 7
```text
sum = 20 + 7 = 27
```

Node 7 is a leaf but:

```text
27 != 22
```

Return False for this path.

---

Backtrack to node 11 and visit node 2.

#### Visit Node 2
```text
sum = 20 + 2 = 22
```

Node 2 is a leaf.

Check:

```text
22 == 22
```

Condition satisfied.

Return:

```text
True
```

---

## Valid Path Found

```text
5 → 4 → 11 → 2
```

Path sum:

```text
5 + 4 + 11 + 2 = 22
```

Since this is a root-to-leaf path and equals target sum:

# Answer = True ✅

---

## Time Complexity
Each node is visited once.

```text
O(N)
```

where **N = number of nodes**

---

## Space Complexity
Recursive call stack can go as deep as tree height.

```text
O(H)
```

where **H = height of tree**

Worst case:

```text
O(N)
```
(for skewed tree)

Best case:

```text
O(log N)
```
(for balanced tree)

---

## Key Concepts Learned
- Binary Trees
- Depth First Search (DFS)
- Recursion
- Root-to-Leaf Traversal
- Running Sum Tracking
- Backtracking
