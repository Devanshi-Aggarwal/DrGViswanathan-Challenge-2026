# 98. Validate Binary Search Tree

## Problem Statement

Given the `root` of a binary tree, determine whether it is a valid **Binary Search Tree (BST)**.

A valid BST satisfies:

- Every node in the left subtree contains a value **less than** the current node.
- Every node in the right subtree contains a value **greater than** the current node.
- Both left and right subtrees must also be valid BSTs.

---

## Approach

This solution performs an **Inorder Traversal** of the tree.

A key property of a Binary Search Tree is that its inorder traversal always produces values in **strictly increasing order**.

During traversal:

- Traverse the left subtree.
- Compare the current node's value with the previously visited node.
- If the current value is less than or equal to the previous value, the tree is **not** a valid BST.
- Continue traversing the right subtree.

A variable `prev` stores the previously visited value throughout the traversal.

---

## Algorithm

1. Initialize `prev` as negative infinity.
2. Perform an inorder traversal.
3. Visit the left subtree.
4. Compare the current node with `prev`.
5. If `current <= prev`, return `False`.
6. Update `prev` with the current value.
7. Traverse the right subtree.
8. If traversal completes successfully, return `True`.

---

## Example

Input:

```text
        2
       / \
      1   3
```

Inorder Traversal:

```text
1 → 2 → 3
```

Since the values are strictly increasing, the tree is a valid BST.

Output:

```text
True
```

---

## Complexity Analysis

### Time Complexity

**O(n)**

Each node is visited exactly once.

### Space Complexity

**O(h)**

where **h** is the height of the tree due to the recursion stack.

- Best Case: **O(log n)** (Balanced Tree)
- Worst Case: **O(n)** (Skewed Tree)

---

## Key Learnings

- Binary Search Tree (BST)
- Inorder Traversal
- Depth First Search (DFS)
- Recursive Tree Traversal
- Previous Node Tracking
- Tree Validation
- Monotonic Sequence Verification
