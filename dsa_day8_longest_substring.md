# DSA Day 8 — Longest Substring Without Repeating Characters

## Problem
Given a string, find the length of the longest substring without repeating characters.

**Example:**
```
Input:  s = "abcabcbb"
Output: 3
Because "abc" is the longest substring without repeating characters

Input:  s = "bbbbb"
Output: 1
```

---

## Solution — Sliding Window (O(n))

```python
s = "abcabcbb"

left = 0
max_length = 0
window_set = set()

for right in range(len(s)):
    while s[right] in window_set:
        window_set.remove(s[left])
        left += 1
    window_set.add(s[right])
    max_length = max(max_length, right - left + 1)

print(max_length)  # Output: 3
```     


---

## How it works
- Use a set to track characters currently in the window
- `right` moves forward every step — expands the window
- When a repeat is found — shrink from left until repeat is gone
- Track the maximum window size seen

---

## Trace
```
right=0, s[0]='a' → not in set → add → set={'a'} → max=1
right=1, s[1]='b' → not in set → add → set={'a','b'} → max=2
right=2, s[2]='c' → not in set → add → set={'a','b','c'} → max=3
right=3, s[3]='a' → IN set → remove s[left]='a', left=1 → set={'b','c'}
                  → add 'a' → set={'b','c','a'} → max=3
right=4, s[4]='b' → IN set → remove s[left]='b', left=2 → set={'c','a'}
                  → add 'b' → set={'c','a','b'} → max=3
```

---

## Key Concepts
- `right - left + 1` = current window size
- `+1` because indices start at 0
- `while` loop inside `for` loop — shrinks window until no repeat
- Set gives O(1) lookup for existence check

---

## Time & Space Complexity
- Time: O(n) — each character added and removed at most once
- Space: O(n) — storing characters in set

---

## The Pattern
> Sliding window = two pointers defining a window.
> Expand right, shrink left when condition breaks.
> Track the best window size seen.

---

## LeetCode
#3 — Longest Substring Without Repeating Characters

## Your Task
Write this solution from memory before next session.
Focus on: the while loop condition and `right - left + 1`.
