# 230. Kth Smallest Element in a BST

## Problem
Given the root of a Binary Search Tree and an integer `k`, return the kth smallest value in the tree.

---

## Approach: Inorder Traversal

A Binary Search Tree has an important property:

- Left subtree contains smaller values
- Root contains middle value
- Right subtree contains larger values

Because of this, **inorder traversal** gives elements in sorted order.

Traversal order:

Left → Root → Right

So the kth visited node is the kth smallest element.

---

## Key Idea

- Start inorder traversal
- Keep decreasing `k`
- When `k == 1`, current node is answer

---

## Why Inorder Works in BST

Example BST:

```text
      3
     / \
    1   4
     \
      2
```

Inorder traversal:

1 → 2 → 3 → 4

Sorted order achieved automatically.

---

## Python Solution

```python
class Solution:
    def kthSmallest(self, root, k):
        count = [k]
        ans = [0]

        def dfs(node):
            if not node:
                return

            dfs(node.left)

            if count[0] == 1:
                ans[0] = node.val

            count[0] -= 1

            if count[0] > 0:
                dfs(node.right)

        dfs(root)
        return ans[0]
```

---

## Dry Run

Input:

root = [3,1,4,null,2]  
k = 1

Traversal:

Visit 1 → k becomes 1 → answer = 1

Output:

1

---

## Complexity Analysis

**Time Complexity:**  
O(H + k) average  
Worst case O(n)

**Space Complexity:**  
O(H)

Where H = height of tree.

---

## Key Learnings
- Binary Search Tree property
- Inorder Traversal
- DFS
- Ordered traversal
- Recursive tree processing
