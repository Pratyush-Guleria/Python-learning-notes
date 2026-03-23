# Conditional Statements

## What are if, elif, else?

These are decision-making statements in Python.

They help the program decide:
- What to execute
- Based on conditions

---

## Example 1

age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
elif age < 0:
    print("Invalid age")
else:
    print("You must be 18+ to vote")

---

## Example 2

response = input("Do you want food? (Y/N): ")

if response == "Y":
    print("Have some food")
else:
    print("Okay, no food.")