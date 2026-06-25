# DSA Day 2 — Maximum Subarray (Kadane's Algorithm)

## Problem
Given an integer array, find the maximum sum of any contiguous subarray.

**Example:**
```
Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Because [4, -1, 2, 1] has the largest sum = 6
```

---

## Solution — Kadane's Algorithm (O(n))

```python
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = 0
max_sum = nums[0]

for num in nums:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

print(max_sum)  # Output: 6
```

---

## The Core Insight
If your running sum goes **below zero** — drop it and start fresh.
Carrying a negative sum always hurts you.

```
current sum = -3, next number = 4
Option 1: -3 + 4 = 1  ← carry forward
Option 2: 4            ← start fresh ✅ always better
```

---

## Step by Step Trace

```
num=-2: current_sum = max(-2, -2) = -2,  max_sum = -2
num= 1: current_sum = max(1,  -1) =  1,  max_sum =  1  ← dropped -2
num=-3: current_sum = max(-3, -2) = -2,  max_sum =  1
num= 4: current_sum = max(4,   2) =  4,  max_sum =  4  ← dropped -2
num=-1: current_sum = max(-1,  3) =  3,  max_sum =  4
num= 2: current_sum = max(2,   5) =  5,  max_sum =  5
num= 1: current_sum = max(1,   6) =  6,  max_sum =  6  ← new high
num=-5: current_sum = max(-5,  1) =  1,  max_sum =  6
num= 4: current_sum = max(4,   5) =  5,  max_sum =  6
```

Final answer: 6 → subarray [4, -1, 2, 1]

---

## Key Concepts

| Line | What it does |
|---|---|
| `current_sum = max(num, current_sum + num)` | Extend or restart — whichever is bigger |
| `max_sum = max(max_sum, current_sum)` | Scoreboard — track the highest ever reached |

---

## The Pattern to Remember
> At every step — extend or restart. Track the best you've ever seen.
> This pattern appears in subarray problems involving running calculations.

## Time & Space Complexity
- Time: O(n) — one pass through the array
- Space: O(1) — no extra data structure needed

---

## Your Task

Write Kadane's Algorithm from memory — just the 2 lines inside the loop.
```python
current_sum = max(num, current_sum + num)
max_sum = max(max_sum, current_sum)
```


**The pattern difference between the two problems:**

|                 | Max Subarray Sum |     Max Subarray Product |
|---              |---          |---                             |
| Track.          | current max | current max AND min            
| Why min?        | Not needed  | Negative × negative = positive |
| Reset condition | sum < 0     | built into max/min logic       |

---

**Key insight to remember:**

> Whenever negatives can flip to positives — track both max and min.

This pattern appears in several other problems too.

---

nums = [2, 3, -2, 4]

max_prod = nums[0]
min_prod = nums[0]
result = nums[0]

for num in nums[1:]:
    new_max = max(num, max_prod * num, min_prod * num)
    new_min = min(num, max_prod * num, min_prod * num)
    max_prod = new_max
    min_prod = new_min
    result = max(result, max_prod)

print(result)
