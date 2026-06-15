# Explanation

## Approach
To solve this problem without using division, we compute:

- **Prefix Product** → product of all elements before index `i`
- **Suffix Product** → product of all elements after index `i`

For every index:

answer[i] = prefix[i] × suffix[i]

---

## Step 1: Compute Prefix Products
Create a prefix array where:

prefix[i] = product of all elements before i

Example:

nums = [1,2,3,4]

prefix = [1,1,2,6]

---

## Step 2: Compute Suffix Products
Create a suffix array where:

suffix[i] = product of all elements after i

Example:

suffix = [24,12,4,1]

---

## Step 3: Multiply Prefix and Suffix
For each index:

answer[i] = prefix[i] * suffix[i]

Result:

[24,12,8,6]

---

## Why This Works
At each index:

- Prefix gives product of left side
- Suffix gives product of right side
- Multiplying both excludes current element

Thus we get product of all elements except self.

---

## Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Concepts Used
- Arrays
- Prefix Product
- Suffix Product
- Simulation
