# Scope: Local vs Global

## What is Scope?

Scope means:
- Where a variable is accessible
- How long a variable exists

---

## 1. Local Scope

A local variable:
- Is created inside a function
- Can only be used inside that function

Example:

def your_name():
    name = "Pratyush"
    print(name)

your_name()

If we try:
print(name)

It will give an error because `name` exists only inside the function.

---

## 2. Global Scope

A global variable:
- Is declared outside the function
- Can be accessed inside and outside functions

Example:

display_name = "XYZ"

def who():
    print(display_name)

who()
print(display_name)

Here:
- display_name is global
- It can be accessed everywhere