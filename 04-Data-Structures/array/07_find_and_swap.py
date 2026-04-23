# =================================================================
# PROBLEM: Find and Replace (Swap Value)
# QUESTION: Locate all occurrences of '10' and replace them with '100'.
# =================================================================

# Initial list with duplicate values of 10
nums = [10, 20, 50, 10, 100, 13, 10, 100]

print(f"This is old list: {nums}")

# Logic: Iterate through the list using indices
for i in range(len(nums)):
    # Check if the current element is equal to 10
    if nums[i] == 10:
        # Update the value at index 'i' directly
        nums[i] = 100

# Final output after modification
print(f"The new list is: {nums}")

# Expected Output: [100, 20, 50, 100, 100, 13, 100, 100]