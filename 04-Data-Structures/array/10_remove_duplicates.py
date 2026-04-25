# =================================================================
# PROBLEM: Remove Duplicates from Sorted Array
# QUESTION: Given a sorted list, remove the duplicates in-place 
#           so that each element appears only once.
# =================================================================

# 1. Defining the Input List (Sorted)
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(f"Original List: {nums}")

# 2. Logic: The Two-Pointer Approach
# 'k' is the position where the next unique element will be placed
k = 1 

for i in range(1, len(nums)):
    # Comparing current element with the previous one
    if nums[i] != nums[i-1]:
        nums[k] = nums[i] # Shifting unique element to index 'k'
        k += 1            # Moving 'k' to the next seat

# 3. Output the Results
print(f"Number of unique elements: {k}")
print(f"Updated List (Unique elements only): {nums[:k]}")

# =================================================================
# RESULT: The first k elements of 'nums' now contain unique values.
# =================================================================
