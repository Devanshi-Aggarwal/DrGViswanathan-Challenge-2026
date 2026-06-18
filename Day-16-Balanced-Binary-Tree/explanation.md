# LeetCode 110 — Balanced Binary Tree

## Problem Statement
Given a binary tree, determine whether it is height-balanced.

A binary tree is considered balanced if:
- The height difference between left and right subtree of every node is at most 1.

---

## Approach Used: DFS + Height Calculation

To check if the tree is balanced, we need two things:
1. Height of left subtree
2. Height of right subtree

For every node:
- Calculate left height
- Calculate right height
- If difference > 1 → tree is unbalanced

Optimization:
Instead of checking balance separately for every node (which becomes slow), we combine:
- Height calculation
- Balance checking

into one recursive function.

---

## Algorithm

1. Create helper function `height(node)`
2. If node is `None`, return 0
3. Recursively compute left and right heights
4. Check:
   - Left subtree already unbalanced?
   - Right subtree already unbalanced?
   - Height difference > 1?
5. If any condition true → return -1
6. Otherwise return:
   1 + max(left_height, right_height)

Final answer:
- Balanced if helper does NOT return -1

---

## Python Solution

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return 0

            l, r = height(root.left), height(root.right)

            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1

            return 1 + max(l, r)

        return height(root) >= 0
```

---

## Complexity Analysis

### Time Complexity
O(n)

Each node is visited once.

### Space Complexity
O(h)

Where h is height of tree due to recursion stack.

Worst case:
O(n) for skewed tree

Best case:
O(log n) for balanced tree

---

## Key Learning

A useful optimization technique:
Sometimes one recursive function can return extra information.

Here:
- Normal height → subtree is balanced
- -1 → subtree is unbalanced

This avoids repeated calculations and improves efficiency.
