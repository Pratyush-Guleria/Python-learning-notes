# =================================================================
# PROBLEM: Search an Element in an Array
# QUESTION: Given an array 'nums' and a 'target' value, find the 
#           index (position) of that target.
# =================================================================


# Defining the list of integers

nums = [10, 20, 30, 40, 50]
target = 40

# Iterate through the list using range(len()) to access indices

# Check if the element at current index matches the target

for i in range(len(nums)):

    # Check if the element at current index matches the target
    if nums[i] == target:
        print(f"Target {target} found at Index {i}")

# Expected Output: Target 40 found at Index 3
