# 215. Kth Largest Element in an Array

## Problem Statement

Given an integer array `nums` and an integer `k`, return the **kth largest element** in the array.

Note that it is the kth largest element in the sorted order, **not** the kth distinct element.

The challenge is to solve the problem without fully sorting the array.

---

## Approach

This solution uses the **Quick Select** algorithm, which is based on the partitioning idea of Quick Sort.

Instead of sorting the entire array, Quick Select repeatedly partitions the array and only continues searching in the half that contains the required element.

Steps:

- Convert the kth largest position into the corresponding index if the array were sorted.
- Choose a pivot element.
- Partition the array into elements smaller and larger than the pivot.
- Determine which partition contains the required index.
- Continue searching only in that partition.

This avoids sorting unnecessary elements and gives an efficient average-case solution.

---

## Algorithm

1. Convert the kth largest element into its sorted index.
2. Select a pivot element.
3. Partition the array around the pivot.
4. If the target index lies in the left partition, recurse left.
5. Otherwise recurse right.
6. Return the element when the partition contains only one element.

---

## Example

Input:

```text
nums = [3,2,1,5,6,4]
k = 2
```

Sorted Array:

```text
[1,2,3,4,5,6]
```

The 2nd largest element is:

```text
5
```

Output:

```text
5
```

---

## Complexity Analysis

### Average Time Complexity

**O(n)**

Only one partition is explored during each recursive call.

### Worst Time Complexity

**O(n²)**

Occurs when poor pivot selections repeatedly produce highly unbalanced partitions.

### Space Complexity

**O(log n)**

Due to recursive function calls.

---

## Key Learnings

- Quick Select Algorithm
- Partitioning Technique
- Divide and Conquer
- Quick Sort Partition Logic
- Selection Algorithms
- Average Linear Time Complexity
- In-place Array Partitioning
