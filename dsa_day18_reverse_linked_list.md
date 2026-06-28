# DSA Day 18 — Reverse a Linked List

## Problem
Given the head of a linked list, reverse it.

**Example:**
```
Input:  1 -> 2 -> 3 -> None
Output: 3 -> 2 -> 1 -> None
```

---

## What is a Linked List
Unlike an array (continuous memory block), a linked list is a chain of
separate nodes. Each node holds a VALUE and a pointer to the NEXT node.

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
```

---

## Solution — Iterative Pointer Reversal (O(n))

```python
def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next   # save where we're going BEFORE losing it
        current.next = prev         # flip the arrow backward
        prev = current               # move prev forward
        current = next_node          # move current forward
    
    return prev   # prev is now the new head
```

---

## The "Kids in a Line" Mental Model

Imagine 3 kids holding hands facing forward: 1 -> 2 -> 3
Goal: make them face backward, WITHOUT moving where any kid stands -
only change who's holding whose hand.

- Before flipping each kid's hand, PEEK AHEAD and remember who they
  were originally holding (next_node) - otherwise you lose your path forward
- Flip their hand to point backward (to prev)
- That kid becomes the new "prev"
- Walk forward to whoever you remembered (next_node becomes current)

KEY INSIGHT: No kid (node) ever changes position in memory.
Only the .next pointers (who's holding whose hand) get rewired.

---

## Full Trace — 1 -> 2 -> 3 -> None

```
Start: prev=None, current=Node(1)

Iter 1: next_node=Node(2) -> Node(1).next=None -> prev=Node(1) -> current=Node(2)
        State: None <- 1     2 -> 3 -> None

Iter 2: next_node=Node(3) -> Node(2).next=Node(1) -> prev=Node(2) -> current=Node(3)
        State: None <- 1 <- 2     3 -> None

Iter 3: next_node=None -> Node(3).next=Node(2) -> prev=Node(3) -> current=None
        State: None <- 1 <- 2 <- 3

Loop stops (current is None). Return prev = Node(3) = new head.
Result: 3 -> 2 -> 1 -> None
```

---

## Why next_node is essential
If you do `current.next = prev` BEFORE saving next_node, you permanently
destroy the only connection to the rest of the original list. You'd have
no way to move forward - completely lost.

ALWAYS: peek ahead and save -> THEN flip -> THEN move forward.

---

## Common mistake to avoid
Don't "just swap the values" inside nodes (collecting all values into
an array, then overwriting). This technically produces correct output
but misses the entire point of the exercise - interviewers want to see
POINTER manipulation, since that's the unique skill linked lists test
that arrays don't have at all. It's also less efficient (extra O(n) space
for the array).

---

## Time & Space Complexity
- Time: O(n) — one pass through the list, each node visited once
- Space: O(1) — only 3 variables (prev, current, next_node) regardless of list size

---

## Pattern
> Linked list reversal = three-pointer technique (prev, current, next_node)
> This exact 3-pointer pattern extends to: reverse part of a list,
> detect cycles, find middle of a list

---

## LeetCode
#206 — Reverse Linked List

## Your Task
Write this solution from memory before next session.
Focus on: the ORDER of operations inside the loop (save next_node FIRST, always).
