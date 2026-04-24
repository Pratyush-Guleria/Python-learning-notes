# =================================================================
# PROBLEM: Remove Element (LeetCode #27)
# QUESTION: Remove all occurrences of 'val' in-place and return k.
# =================================================================

# 1. Input Data
nums = [3, 2, 2, 3]
val = 3

print(f"Original List: {nums}")

# 2. Asali Logic (The Two-Pointer Approach)
# 'k' points to the position where the next valid element should go
k = 0 

for i in range(len(nums)):
    # If current element is not the one we want to remove
    if nums[i] != val:
        nums[k] = nums[i] # Move it to the front
        k += 1            # Move the pointer forward

# 3. Final Output
print(f"Number of elements after removal: {k}")
print(f"Updated List (first k elements): {nums[:k]}")

# =================================================================
# NOTE: LeetCode uses a 'class Solution' structure, but for 
# local practice and GitHub, this simple structure is best.
# =================================================================
