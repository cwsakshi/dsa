# DSA Day 14 — Merge Intervals

## Problem
Given a list of intervals, merge all overlapping intervals.

**Example:**
```
Input:  [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

---

## Solution — Sort + Merge (O(n log n))

```python
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort(key=lambda x: x[0])  # sort by start value

result = [intervals[0]]

for interval in intervals[1:]:
    last = result[-1]
    if interval[0] <= last[1]:
        # overlap - merge by extending the end
        last[1] = max(last[1], interval[1])
    else:
        # no overlap - add as new interval
        result.append(interval)

print(result)  # [[1,6],[8,10],[15,18]]
```

---

## Why sort first
If intervals are sorted by start value, you only ever need to compare
each new interval to the LAST interval already merged — not every pair.
This turns an O(n²) problem into O(n log n).

## Why max() when merging
```python
last[1] = max(last[1], interval[1])
```
Without max(), if the current interval is fully contained inside the
previous one (e.g. [1,10] followed by [2,5]), you might accidentally
shrink the merged end. max() ensures the end always grows correctly.

---

## Trace
```
sorted: [[1,3],[2,6],[8,10],[15,18]]

result = [[1,3]]
interval=[2,6]: 2 <= 3 → overlap → merge → last[1]=max(3,6)=6 → result=[[1,6]]
interval=[8,10]: 8 <= 6? No → no overlap → append → result=[[1,6],[8,10]]
interval=[15,18]: 15 <= 10? No → no overlap → append → result=[[1,6],[8,10],[15,18]]
```

---

## Time & Space Complexity
- Time: O(n log n) — dominated by the sort
- Space: O(n) — for the result list

---

## Pattern
> Overlapping intervals = sort by start, merge by comparing to last merged interval's end
> Common in: meeting room scheduling, calendar conflicts, range merging

---

## LeetCode
#56 — Merge Intervals

## Your Task
Write this solution from memory before next session.
Focus on: sorting by lambda key, and the max() logic when merging.
