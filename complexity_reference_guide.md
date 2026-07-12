# Time & Space Complexity — Complete Reference Guide

## What is Time Complexity?
Answers: "As input grows bigger, how much MORE work does my code do?"
Not about actual seconds — about the PATTERN of growth......

## What is Space Complexity?
Answers: "As input grows bigger, how much MORE memory does my code need?"

---

## The Complexity Ladder (fastest to slowest)____

```
O(1)        - constant      - same work no matter input size
O(log n)    - logarithmic   - work grows very slowly
O(n)        - linear        - work grows directly with input
O(n log n)  - linearithmic  - slightly worse than linear
O(n²)       - quadratic     - work grows by the square of input
```

---

## Mapped to Problems You've Already Solved

### O(1) — Constant Time
```python
def get_first(nums):
    return nums[0]
```
Same single step regardless of array size (10 or 10 million elements).

**Space O(1) example — Binary Search variables:**
Only uses `left`, `right`, `mid` — fixed number of variables, doesn't grow with input.

---

### O(log n) — Binary Search
```python
while left <= right:
    mid = (left + right) // 2
```
Each step CUTS the problem in half.
- 1000 elements → only ~10 steps needed (2^10 = 1024)
- 1,000,000 elements → only ~20 steps needed

---

### O(n) — Two Sum (hashmap version)
```python
for i in range(len(nums)):
    need = target - nums[i]
    if need in seen:
        ...
    seen[nums[i]] = i
```
One loop through array. Array doubles → work roughly doubles. Direct proportional relationship.

**Space O(n) example:** `seen` dictionary can grow to hold up to n entries (worst case: no duplicates found early).

---

### O(n log n) — Merge Intervals / Top K Frequent
```python
intervals.sort(key=lambda x: x[0])
# or
sorted_items = sorted(counts.items(), key=lambda x: x[1])
```
Sorting algorithms take n log n time. Slightly worse than linear, but much better than quadratic.

---

### O(n²) — Two Sum Brute Force (the very first version)
```python
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        ...
```
Loop INSIDE another loop. Array doubles → work roughly QUADRUPLES (2² = 4).
This is why we look for hashmap/sorting tricks to avoid nested loops.

---

## CRITICAL RULE #1 — Sequential steps: take the SLOWEST one

Example: Top K Frequent Elements
```python
counts = {}
for num in nums:                          # Step 1: O(n)
    counts[num] = counts.get(num, 0) + 1

sorted_items = sorted(counts.items(), ...)  # Step 2: O(n log n)
result = [item[0] for item in sorted_items[:k]]  # Step 3: O(k)
```

Overall Time Complexity = **O(n log n)**

Why? Because when steps run one after another (not nested), you take
whichever single step is most expensive — NOT add them all together
in detail. The sort dominates as n grows large, even though counting
itself is only O(n).

---

## CRITICAL RULE #2 — Space: check EVERY data structure, not just the final return

Example: Top K Frequent Elements
```python
counts = {}        # can grow to size n (worst case: all unique numbers)
result = [...]      # only size k
```

Overall Space Complexity = **O(n)**

Common mistake: assuming space = size of final output (k).
Correct approach: look at the LARGEST structure created anywhere in
the function. The counts dictionary (size n) dominates over the
final result list (size k), since n is generally >> k.

---

## Quick Reference Table — Problems Solved So Far

| Problem | Time | Space | Why |
|---|---|---|---|
| Two Sum (brute force) | O(n²) | O(1) | nested loops |
| Two Sum (hashmap) | O(n) | O(n) | one loop + dict storage |
| Two Sum (two pointers, sorted) | O(n) | O(1) | one loop, no extra structure |
| Kadane's (Max Subarray) | O(n) | O(1) | one pass, two variables |
| Contains Duplicate | O(n) | O(n) | one loop + set storage |
| Find Pivot Index | O(n) | O(1) | one pass, running totals |
| Valid Palindrome | O(n) | O(n) | cleaning string creates new string |
| Valid Anagram | O(n) | O(n) | two hashmaps |
| Longest Substring (no repeat) | O(n) | O(n) | sliding window + set |
| Find All Anagrams | O(n) | O(1)* | sliding window + dict (*bounded by alphabet size) |
| Max Sum Subarray of Size K | O(n) | O(1) | fixed sliding window |
| K Distinct Characters | O(n) | O(k) | dict bounded by k |
| Rotate Array | O(n) | O(n) | slicing creates new lists |
| Binary Search | O(log n) | O(1) | halves search space each step |
| Merge Intervals | O(n log n) | O(n) | sorting dominates |
| Group Anagrams | O(n·k log k) | O(n·k) | n words, each sorted (k = word length) |
| Top K Frequent Elements | O(n log n) | O(n) | counting O(n) + sort O(n log n) dominates |

---

## How to Answer This in an Interview

1. Identify each major step in your code (loops, sorts, recursive calls)
2. State each step's individual complexity
3. For TIME: combine sequential steps by taking the MAX (slowest)
   - Combine NESTED steps by MULTIPLYING
4. For SPACE: identify the LARGEST data structure created anywhere,
   not just what gets returned
5. Say it out loud naturally: "This has one O(n) loop for counting,
   then an O(n log n) sort, so the dominant term is O(n log n) overall."

---

## Your Task
Re-read this file before every DSA session as a warm-up.
Try to answer Time & Space complexity OUT LOUD for every new problem
before checking against the solution.
