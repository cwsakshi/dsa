# LeetCode Solutions — July 5, 2026

## #121 — Best Time to Buy and Sell Stock ✅ Accepted (Runtime 0ms)

### Problem
Given prices array, find the maximum profit from one buy and one sell.
Must buy before you sell. Return 0 if no profit possible.

### Key Insight
Walk through prices left to right, tracking:
1. Minimum price seen so far (best day to buy)
2. Profit if you sell TODAY = current_price - min_price
3. Maximum profit seen across all days

### Solution
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')   # infinity - any real price will be smaller
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)      # update cheapest buy day
            profit = price - min_price             # profit if sell today
            max_profit = max(max_profit, profit)   # track best profit
        
        return max_profit   # OUTSIDE the loop
```

### Trace — prices = [7,1,5,3,6,4]
```
Day 1: price=7 -> min=7,  profit=0, max_profit=0
Day 2: price=1 -> min=1,  profit=0, max_profit=0
Day 3: price=5 -> min=1,  profit=4, max_profit=4
Day 4: price=3 -> min=1,  profit=2, max_profit=4
Day 5: price=6 -> min=1,  profit=5, max_profit=5  <- best
Day 6: price=4 -> min=1,  profit=3, max_profit=5
Answer: 5
```

### Why float('inf')
infinity means "I haven't seen any price yet, so anything will be cheaper."
min(infinity, 7) = 7 -> first real price automatically replaces it.
Alternative: min_price = prices[0] (also valid)

### Common mistakes
- Returning inside the loop (returns after first price only)
- Initializing min_price = 0 (can cause wrong results)

### Time & Space: O(n) time, O(1) space

---

## #70 — Climbing Stairs ✅ Accepted (Runtime 0ms, Beats 100%)

### Problem
n steps, can climb 1 or 2 steps at a time.
How many distinct ways to reach the top?

### Key Insight
This IS Fibonacci — to reach step n, you either:
- Came from step n-1 (took 1 step) → ways(n-1)
- Came from step n-2 (took 2 steps) → ways(n-2)
So: ways(n) = ways(n-1) + ways(n-2)

### Solution (with memoization)
```python
class Solution:
    def climbStairs(self, n: int, ways={}) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in ways:
            return ways[n]
        ways[n] = self.climbStairs(n-1, ways) + self.climbStairs(n-2, ways)
        return ways[n]
```

### Base cases — different from Fibonacci!
- n=1 -> 1 way  (just [1])
- n=2 -> 2 ways ([1+1] or [2])
- NOT n<=1 return n like Fibonacci — this gives wrong answer for n=2

### Why return n is WRONG (even though it passed)
n=1 -> return 1 ✅ (coincidence)
n=2 -> return 2 ✅ (coincidence)
n=3 -> return 3 ✅ (coincidence)
n=4 -> return 4 ❌ (correct answer is 5)
n=5 -> return 5 ❌ (correct answer is 8)
Always write the full memoized solution in real interviews.

### Time & Space: O(n) time, O(n) space (memo dict)
