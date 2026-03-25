# String Methods

## What are String Methods?

String methods are built-in functions used to:
- Modify
- Transform
- Analyze
- Manipulate strings

---

## 1. strip()

Removes whitespace from both sides.

name = input("Enter your name: ")
name = name.strip()
print(f"Hello, {name}")

---

## 2. capitalize()

Makes first letter uppercase.

name = input("Enter your name: ")
name = name.capitalize()
print(name)

---

## 3. title()

Makes first letter of every word uppercase.

name = input("Enter your name: ")
name = name.title()
print(name)

---

## 4. Method Chaining

name = input("Enter your name: ").strip().title()
print(name)

We can chain multiple string methods together.

---

## 5. split()

Splits string into multiple parts.

first, last = input("Enter your full name: ").split(" ")
print(f"First name: {first}")
print(f"Last name: {last}")