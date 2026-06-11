# LeetCode 56 - Merge Intervals

## Problem Statement

Given a collection of intervals, merge all overlapping intervals and return an array of non-overlapping intervals that covers all the intervals in the input.

---

## Approach

I first sort all intervals based on their starting value.

Then, I iterate through the sorted intervals and compare each interval with the last interval in the answer list.

- If the intervals do not overlap, I add the current interval to the answer.
- If they overlap, I merge them by updating the ending value of the last interval.

This ensures that all overlapping intervals are combined efficiently.

---

## Algorithm

1. Sort the intervals based on their start value.
2. Create an empty answer list.
3. Traverse through each interval.
4. If the answer list is empty or there is no overlap, add the interval.
5. Otherwise, merge the intervals by updating the ending value.
6. Return the merged intervals.

---

## Complexity Analysis

### Time Complexity

O(n log n)

Sorting the intervals takes O(n log n) time.

### Space Complexity

O(n)

The answer list stores the merged intervals.

---

## Key Learning

Sorting is often the first step in interval problems.

Once intervals are sorted, overlapping intervals become adjacent, making it easy to merge them in a single traversal.

---

## Concepts Practiced

- Arrays
- Sorting
- Intervals
- Greedy Approach
- List Manipulation
