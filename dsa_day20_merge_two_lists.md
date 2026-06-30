# DSA Day 20 — Merge Two Sorted Lists

## Problem
Merge two sorted linked lists into one sorted list.

**Example:**
```
List 1: 1 -> 3 -> 5
List 2: 2 -> 4 -> 6
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
```

---

## Solution — Dummy Node + Pointer Walking (O(n+m))

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_two_lists(l1, l2):
    dummy = ListNode(0)   # throwaway placeholder node
    current = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # attach whichever list still has leftover nodes
    current.next = l1 if l1 else l2
    
    return dummy.next   # skip the dummy, return the real head
```

---

## The Dummy Node Trick

**Problem without dummy:** the very FIRST node attached needs special
handling (nothing exists yet to attach to), but every node AFTER that
needs different handling (attach to current.next). This requires an
ugly `if result_head is None:` special case.

**With dummy:** `current` starts pointing at a throwaway node (value=0,
never used). Now even the FIRST real node follows the EXACT SAME rule
as every other node: `current.next = smaller_node`. No special case needed.

```
Before: dummy -> None
After:  dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
return dummy.next  -> skips dummy, gives the real first node
```

---

## How it works
- Walk both lists simultaneously with two pointers (l1, l2)
- Always pick whichever current node has the SMALLER value
- Attach it, advance that list's pointer, advance current
- When one list runs out, attach whatever's LEFT in the other list directly

---

## Time & Space Complexity
- Time: O(n + m) — one pass through both lists combined (n and m = list lengths)
- Space: O(1) — reusing existing nodes, not creating new ones (just rewiring)

---

## Pattern
> Merging two sorted sequences = walk both with pointers, always take the smaller
> Dummy node pattern = use a placeholder to avoid special-casing "the first element"
> This pattern extends to: merge sort's merge step, merge k sorted lists

---

## LeetCode
#21 — Merge Two Sorted Lists

## Your Task
Write this solution from memory before next session.
Focus on: why the dummy node removes the need for a first-node special case.
