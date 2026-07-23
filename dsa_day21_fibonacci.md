# DSA Day 21 — Fibonacci: Recursion + Memoization

## Problem
Return the nth Fibonacci number.
Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21...

**Example:**
```
fibonacci(6) = 8
```

---

## Solution 1 — Pure Recursion (O(2^n)) - slow but easy to understand

```python
def fibonacci(n):
    if n <= 1:        # base case - stops recursion
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # 8
```

## How recursion works here
To find fibonacci(5), the function calls fibonacci(4) + fibonacci(3).
To find fibonacci(4), it calls fibonacci(3) + fibonacci(2).
This keeps breaking down until it hits the BASE CASE (n <= 1),
which returns immediately without calling itself again.

## Why it's slow - O(2^n)
Each call branches into 2 more calls. fibonacci(3) gets recalculated
many times from different branches - wasted work that explodes
exponentially as n grows.

---

## Solution 2 — Memoization (O(n)) - store results, avoid recalculating

```python
def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]   # already calculated - just look it up
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print(fibonacci(6))  # still 8, but now O(n) time
```

## Why memoization works
First time fibonacci(3) is needed -> calculate it, store it in memo.
Every SUBSEQUENT time fibonacci(3) is needed -> just return memo[3].
No repeated work. Each value calculated exactly once. O(n) total.

---

## Time & Space Complexity:

| Version | Time | Space |
|---------|------|-------|
| Pure recursion | O(2^n) | O(n) call stack |
| Memoization | O(n) | O(n) memo dict + call stack |

---

## Key concepts
- Recursion: a function that calls ITSELF, breaking a problem into smaller versions
- Base case: the stopping condition that prevents infinite recursion (n <= 1 here)
- Memoization: cache results in a dictionary to avoid recalculating the same thing
- This is the FOUNDATION of Dynamic Programming - a major interview category

---

## Your Task
Write the memoized version from memory before next session.
Focus on: the base case first, then the memo lookup, then the calculation + store.
