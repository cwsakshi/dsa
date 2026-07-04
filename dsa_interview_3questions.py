# DSA Interview Practice — 3 Questions

## Question 1: Two Sum (Hashmap)
```python
nums = [2, 7, 11, 15]
target = 9
seen = {}

for i in range(len(nums)):    # range(len(nums)) for INDICES, not 'for i in nums'
    need = target - nums[i]
    if need in seen:
        print(seen[need], i)
        break                  # always break after finding answer
    seen[nums[i]] = i

# Output: 0 1
```

## Question 2: Maximum Subarray — Kadane's Algorithm
```python
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
current_sum = 0
max_sum = nums[0]

for num in nums:
    current_sum = max(num, current_sum + num)   # max(num, ...) NOT max(current_sum, ...)
    max_sum = max(current_sum, max_sum)

print(max_sum)  # 6  (subarray [4,-1,2,1])
```

## Question 3: Find All Anagrams in a String
```python
from collections import Counter

s = "cbaebabacd"
p = "abc"

p_count = Counter(p)
window_count = Counter()
result = []
k = len(p)

for i in range(len(s)):
    char = s[i]                          # char = s[i], NOT just 'char' from previous loop
    window_count[char] += 1
    
    if i >= k:
        old_char = s[i - k]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]
    
    if window_count == p_count:
        result.append(i - k + 1)

print(result)  # [0, 6]
```

## Common mistakes caught today:
# 1. Two Sum: 'for i in nums' gives VALUES not INDICES -> use range(len(nums))
# 2. Kadane's: max(current_sum, current_sum+num) never resets -> use max(num, current_sum+num)
# 3. Anagrams: using 'char' from previous loop -> always use s[i] inside the window loop
