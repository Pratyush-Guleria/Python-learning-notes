# =================================================================
# PROBLEM: Find Minimum Element
# QUESTION: Identify the smallest number in the list and its position.
# =================================================================

# Defining a list of integers
nums = [45, 12, 89, 5, 67, 2, 30]

# 1. Initialize min_value with the first element
min_value = nums[0]
min_index = 0

# 2. Iterate through the entire list using its length
for i in range(len(nums)):
    # 3. If current element is smaller than min_value, update it
    if nums[i] < min_value:
        min_value = nums[i]
        min_index = i

# 4. Final Output showing the result
print(f"The Minimum Value is {min_value} at Index {min_index}")

# Expected Output: The Minimum Value is 2 at Index 5