# DSA Day 13 — Binary Search

## Problem
Given a sorted array and a target value, return the index of target.
If not found, return -1.

**Example:**
```
Input:  nums = [1,3,5,7,9,11], target = 7
Output: 3
```

---

## Solution — __Binary Search (O(log n))__

```python
class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
```

---

## How it works
- Compare target to the middle element
- If equal → found, return index
- If target is bigger → search right half (left = mid + 1)
- If target is smaller → search left half (right = mid - 1)
- Repeat until found or left > right (not found → return -1)

---

## Trace
```
nums = [1,3,5,7,9,11], target = 7

left=0, right=5: mid=2, nums[2]=5 → 5<7 → search right → left=3
left=3, right=5: mid=4, nums[4]=9 → 9>7 → search left  → right=3
left=3, right=3: mid=3, nums[3]=7 → found! return 3
```

---

## Why it's faster than linear search
- Linear search: check every element → O(n)
- Binary search: eliminate HALF the array every comparison → O(log n)
- For 1 million elements: linear = up to 1,000,000 checks, binary = only ~20 checks

---

## Common mistake — missing return -1
If the while loop ends without finding the target, the function must
explicitly return -1. Without it, Python returns None by default,
which causes wrong answer on "not found" test cases.

```python
while left <= right:
    ...
return -1   # MUST be outside the while loop, not forgotten
```

## Common mistake — unreachable code
```python
if nums[mid] == target:
    return mid
    break    # NEVER runs — return already exits the function
```
Once `return` executes, nothing after it in that code path runs.
Remove dead code like this.

---

## Time & Space Complexity
- Time: O(log n)
- Space: O(1)

---

## Pattern
> Sorted array + find a value = think binary search first
> Halving the search space each time gives massive speedup over linear scan

---

## LeetCode
#704 — Binary Search ✅ Accepted

## Your Task
Write this solution from memory before next session.
Focus on: the elif/else logic for moving left/right, and return -1 placement.
