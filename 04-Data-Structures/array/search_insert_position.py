# =================================================================
# PROBLEM: Search Insert Position (LeetCode #35)
# DESCRIPTION: Given a sorted array and a target value, return the 
#              index if the target is found. If not, return the 
#              index where it would be if it were inserted in order.
# COMPLEXITY: O(log n) - Binary Search Approach
# =================================================================

# 1. Define Input Data
nums = [1, 2, 3, 4, 5, 6]
target = 7

print(f"Input Array: {nums}")
print(f"Target Value: {target}")

# 2. Binary Search Logic
low = 0
high = len(nums) - 1
found_index = -1

while low <= high:
    # Finding the middle index
    mid = (low + high) // 2
    
    if nums[mid] == target:
        found_index = mid
        break  # Target found, exit the loop
    
    elif nums[mid] < target:
        # Target is larger, discard the left half
        low = mid + 1
        
    else:
        # Target is smaller, discard the right half
        high = mid - 1

# 3. Final Output Logic
if found_index != -1:
    print(f"Success: Target found at Index {found_index} 🏆")
else:
    # If not found, the 'low' pointer naturally points to the correct insert position
    print(f"Target not found. It should be inserted at Index: {low} 📍")

# =================================================================
# PRO TIP: The 'low' pointer ends up at the correct insertion 
#          point because it moves past all elements smaller than 
#          the target.
# =================================================================
