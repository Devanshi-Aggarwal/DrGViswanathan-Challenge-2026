# 560. Subarray Sum Equals K

## Problem Statement

Given an integer array `nums` and an integer `k`, return the total number of **continuous subarrays** whose sum equals `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

---

## Approach

A brute-force solution checks every possible subarray, resulting in **O(n²)** time complexity.

A more efficient approach uses:

- Prefix Sum
- Hash Map (Counter)

The key observation is:

If

Current Prefix Sum = `S`

and there exists a previous Prefix Sum = `S - k`

then the subarray between them has sum exactly equal to `k`.

We store the frequency of every prefix sum in a hash map while traversing the array only once.

---

## Algorithm

1. Initialize a Counter with `{0:1}`.
   - This handles subarrays starting from index `0`.

2. Maintain:
   - `s` = current prefix sum
   - `ans` = total number of valid subarrays

3. For every number:
   - Update the prefix sum.
   - Check if `(prefixSum - k)` exists.
   - Add its frequency to the answer.
   - Store the current prefix sum.

4. Return the total answer.

---

## Example

### Input

```text
nums = [1,1,1]
k = 2
```

### Prefix Sum Table

| Current Number | Prefix Sum | PrefixSum - k | Count Added |
|---------------|-----------|---------------|------------|
|1|1|-1|0|
|1|2|0|1|
|1|3|1|1|

Answer = **2**

Subarrays are:

```text
[1,1]
[1,1]
```

---

## Why This Works

Whenever

```text
Current Prefix Sum - Previous Prefix Sum = k
```

the elements between those two prefix sums form a valid subarray.

Using a hash map lets us find previous prefix sums in **O(1)** time.

---

## Complexity Analysis

### Time Complexity

**O(n)**

Only one traversal of the array is required.

### Space Complexity

**O(n)**

The hash map stores prefix sums.

---

## Key Learnings

- Prefix Sum
- Hash Map
- Frequency Counting
- Running Sum
- Array Traversal
- Optimized Subarray Problems
