# PROBLEM: Count Occurrences
# QUESTION: Count how many times the target number appears in the list.

nums = [10, 40, 20, 10, 32, 10]
target = 10
count = 0

# Loop through the list to find the target
for i in range(len(nums)):
    if nums[i] == target:
        # Increment the counter if a match is found
        count += 1

print(f"The number {target} appeared {count} times in the list.")