# =================================================================
# PROBLEM: Two Sum (Brute Force Approach)
# QUESTION: Given an array of integers 'nums' and an integer 'target', 
#           find the indices of two numbers such that they add up to the target.
# =================================================================

# Input data
nums = [2, 7, 11, 15]
target = 26

# Logic: Using Nested Loops to find the pair
# Outer loop picks the first number (i)
for i in range(len(nums)):
    
    # Inner loop picks the second number (j)
    # Start j from 'i + 1' to avoid duplicate pairs and using the same element twice
    for j in range(i + 1, len(nums)):
        
        # Check if the sum of elements at index i and j equals the target
        if nums[i] + nums[j] == target:
            print(f"Target found: {nums[i]} (Index {i}) + {nums[j]} (Index {j}) = {target}")
            
            # Professional Output as a list of indices
            result = [i, j]
            print(f"Resulting Indices: {result}")

# Expected Output: Resulting Indices: [2, 3]
