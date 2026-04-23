# PROBLEM: Find Maximum Element
# QUESTION: Identify the largest number in the list and its position.

nums = [15, 42, 8, 91, 23]

# 1. Assume the first element is the maximum
max_val = nums[0]
max_index = 0

# 2. Iterate through the list
for i in range(len(nums)):
    # 3. Compare current element with max_val
    if nums[i] > max_val:
        # 4. If current element is bigger, update max_val and max_index
        max_val = nums[i]
        max_index = i

# 5. Final Output
print(f"The Maximum Value is {max_val} at Index {max_index}")
