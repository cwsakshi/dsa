# DSA Day 16 — Top K Frequent Elements

## Problem
Given an array of integers, return the k most frequent elements.

**Example:**
```
Input:  nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

---

## Solution — Count + Sort by Lambda (O(n log n))

```python
nums = [1,1,1,2,2,3]
k = 2

# Phase 1: count frequencies
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
# counts = {1: 3, 2: 2, 3: 1}

# Phase 2: sort by frequency, take top k
sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
# sorted_items = [(1,3), (2,2), (3,1)]

result = [item[0] for item in sorted_items[:k]]
print(result)  # [1, 2]
```

---

## How it combines two known patterns
1. Counting occurrences with a dictionary (same as count_words pattern)
2. Sorting with lambda key (same as sorting students by score)

```python
counts.items()  # gives [(key, value), (key, value), ...] pairs
sorted(..., key=lambda x: x[1], reverse=True)  # sort by the count (2nd item)
sorted_items[:k]  # slice top k tuples
[item[0] for item in ...]  # extract just the number, not the count
```

---

## Common mistake
`sorted_items` is a LIST of tuples after sorted() - it does NOT have
.values() like a dictionary does. Slice it directly with [:k] instead.

---

## Time & Space Complexity
- Time: O(n log n) — dominated by the sort
- Space: O(n) — for the dictionary

---

## Pattern
> Frequency counting + sorting by count = the standard approach for
> "top k" or "most frequent" style problems

---

## LeetCode
#347 — Top K Frequent Elements

## Your Task
Write this solution from memory before next session.
Focus on: counts.items() + sorted with lambda key + list comprehension to extract values.
