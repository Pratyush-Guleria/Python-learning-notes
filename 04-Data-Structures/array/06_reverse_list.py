# =================================================================
# PROBLEM: Reverse List
# QUESTION: Print all elements of the list in reverse order using a loop.
# =================================================================

nums = [10, 20, 30, 40, 50]

print("Printing list in reverse order:")

# range(start index, stop index, step)
for i in range(len(nums) - 1, -1, -1):
    print(f"Value at Index {i}: {nums[i]}")
    pass