# LeetCode 226 - Invert Binary Tree

## Problem Statement

Given the root of a binary tree, invert the tree and return its root.

---

## Approach

I used a recursive DFS approach.

For each node, I swap its left and right children and then recursively apply the same operation to both subtrees. The recursion stops when a null node is encountered.

---

## Algorithm

1. Check if the current node is null.
2. Store the left and right child nodes.
3. Recursively invert the right subtree and assign it to the left child.
4. Recursively invert the left subtree and assign it to the right child.
5. Return the current node.

---

## Complexity Analysis

### Time Complexity

O(n)

Each node is visited exactly once.

### Space Complexity

O(h)

Where h is the height of the tree due to the recursion stack.

---

## Key Learning

This problem demonstrates how recursion can simplify tree manipulation problems. By solving the same task for smaller subtrees, we can invert the entire tree with very little code.

---

## Concepts Practiced

- Binary Trees
- DFS
- Recursion
- Tree Traversal
