# DSA Day 9 — Maximum Sum Subarray of Size K

## Problem
Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.

**Example:**
```
Input:  nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Because [5, 1, 3] has the maximum sum = 9
```

---

## Solution — Fixed Sliding Window (O(n))

```python
nums = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i-k]
    max_sum = max(max_sum, window_sum)

print(max_sum)  # Output: 9
```

---

## How it works
- Calculate sum of first k elements as starting window
- Slide window forward one step at a time:
  - Add new element entering from right: `nums[i]`
  - Remove old element leaving from left: `nums[i-k]`
- Track maximum sum seen

---

## Trace
```
Initial window: [2, 1, 5] → sum = 8, max = 8

i=3: add nums[3]=1, remove nums[0]=2 → sum = 8+1-2 = 7, max = 8
i=4: add nums[4]=3, remove nums[1]=1 → sum = 7+3-1 = 9, max = 9 ✅
i=5: add nums[5]=2, remove nums[2]=5 → sum = 9+2-5 = 6, max = 9
```

---

## Key Line
```python
window_sum += nums[i] - nums[i-k]
```
- `nums[i]` — new number entering window from right
- `nums[i-k]` — old number leaving window from left
- No need to recalculate sum from scratch each time

---

## Difference from Kadane's

| | Kadane's | Fixed Sliding Window |
|---|---|---|
| Window size | Variable | Fixed at k |
| Use case | Max subarray any size | Max subarray exact size k |
| Key operation | extend or restart | add new, remove old |

---

## Time & Space Complexity
- Time: O(n) — one pass
- Space: O(1) — no extra data structure

---

## The Pattern
> Fixed size window: calculate first window, then slide by adding new element and removing old one.
> Never recalculate from scratch — just update.

---

## LeetCode
#643 — Maximum Average Subarray I (same pattern)

## Your Task
Write this solution from memory before next session.
Focus on: `sum(nums[:k])` for initialization and `nums[i] - nums[i-k]` for sliding.
