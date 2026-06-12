# LeetCode 104 - Maximum Depth of Binary Tree

## Problem Statement

Given the root of a binary tree, return its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node to the farthest leaf node.

---

## Approach

I used a recursive DFS approach.

For each node, the maximum depth is calculated as:

1 + maximum depth of left subtree or right subtree

If the node is null, its depth is 0.

This recursive relationship makes the solution very concise and efficient.

---

## Algorithm

1. Check if the current node is null.
2. If null, return 0.
3. Recursively calculate depth of left subtree.
4. Recursively calculate depth of right subtree.
5. Return 1 + maximum of both depths.

---

## Complexity Analysis

### Time Complexity

O(n)

Each node is visited exactly once.

### Space Complexity

O(h)

Where h is the height of the tree due to recursion stack.

---

## Key Learning

Binary tree depth problems are naturally recursive.

By thinking of each subtree as a smaller version of the original problem, recursion provides a clean and elegant solution.

---

## Concepts Practiced

- Binary Trees
- DFS
- Recursion
- Tree Traversal
