# DSA Day 10 — Find All Anagrams in a String

## Problem
Given two strings s and p, return all the start indices of p's anagrams in s.

**Example:**
```
Input:  s = "cbaebabacd", p = "abc"
Output: [0, 6]

Because:
s[0:3] = "cba" → anagram of "abc" ✅
s[6:9] = "bac" → anagram of "abc" ✅
```

---

## Solution — Sliding Window + Two Hashmaps (O(n))

```python
s = "cbaebabacd"
p = "abc"

p_count = {}
for char in p:
    if char in p_count:
        p_count[char] += 1
    else:
        p_count[char] = 1

window_count = {}
result = []
k = len(p)

for i in range(len(s)):
    # add new character entering from right
    char = s[i]
    if char in window_count:
        window_count[char] += 1
    else:
        window_count[char] = 1
    
    # remove old character leaving from left
    if i >= k:
        old_char = s[i - k]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]
    
    # check if current window is an anagram
    if window_count == p_count:
        result.append(i - k + 1)

print(result)  # Output: [0, 6]
```

---

## How it works
- Build p_count — fixed character counts of p
- Slide a window of size k = len(p) across s
- At each step: add new char on right, remove old char on left
- Compare window_count with p_count — if equal → anagram found

---

## Trace
```
p_count = {'a':1, 'b':1, 'c':1}  ← never changes 

i=0: add 'c' → window={'c':1}
i=1: add 'b' → window={'c':1,'b':1}
i=2: add 'a' → window={'c':1,'b':1,'a':1} == p_count ✅ → result=[0]
i=3: add 'e', remove s[0]='c' → window={'b':1,'a':1,'e':1} ≠ p_count
i=4: add 'b', remove s[1]='b' → window={'b':1,'a':1,'e':1} ≠ p_count
i=5: add 'a', remove s[2]='a' → window={'b':1,'a':1,'e':1} wait...
i=6: add 'b', remove s[3]='e' → window={'a':1,'b':2} hmm
     ...continues sliding...
i=8: window = {'b':1,'a':1,'c':1} == p_count ✅ → result=[0,6]
```

---

## Key concepts

**`.get(key, default)`** — get value or return default if key missing:
```python
p_count[char] = p_count.get(char, 0) + 1
# Same as:
if char in p_count:
    p_count[char] += 1
else:
    p_count[char] = 1
```

**Why delete zero counts:**
```python
if window_count[old_char] == 0:
    del window_count[old_char]
```
If count is 0 but key exists → dictionaries won't match even if they should.
Delete zero-count keys to keep comparison clean.

---

## Time & Space Complexity
- Time: O(n) — one pass through s
- Space: O(1) — at most 26 characters in dictionary

---

## Pattern
> Fixed sliding window + two hashmaps for character counting.
> This pattern appears in: permutation in string, minimum window substring.

---

## LeetCode
#438 — Find All Anagrams in a String

## Your Task
Write this solution from memory before next session.
Focus on: removing old char when i >= k, deleting zero counts.
