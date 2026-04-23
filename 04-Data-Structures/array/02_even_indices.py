# =================================================================
# PROBLEM: Find Indices of Even Numbers
# QUESTION: Identify all even numbers in a list and print their positions.
# =================================================================

# Defining a list with mixed even and odd numbers

nums = [12, 19, 32, 23, 34, 84]

# Loop through each index of the list

for i in range(len(nums)):

    # Use modulo operator (%) to check for even numbers (divisible by 2)
    if nums[i] % 2 ==0:
        print(f"Even Number {nums[i]} detected at Index: {i}")

# Even Number 12 detected at Index: 0
# Even Number 32 detected at Index: 2
# Even Number 34 detected at Index: 4
# Even Number 84 detected at Index: 5