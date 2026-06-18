# DSA Day 1 — Two Sum

## Problem
Given an array of integers, return the indices of the two numbers that add up to a target.
You may assume exactly one solution exists. You cannot use the same element twice.

**Example:**
```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Because nums[0] + nums[1] = 2 + 7 = 9
```

---

## Solution 1 — Brute Force (O(n²))

```python
nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print((i, j))
```

- Two nested loops
- For every number, check every other number
- Slow for large arrays — 1 million numbers = 1 trillion operations

---

## Solution 2 — Hashmap (O(n)) ✅ OPTIMAL

```python
nums = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(nums)):
    need = target - nums[i]
    if need in seen:
        print([seen[need], i])
    seen[nums[i]] = i
```

### How it works — step by step trace:
```
Start: seen = {}

i=0, nums[0]=2, need=7
→ is 7 in {} ? No
→ store 2 → seen = {2:0}

i=1, nums[1]=7, need=2
→ is 2 in {2:0} ? YES
→ print [seen[2], 1] → print [0, 1] ✅
```

---

## Key Concepts Learned

| Concept | Explanation |
|---|---|
| Array | List of items in order. Each item has an index starting from 0 |
| Index | Position of an item. nums[2] gives the item at position 2 |
| Nested loop | A loop inside a loop. Used in brute force |
| Dictionary | Stores key → value pairs. Used to remember things seen before |
| O(n²) | Time complexity of brute force — very slow for large inputs |
| O(n) | Time complexity of hashmap — only one loop, very fast |

---

## The Pattern to Remember
> Whenever you need to check "have I seen this before?" — reach for a dictionary.
> This pattern appears in ~30% of all hashmap problems.

---

## Your Task
Write the hashmap solution from scratch — no looking. If you can write it from memory, you own it.



     



