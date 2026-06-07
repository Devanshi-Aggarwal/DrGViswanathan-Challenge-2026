# LeetCode 347 - Top K Frequent Elements

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

---

## Approach

I used Python's `Counter` to count the frequency of each element in the array.

After creating the frequency map, I used `most_common(k)` to retrieve the k elements with the highest frequencies and extracted only the elements from the returned pairs.

---

## Algorithm

1. Count the frequency of each element using `Counter`.
2. Retrieve the k most frequent elements using `most_common(k)`.
3. Extract the element values from the returned pairs.
4. Return the resulting list.

---

## Example

### Input

```text
nums = [1,1,1,2,2,3]
k = 2
```

### Output

```text
[1,2]
```

### Explanation

Frequency count:

```text
1 → 3
2 → 2
3 → 1
```

The two most frequent elements are 1 and 2.

---

## Complexity Analysis

### Time Complexity

O(n log k)

### Space Complexity

O(n)

---

## Key Learning

Frequency-based problems can often be solved efficiently using Hash Maps. Python's `Counter` simplifies frequency counting and provides built-in methods for retrieving the most common elements.

---

## Concepts Practiced

- Hash Maps
- Frequency Counting
- Python Counter
- Arrays
