# DSA Day 17 — Valid Parentheses

## Problem
Given a string containing (){}[], determine if the brackets are balanced.

**Example:**
```
Input: "({[]})"  -> True
Input: "([)]"    -> False
```

---

## Solution — Stack (O(n))

```python
s = "({[]})"
stack = []

pairs = {')': '(', '}': '{', ']': '['}

for char in s:
    if char in "({[":
        stack.append(char)
    elif stack and stack[-1] == pairs[char]:
        stack.pop()
    else:
        print(False)
        break
else:
    print(len(stack) == 0)
```

---

## What is a Stack
Like a pile of plates - can only add (push) or remove (pop) from the TOP.
Last one in is the first one out (LIFO - Last In First Out).

## How it works
- Opening bracket -> push onto stack ("waiting to be closed")
- Closing bracket -> check if it matches the TOP of the stack
  - pairs[char] tells you which opening bracket SHOULD be on top right now
  - Match -> pop (this pair is resolved)
  - No match -> immediately invalid, break

## Why TWO checks are needed

**Check 1 (during loop): stack[-1] == pairs[char]**
Catches WRONG ORDER. Example "([)]":
```
'(' -> push -> stack=['(']
'[' -> push -> stack=['(','[']
')' -> closing -> stack[-1]='[' but pairs[')']='(' -> MISMATCH -> False
```
Even though counts match (2 opens, 2 closes), the order is wrong.

**Check 2 (after loop): len(stack) == 0**
Catches LEFTOVER unclosed brackets. Example "(((":
```
All three push successfully, no closing brackets to mismatch.
Loop finishes with no break, but stack=['(','(','('] is NOT empty.
```
Without this check, unclosed brackets would incorrectly pass.

---

## Trace — "({[]})"
```
'(' -> push -> stack=['(']
'{' -> push -> stack=['(','{']
'[' -> push -> stack=['(','{','[']
']' -> match '[' -> pop -> stack=['(','{']
'}' -> match '{' -> pop -> stack=['(']
')' -> match '(' -> pop -> stack=[]
Loop finishes -> else runs -> len(stack)==0 -> True
```

## Trace — "([)]"
```
'(' -> push -> stack=['(']
'[' -> push -> stack=['(','[']
')' -> stack[-1]='[' != pairs[')']='(' -> MISMATCH -> print(False), break
```

---

## Time & Space Complexity
- Time: O(n) - one pass through string
- Space: O(n) - stack can hold up to n characters (worst case all opening brackets)

---

## Pattern
> Matching/balancing problems where ORDER matters = Stack
> Stack always checks the MOST RECENT unresolved item first

---

## LeetCode
#20 — Valid Parentheses

## Your Task
Write this solution from memory before next session.
Focus on: pairs dictionary lookup, elif condition checking stack[-1], and the two separate failure checks.
