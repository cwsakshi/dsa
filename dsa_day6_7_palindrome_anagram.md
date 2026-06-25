# DSA Day 6 — Valid Palindrome

## Problem
Given a string, determine if it is a palindrome.
Consider only alphanumeric characters and ignore cases.

**Example:**
```
Input:  s = "A man, a plan, a canal: Panama"
Output: True

Input:  s = "race a car"
Output: False
```

---

## Solution — Clean + Two Pointers (O(n))

```python
s = "A man, a plan, a canal: Panama"
cleaned = "".join(c.lower() for c in s if c.isalnum())

left = 0
right = len(cleaned) - 1

while left < right:
    if cleaned[left] != cleaned[right]:
        print(False)
        break
    left += 1
    right -= 1
else:
    print(True)
```

## Key Line
```python
cleaned = "".join(c.lower() for c in s if c.isalnum())
```
- `c.isalnum()` — keeps only letters and numbers
- `c.lower()` — makes everything lowercase
- `"".join()` — joins characters back into string

## Pattern
> String cleaning + two pointers = palindrome check
> Always clean the string before applying logic

## Time & Space
- Time: O(n)
- Space: O(n) — storing cleaned string

---
---

# DSA Day 7 — Valid Anagram

## Problem
Given two strings s and t, return true if t is an anagram of s.
An anagram uses the same characters the same number of times.

**Example:**
```
Input:  s = "anagram", t = "nagaram"
Output: True

Input:  s = "rat", t = "car"
Output: False
```

---

## Solution — Two Hashmaps (O(n))

```python
s = "anagram"
t = "nagaram"

count_s = {}
count_t = {}

for char in s:
    if char in count_s:
        count_s[char] += 1
    else:
        count_s[char] = 1

for char in t:
    if char in count_t:
        count_t[char] += 1
    else:
        count_t[char] = 1

if count_s == count_t:
    print("It is anagram")
else:
    print("It is not anagram")
```

## How it works
- Count character frequency in both strings
- Compare both dictionaries — if equal, it's an anagram

## Key insight
Python lets you compare two dictionaries directly with ==
If all keys and values match → True

## Time & Space
- Time: O(n) — two passes
- Space: O(n) — storing character counts

## Pattern
> Anagram = same character counts. Two hashmaps + compare.
> Appears in: group anagrams, permutation checks, string matching.

---

## Your Task
Write both solutions from memory before next session.
