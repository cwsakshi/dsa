# DSA Day 11 — Longest Substring with At Most 2 Distinct Characters

## Problem
Given a string s, find the length of the longest substring that contains
at most 2 distinct characters.______

**Example:**
```
Input:  s = "eceba"
Output: 3
Because "ece" has 2 distinct characters and length 3
```

---

## Solution — Sliding Window + Dictionary (O(n))

```python
s = "eceba"
k = 2  # at most k distinct characters

window = {}
left = 0
max_length = 0

for right in range(len(s)):
    char = s[right]
    window[char] = window.get(char, 0) + 1
    
    while len(window) > k:
        left_char = s[left]
        window[left_char] -= 1
        if window[left_char] == 0:
            del window[left_char]
        left += 1
    
    max_length = max(max_length, right - left + 1)

print(max_length)  # Output: 3
```

---

## Why dictionary instead of set
- Set only tells you "is this character here?" (yes/no)
- Dictionary tells you "how many of this character are here?"
- Need counts to know exactly when a character's count hits 0 and can be removed
- `len(window)` = number of distinct characters currently in window

---

## How it works
- Expand window by adding char on right, increment its count
- If distinct character count exceeds k → shrink from left
- When a character's count reaches 0 → delete it from dictionary
- Track maximum window size seen

---

## Trace
```
s = "eceba", k=2

right=0: 'e' → window={'e':1} → distinct=1 ≤ 2 → max=1
right=1: 'c' → window={'e':1,'c':1} → distinct=2 ≤ 2 → max=2
right=2: 'e' → window={'e':2,'c':1} → distinct=2 ≤ 2 → max=3
right=3: 'b' → window={'e':2,'c':1,'b':1} → distinct=3 > 2
          → shrink: remove s[0]='e' → window={'e':1,'c':1,'b':1} still 3 distinct
          → shrink: remove s[1]='c' → window={'e':1,'b':1} → distinct=2 ✅
          → max stays 3
right=4: 'a' → window={'e':1,'b':1,'a':1} → distinct=3 > 2
          → shrink until distinct=2
```

---

## Time & Space Complexity
- Time: O(n) — each character processed at most twice
- Space: O(k) — dictionary holds at most k+1 characters

---

## Pattern
> "At most k distinct characters" = sliding window + dictionary tracking counts
> Shrink window when distinct count exceeds k
> Same family as: Longest Substring Without Repeating Characters, Find All Anagrams

---

## Your Task
Write this solution from memory before next session.
Focus on: window.get(char, 0), the while len(window) > k shrink logic, and deleting zero counts.
