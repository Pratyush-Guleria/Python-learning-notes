# =================================================================
# PROBLEM: Roman to Integer (LeetCode #13)
# DESCRIPTION: Convert a Roman numeral string to an integer.
# LOGIC: Hash Map (Dictionary) + Left-to-Right Scan.
#        If current value < next value, subtract it. Otherwise, add it.
# =================================================================

def roman_to_int(s):
    # Dictionary to store Roman numeral values
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    
    for i in range(len(s)):
        # Check if the current numeral is smaller than the next one
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
            # Subtractive Case: e.g., IV (1 < 5) -> Subtract 1
            total -= roman_map[s[i]]
        else:
            # Standard Case: Add the value
            total += roman_map[s[i]]
            
    return total

# --- TESTING ---
test_string = "MCMXCIV" # Expected: 1994
print(f"Roman Numeral: {test_string}")
print(f"Integer Value: {roman_to_int(test_string)} 🏆")
