# 🔗 Logical Operators in Python

## 🧠 What are Logical Operators?
Logical operators are used to **combine multiple conditions** and return a single True/False result.

👉 They are mainly used in:
- Decision making  
- Conditions (`if`, `elif`, `else`)  
- Real-world logic building  

---

## 🎯 Why are they important?
- Help in writing complex conditions  
- Used in authentication systems, filtering, validations  
- Foundation for real-world programming logic  

---

# 📌 Types of Logical Operators

## 1. 🔒 AND Operator (`and`)

👉 Returns **True only if both conditions are True**

---

### Example:

```python

age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Allowed")
else:
    print("Not allowed")

```

## 2. 🔓 OR Operator (or)

👉 Returns True if at least one condition is True

---

### Example:

```python

is_student = True
age = 55

if age >= 50 or is_student:
    print("You get discount")
else:
    print("No discount")

```

## 3. 🔄 NOT Operator (not)

👉 Reverses the condition
(True → False, False → True)

---

### Example:

```python

is_sunny = False

if not is_sunny:
    print("It is cloudy")

```