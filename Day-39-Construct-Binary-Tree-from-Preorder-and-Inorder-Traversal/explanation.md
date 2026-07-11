# 105. Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement

Given two integer arrays `preorder` and `inorder`, where:

- `preorder` represents the preorder traversal of a binary tree.
- `inorder` represents the inorder traversal of the same tree.

Construct and return the binary tree.

---

## Approach

This solution uses **Recursion** along with a **Hash Map** for efficient index lookup.

### Key Observations

- In **Preorder Traversal**, the first element is always the root.
- In **Inorder Traversal**, all nodes to the left of the root belong to the left subtree, while all nodes to the right belong to the right subtree.

To efficiently locate the root in the inorder array, a dictionary is created that maps each node value to its index.

The tree is then recursively constructed by determining the boundaries of the left and right subtrees.

---

## Algorithm

1. Store every value and its index from the inorder array in a hash map.
2. The first element in the preorder segment becomes the root.
3. Find the root's position in the inorder array.
4. Calculate the size of the left subtree.
5. Recursively build:
   - Left subtree
   - Right subtree
6. Return the constructed root node.

---

## Example

Input:

```text
Preorder = [3,9,20,15,7]
Inorder  = [9,3,15,20,7]
```

Tree Construction:

```text
        3
       / \
      9   20
         /  \
        15   7
```

Output:

```text
[3,9,20,null,null,15,7]
```

---

## Complexity Analysis

### Time Complexity

**O(n)**

Each node is processed exactly once.

### Space Complexity

**O(n)**

- Hash map stores every node.
- Recursive call stack in the worst case.

---

## Key Learnings

- Binary Tree Construction
- Preorder Traversal
- Inorder Traversal
- Divide and Conquer
- Recursion
- Hash Map
- Recursive Tree Building
- Tree Partitioning
