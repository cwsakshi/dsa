# DSA Day 4 — Two Sum II (Two Pointers)

## Problem
Given a sorted array, return indices of two numbers that add up to target.
Must use constant extra space — no hashmap allowed.

**Example:**
```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

---

## Solution — Two Pointers (O(n) time, O(1) space)

```python
nums = [2, 7, 11, 15]
target = 9

left = 0
right = len(nums) - 1

while left < right:
    current_sum = nums[left] + nums[right]
    
    if current_sum == target:
        print([left, right])
        break
    elif current_sum > target:
        right -= 1
    else:
        left += 1
```

---

## How it works
- Start with one pointer at beginning, one at end
- Calculate sum of both pointers
- Sum too big → move right pointer left (smaller number)
- Sum too small → move left pointer right (bigger number)
- Sum equals target → found it, break

## Trace
```
left=0, right=3 → 2+15=17 → too big → right=2
left=0, right=2 → 2+11=13 → too big → right=1
left=0, right=1 → 2+7=9   → found! → [0, 1] ✅
```

---

## Comparison Table

| Approach | Time | Space |
|---|---|---|
| Brute force (nested loops) | O(n²) | O(1) |
| Hashmap (Two Sum I) | O(n) | O(n) |
| Two Pointers (Two Sum II) | O(n) | O(1) ✅ |

---

## The Pattern
> Sorted array + find a pair = think two pointers first.
> Two pointers gives you O(n) time AND O(1) space — best of both worlds.

---

## Your Task
Write this solution from memory before next session.
Focus on: while condition, moving pointers correctly, break after finding answer.
