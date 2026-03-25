"""
Topic: Logical Operators in Python
"""

# AND operator
# Returns True only if both conditions are True

age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Allowed")
else:
    print("Not allowed")


# OR operator
# Returns True if at least one condition is True

is_student = True
age = 55

if age >= 50 or is_student:
    print("You get discount")


# NOT operator
# Reverses the condition

is_sunny = False

if not is_sunny:
    print("It is cloudy")