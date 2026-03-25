"""
Topic: Rounding in Python
Author: Pratyush
"""

# -----------------------------
# What is Rounding?
# -----------------------------
# Rounding converts a number to its nearest value
# It can remove decimal places or round to specific digits

# Syntax:
# round(number, digits)


# Example 1: Basic Rounding

num = 5.5
result = round(num)

print(result)  # Output: 6


# Example 2: Rounding to 2 decimal places

num = 5.459
result = round(num, 2)

print(result)  # Output: 5.46


# Example 3: Rounding to nearest 10

num = 674
result = round(num, -1)

print(result)  # Output: 670


# Example 4: Rounding to nearest 100

result = round(num, -2)
print(result)  # Output: 700