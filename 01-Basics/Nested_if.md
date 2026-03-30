# 🧩 Nested If in Python

## 🧠 What is Nested If?
Nested if means:
👉 **an `if` statement inside another `if` statement**

---

## 🎯 Why do we use Nested If?
- Jab multiple conditions check karni ho step-by-step  
- Jab ek condition ke andar aur checks karne ho  
- Real-world decision making ke liye  

---

# 📌 Basic Example

```python

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

```

### Another Example :

```python

age = 16
has_ticket = True

if age > 0:
    if age >= 18:
        if has_ticket:
            print("Entry allowed")
        else:
            print("Ticket required")
    else:
        print("You are underage")
else:
    print("Invalid age")

```

### Another Example :

```python

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Invalid username")

```

# 🔥 Pro Tip (VERY IMPORTANT)

### 👉 Deep nesting = bad practice sometimes ❌
### 👉 Instead use:

```python

if age > 0 and age >= 18 and has_ticket:
    print("Entry allowed")
else:
    print("Not allowed")

```

# ⚡ When to Use Nested If?

✔ When conditions depend on each other
✔ When step-by-step validation needed
✔ When logic cannot be simplified