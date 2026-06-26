# 235. Lowest Common Ancestor of a Binary Search Tree

## Problem
Given a Binary Search Tree (BST), find the Lowest Common Ancestor (LCA) of two given nodes.

The LCA is the lowest node that has both nodes as descendants.

---

## Approach: BST Property

A Binary Search Tree follows:

- Left subtree → smaller values  
- Right subtree → larger values  

This helps us avoid searching the entire tree.

---

## Key Idea

For current root:

- If both `p` and `q` are smaller → move left  
- If both `p` and `q` are larger → move right  
- Otherwise → current node is LCA  

The first split point is the answer.

---

## Steps
1. Start from root.
2. Compare root with p and q.
3. Move left or right depending on values.
4. Return root when split occurs.

---

## Python Solution

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)

        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)

        return root
```

---

## Complexity Analysis

**Time Complexity:** O(H)  
H = height of tree

**Space Complexity:** O(H)  
Recursion stack

---

## Key Learnings
- Binary Search Tree traversal
- Lowest Common Ancestor
- Recursive search
- Tree decision making using ordering
