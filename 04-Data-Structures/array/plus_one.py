# =================================================================
# PROBLEM: Plus One (LeetCode #66)
# DESCRIPTION: Given a large integer represented as an array of digits, 
#              increment the integer by one and return the resulting array.
# COMPLEXITY: O(n) - Single pass through the array
# =================================================================

def plus_one(digits):
    # We iterate backwards from the last digit
    for i in range(len(digits) - 1, -1, -1):
        # If current digit is less than 9, just add 1 and return
        if digits[i] < 9:
            digits[i] += 1
            return digits
        
        # If digit is 9, it becomes 0 (carry over to next index)
        digits[i] = 0
        
    # EDGE CASE: If all digits were 9 (e.g., [9, 9, 9])
    # We reached here because the loop finished without returning
    # So we insert '1' at the beginning (making it [1, 0, 0, 0])
    digits.insert(0, 1)
    return digits

# --- TESTING LOCALLY ---
input_digits = [1, 2, 9]
print(f"Input: {input_digits}")

result = plus_one(input_digits)
print(f"Result: {result} 🏆")

# Test with Edge Case [9, 9, 9]
edge_case = [9, 9, 9]
print(f"\nEdge Case Input: {edge_case}")
print(f"Edge Case Result: {plus_one(edge_case)} 🚀")
