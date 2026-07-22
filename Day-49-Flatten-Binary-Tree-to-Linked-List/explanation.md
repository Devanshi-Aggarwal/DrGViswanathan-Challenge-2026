# 114. Flatten Binary Tree to Linked List

## Problem Statement

Given the root of a binary tree, flatten the tree into a linked list **in-place**.

The linked list should:
- Use the same `TreeNode` class.
- Use the **right** pointer as the next node.
- Set every **left** pointer to `None`.
- Follow the **Preorder Traversal (Root → Left → Right)** order.

---

## Approach

Instead of using recursion or an additional stack, we can modify the tree directly.

For every node:

1. If the node has a left subtree:
   - Find the **rightmost node** of that left subtree.
2. Connect the original right subtree to this rightmost node.
3. Move the left subtree to the right.
4. Set the left child to `None`.
5. Continue moving to the next right node.

This transforms the tree into a preorder linked list while using constant extra space.

---

## Algorithm

1. Start from the root.
2. While the current node exists:
   - If it has a left child:
     - Find the rightmost node of the left subtree.
     - Attach the original right subtree to it.
     - Move the left subtree to the right.
     - Set the left child to `None`.
   - Move to the next right node.
3. Continue until the tree is flattened.

---

## Example

### Input

```text
        1
      /   \
     2     5
    / \     \
   3   4     6
```

### Transformation

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

### Output

```text
[1,null,2,null,3,null,4,null,5,null,6]
```

---

## Why This Works

The preorder traversal visits:

```text
Root → Left → Right
```

Whenever we move the left subtree to the right and attach the original right subtree after it, we preserve this traversal order.

---

## Complexity Analysis

### Time Complexity

**O(n)**

Each node is processed only a constant number of times.

### Space Complexity

**O(1)**

The tree is modified in-place without using recursion or additional data structures.

---

## Key Learnings

- Morris-style Tree Traversal
- Binary Tree Manipulation
- In-place Algorithms
- Pointer Rearrangement
- Preorder Traversal
- Constant Space Optimization
