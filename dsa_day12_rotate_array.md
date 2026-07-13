# DSA Day 12 — Rotate Array

## Problem
Given an array of integers, rotate the array to the right by k steps.

**Example:**
```
Input:  nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```

---

## Solution — Slicing + Modulo

```python
class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
```

---

## How it works --
- `nums[-k:]` → last k elements
- `nums[:-k]` → everything except last k elements
- Concatenate: last k elements move to front, rest move to back
- `nums[:] = ...` → modifies the array IN PLACE (doesn't create new list)

---

## Why modulo is needed
If k is larger than array length, rotating "wraps around".
Rotating by len(nums) brings array back to original position.
So k=10 on a 7-element array is same as k=10%7=3.

```python
k = k % len(nums)   # always do this first in rotation problems
```

---

## Trace
```
nums = [1,2,3,4,5,6,7], k=3

nums[-3:]  = [5,6,7]
nums[:-3]  = [1,2,3,4]

result = [5,6,7] + [1,2,3,4] = [5,6,7,1,2,3,4]
```

---

## Key concept: In-place modification
LeetCode wants `-> None` return type — meaning don't return a new list,
modify the original array directly:

```python
nums[:] = new_values   # modifies original list in place
return new_values       # creates and returns a NEW list (different!)
```

`nums[:] = ...` keeps the same list object but changes its contents.
This matters when other code references the same list elsewhere.

---

## Time & Space Complexity
- Time: O(n) — slicing creates temporary lists
- Space: O(n) — temporary lists during slicing

---

## Pattern
> Array rotation = split into two parts + swap their order using slicing
> Always handle k > len(nums) with modulo

---

## LeetCode
#189 — Rotate Array ✅ Accepted

## Your Task
Write this solution from memory before next session.
Focus on: the modulo step and nums[:] = ... for in-place modification.
