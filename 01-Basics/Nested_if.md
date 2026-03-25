"""
Topic: Nested If
"""

age = 22
has_ticket = True

if age > 0:

    if age >= 18:

        if has_ticket:
            print("Entry allowed")
        else:
            print("Ticket required")

    else:
        print("You must be 18+")

else:
    print("Invalid age")