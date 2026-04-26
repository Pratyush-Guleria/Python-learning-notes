# =================================================================
# PROBLEM: Binary Search (LeetCode #704)
# DESCRIPTION: Searching for a target value in a sorted array 
#              with O(log n) time complexity.
# =================================================================

# 1. Define Input Data
nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(f"Input Array: {nums}")
print(f"Target Value: {target}")

# 2. Binary Search Logic (The Algorithm)
low = 0
high = len(nums) - 1
result_index = -1  # Default if target is not found

while low <= high:
    # Calculate the middle index
    mid = (low + high) // 2 
    
    # CASE 1: Target found at mid
    if nums[mid] == target:
        result_index = mid
        break  # Exit loop immediately
        
    # CASE 2: Target is larger, ignore left half
    elif nums[mid] < target:
        low = mid + 1
        
    # CASE 3: Target is smaller, ignore right half
    else:
        high = mid - 1

# 3. Display the Results
if result_index != -1:
    print(f"Success: Target found at Index {result_index}")
else:
    print("Error: Target not found in the array")

# =================================================================
# EFFICIENCY NOTE: 
# This algorithm runs in O(log n) time, making it much faster 
# than a linear search for large datasets.
# =================================================================
