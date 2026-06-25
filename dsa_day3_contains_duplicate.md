# DSA Day 3 — Contains Duplicate

## Problem
Given an array of integers, return true if any value appears at least twice, 
and false if every element is distinct.

**Example:**
```
Input:  nums = [1, 2, 3, 1]
Output: True

Input:  nums = [1, 2, 3, 4]
Output: False
```

---

## Solution — Hashmap (O(n))

```python
nums = [1, 2, 3, 1]

seen = {}

for num in nums:
    if num in seen:
        print(True)
        break
    seen[num] = True
else:
    print(False)
```

---

## How it works
- Loop through array once
- For each number — check if it's already in `seen`
- If yes → duplicate found → print True and stop immediately
- If no → store it in `seen` and continue
- If loop finishes without breaking → no duplicates → print False

---

## New concept — for...else
Python's `for...else` is unique:
- `else` block runs ONLY if the loop completed without hitting `break`
- If `break` was triggered → `else` is skipped

```python
for num in nums:
    if condition:
        break        # else block won't run
else:
    print(False)     # only runs if no break happened
```

Most people don't know this exists. Remember it.

---

## Time & Space Complexity

| | What it means | This problem |
|---|---|---|
| Time O(n) | Steps grow with input size | One pass through array |
| Space O(n) | Memory grows with input size | Storing all values in seen dict |

**Simple rule:**
- Time = how many steps does your code take?
- Space = how much extra memory does your code use?

---

## The Pattern
> Same "have I seen this before" hashmap pattern from Two Sum.
> Instead of looking for a complement, you're looking for a repeat.

This pattern appears in: duplicate detection, anagram checking, frequency counting.

---

## Your Task
Write this solution from memory before next session.
Focus on: correct indentation of `break`, and `for...else` placement.
