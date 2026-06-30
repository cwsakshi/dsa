# DSA Day 19 — Container With Most Water

## Problem
Given heights of vertical lines, find two lines that form a container
holding the most water.

**Example:**
```
Input:  height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

---

## Solution — Two Pointers (O(n))

```python
height = [1,8,6,2,5,4,8,3,7]

left = 0
right = len(height) - 1
max_area = 0

while left < right:
    width = right - left
    current_height = min(height[left], height[right])
    area = width * current_height
    max_area = max(max_area, area)
    
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(max_area)  # 49
```

---

## The formula
```
area = (right - left) * min(height[left], height[right])
```
Width = distance between the two lines.
Height = limited by the SHORTER line (water spills over the shorter side).

---

## Why start from BOTH ends (widest possible container)
left=0, right=len-1 gives the maximum possible WIDTH to start.
As pointers move inward, width can only shrink - so you need height
to compensate for any area improvement.

## Why move the SHORTER pointer specifically
If height[left] < height[right]:
- Moving `right` inward can NEVER help. The shorter side (left) is
  still the limiting factor (min() picks the smaller one regardless),
  so you'd just be shrinking width for zero benefit.
- Moving `left` inward instead gives a CHANCE to find a taller line,
  which could increase area despite the smaller width.

This is the key insight that makes two pointers work here instead of
checking every pair (which would be O(n²)).

---

## Time & Space Complexity
- Time: O(n) — each pointer moves at most n times total, one pass
- Space: O(1) — only a few variables, no extra structure

---

## Pattern
> Two pointers from both ends, move the pointer that's "limiting" you
> This pattern: maximize/optimize over a range where one side is the
> bottleneck - moving the bottleneck side is the only way to potentially improve

---

## LeetCode
#11 — Container With Most Water

## Your Task
Write this solution from memory before next session.
Focus on: WHY we move the shorter pointer, not just memorizing the code.
