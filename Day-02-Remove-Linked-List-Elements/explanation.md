# Remove Linked List Elements

## Problem

Remove all nodes whose value equals the given target.

## Approach

Used a dummy node to handle edge cases where the head node itself needs to be removed.

Traversed the linked list once and connected only the nodes whose values were not equal to the target.

## Complexity

Time: O(n)

Space: O(1)

## Key Learning

Dummy nodes simplify linked list problems by avoiding special handling for head node deletions.
