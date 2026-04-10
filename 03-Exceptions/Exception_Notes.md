 pratyushguleria@Pratyushs-MacBook-Air  ~  cd
 pratyushguleria@Pratyushs-MacBook-Air  ~  clear
  UW PICO 5.09                                                           New Buffer









# ⚠ ️ Exception Handling in Python

## 🧠 What are Exceptions?

Exceptions are **unexpected errors** that occur during program execution.

👉 Without handling:
- Program crashes ❌

👉 With handling:
- Program runs safely ✅

---

## 🔹 Why do we use Exception Handling?

- Prevent program crash
- Handle user input errors
- Make code robust and professional

---

## 🧩 Basic Structure

```python

try:
    # Code that may cause error
except:
    # Runs if error occurs

```

# 🔹 try Block
The try block contains code that might cause an error.

```python

try:
    num = int(input("Enter a number: "))

```
:
👉 Example problem:
		• User enters text instead of number → ❌ crash

# 🔹 except Block
The except block runs when an error occurs in try.

```python

try:
    num = int(input("Enter a number: "))
except:
    print("Invalid input")

```

# 🎯 Handling Specific Errors
Instead of catching all errors, we can catch specific ones:

```python

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number")

```

# ⚡ Catching Multiple Errors

```python

try:
    num = int(input())
    result = 10 / num
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")

```

# 🧠 Catching All Errors (Advanced but useful)

```python

try:
    num = int(input())
except Exception as e:
    print(f"Error occurred: {e}")

```
👉 as e means:
	•	Store error in variable e
	•	Helps in debugging


# 🔹 else Block
The else block runs only if NO error occurs.

```python

try:
    num = int(input())
except ValueError:
    print("Invalid input")
else:
    print("Input successful")

```

# 🔹 finally Block
The finally block always runs, no matter what.

```python

try:
    num = int(input())
except:
    print("Error")
finally:
    print("Program ended")

```
👉 Used for:
	•	Closing files
	•	Cleaning resources


# 🔥 raise Keyword
Used to manually create an exception.

```python

age = int(input("Enter age: "))

if age < 0:
    raise ValueError("Age cannot be negative")

```

