# LeetCode 101 — Symmetric Tree

## Problem Statement
Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

---

## Approach Used: Recursive DFS (Mirror Comparison)

A tree is symmetric if:

- Left subtree mirrors right subtree
- Root values are equal
- Outer nodes match inner nodes recursively

Instead of checking the tree normally, we compare two nodes at a time:

- `left.left` with `right.right`
- `left.right` with `right.left`

This ensures mirror symmetry.

---

## Algorithm

1. Create a helper function to compare two nodes.
2. If both nodes are `None`, return `True`.
3. If one node is `None` and the other is not, return `False`.
4. Check:
   - Node values are equal
   - Left child of first node matches right child of second node
   - Right child of first node matches left child of second node
5. Start comparison using root with itself.

---

## Python Solution

```python
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def isSymmetric(p: TreeNode | None, q: TreeNode | None) -> bool:
            if not p or not q:
                return p == q

            return (
                p.val == q.val and
                isSymmetric(p.left, q.right) and
                isSymmetric(p.right, q.left)
            )

        return isSymmetric(root, root)
```

---

## Complexity Analysis

### Time Complexity
O(n)

Each node is visited once.

### Space Complexity
O(h)

Where `h` is the height of the tree due to recursive stack.

Worst case:
- O(n) for skewed tree

Best case:
- O(log n) for balanced tree

---

## Key Learning

This problem teaches an important mindset:

Tree problems become easier when viewed as **relationship checks** instead of traversal problems.

Ask:
> What condition must always remain true?

Here, symmetry means mirror relationships must hold at every level.
