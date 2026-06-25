# DSA Day 5 — Find Pivot Index

## Problem
Given an integer array, find the index where the total sum on the left 
equals the total sum on the right. Return -1 if no such index exists.

**Example:**
```
Input:  nums = [1, 7, 3, 6, 5, 6]
Output: 3
Because left sum = 1+7+3 = 11, right sum = 5+6 = 11
```

---

## Solution — Prefix Sum (O(n) time, O(1) space)

```python
nums = [1, 7, 3, 6, 5, 6]
total_sum = sum(nums)
left_sum = 0

for i in range(len(nums)):
    right_sum = total_sum - left_sum - nums[i]
    
    if left_sum == right_sum:
        print(i)
        break
    
    left_sum += nums[i]
```

---

## How it works
- Precompute total sum of entire array
- Loop through array once, tracking left_sum
- At each index: right_sum = total - left_sum - current number
- If left_sum == right_sum → found pivot index

---

## Trace
```
total_sum = 28

i=0: right=28-0-1=27,  left=0  → no  → left=1
i=1: right=28-1-7=20,  left=1  → no  → left=8
i=2: right=28-8-3=17,  left=8  → no  → left=11
i=3: right=28-11-6=11, left=11 → ✅  → print(3)
```

---

## Key Formula
```
right_sum = total_sum - left_sum - nums[i]
```
This eliminates the need for a second loop entirely.

---

## Time & Space Complexity
- Time: O(n) — one pass through array
- Space: O(1) — only tracking two variables

---

## The Pattern
> When you need left and right sums at every index:
> Precompute total sum, track left sum as you go.
> Right sum = total - left - current.

---

## Your Task
Write this solution from memory before next session.
Focus on: the right_sum formula and updating left_sum AFTER the check.
