# LeetCode 100 - Same Tree

## Problem Statement

Given the roots of two binary trees `p` and `q`, determine whether they are structurally identical and contain the same values at corresponding nodes.

---

## Approach

I used a recursive Depth First Search (DFS) approach.

For two trees to be the same:

1. Both nodes must be `None`.
2. Both nodes must have the same value.
3. Their left subtrees must be identical.
4. Their right subtrees must be identical.

The recursion compares the current nodes first and then recursively checks the left and right children.

---

## Algorithm

1. If both nodes are `None`, return `True`.
2. If one node is `None` or their values differ, return `False`.
3. Recursively compare the left subtrees.
4. Recursively compare the right subtrees.
5. Return `True` only if both subtree comparisons return `True`.

---

## Example

Input:

```
p = [1,2,3]
q = [1,2,3]
```

Output:

```
True
```

Explanation:

- Root nodes are equal (1 == 1)
- Left children are equal (2 == 2)
- Right children are equal (3 == 3)

Therefore, both trees are identical.

---

## Complexity Analysis

### Time Complexity

O(n)

where n is the number of nodes.

Each node is visited once.

### Space Complexity

O(h)

where h is the height of the tree due to the recursion stack.

In the worst case (skewed tree), h = n.

---

## Key Learning

Recursive tree problems become easier when we define the conditions under which two nodes are considered equal and then apply the same logic to their children.

This problem reinforced the concept of recursive DFS traversal in binary trees.

---

## Concepts Practiced

- Binary Trees
- Depth First Search (DFS)
- Recursion
- Tree Traversal
