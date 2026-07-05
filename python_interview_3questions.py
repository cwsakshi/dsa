# Python Interview Practice — 3 Questions

## Question 1: List Comprehension with multiple conditions
# Find numbers divisible by BOTH 2 and 3 (use 'and', not 'or')

numbers = [1, 6, 9, 12, 15, 18, 20, 24]
result = [num for num in numbers if num % 2 == 0 and num % 3 == 0]
print(result)  # [6, 12, 18, 24]

# Common mistake: using 'or' instead of 'and'
# 'or' returns numbers divisible by 2 OR 3 -> [6, 9, 12, 15, 18, 20, 24]
# 'and' returns numbers divisible by BOTH -> [6, 12, 18, 24]


## Question 2: Dictionary Comprehension
# Create a dict where key = word, value = its length

words = ["python", "sql", "ai", "langchain", "groq"]
result = {word: len(word) for word in words}
print(result)
# {'python': 6, 'sql': 3, 'ai': 2, 'langchain': 9, 'groq': 4}

# Syntax: {key: value for item in iterable}
# Similar to list comprehension but creates a dict, uses {} and key:value pair


## Question 3: Top 3 Most Frequent Numbers

nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
k = 3

# Manual version (shows understanding of logic):
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
result = [item[0] for item in sorted_items[:k]]
print(result)  # [4, 1, 3]

# Counter version (cleaner, shows Python fluency):
from collections import Counter
result = [item[0] for item in Counter(nums).most_common(k)]
print(result)  # [4, 1, 3]

# Know BOTH versions:
# Manual -> for interviews asking "without libraries"
# Counter -> for real code and when they just want the solution
