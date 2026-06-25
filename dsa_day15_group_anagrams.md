# DSA Day 15 — Group Anagrams

## Problem
Given a list of strings, group all anagrams together.

**Example:**
```
Input:  ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
```

---

## Solution — Sorted String as Key (O(n * k log k))

```python
words = ["eat","tea","tan","ate","nat","bat"]

groups = {}

for word in words:
    key = "".join(sorted(word))
    
    if key in groups:
        groups[key].append(word)
    else:
        groups[key] = [word]

print(list(groups.values()))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

---

## Key insight
If two words are anagrams, sorting their letters gives the EXACT SAME result:
```
"eat" sorted -> ['a','e','t'] -> "aet"
"tea" sorted -> ['a','e','t'] -> "aet"
"ate" sorted -> ['a','e','t'] -> "aet"
```
Same sorted string = same key = group together.

## Why "".join(sorted(word))
- sorted(word) returns a LIST of characters: ['a','e','t']
- "".join(...) glues that list back into a single string: "aet"
- Same trick used in Valid Palindrome's cleaning step

---

## Trace
```
"eat" -> key="aet" -> not in groups -> groups={"aet":["eat"]}
"tea" -> key="aet" -> already in groups -> groups={"aet":["eat","tea"]}
"tan" -> key="ant" -> not in groups -> groups={"aet":[...], "ant":["tan"]}
"ate" -> key="aet" -> already in groups -> groups["aet"].append("ate")
"nat" -> key="ant" -> already in groups -> groups["ant"].append("nat")
"bat" -> key="abt" -> not in groups -> new entry
```

---

## Time & Space Complexity
- Time: O(n * k log k) — n words, each sorted in k log k time (k = word length)
- Space: O(n * k) — storing all words in the dictionary

---

## Pattern
> Turning a COMPARISON problem (is X anagram of Y?) into a GROUPING problem
> (do X and Y produce the same sorted key?) is far more efficient than
> comparing every pair of words.

---

## LeetCode
#49 — Group Anagrams

## Your Task
Write this solution from memory before next session.
Focus on: "".join(sorted(word)) as the key generation step.
