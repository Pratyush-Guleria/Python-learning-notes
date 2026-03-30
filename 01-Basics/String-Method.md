# 🔤 String Methods in Python

## 🧠 What are String Methods?
String methods are **built-in functions** used to:

- Modify strings  
- Transform data  
- Clean user input  
- Analyze text  

👉 Strings are everywhere → user input, files, APIs, ML data  

---

## 🎯 Why are they important?
- Clean messy input (very common)  
- Format data properly  
- Used in real-world apps (login, forms, search, etc.)  

---

# 📌 1. strip()

👉 Removes whitespace from both sides of a string

```python

name = input("Enter your name: ")
name = name.strip()

print(f"Hello, {name}")

```

## 📌 2. capitalize()
👉 Makes the first letter uppercase

```python

name = input("Enter your name: ")
name = name.capitalize()

print(name)

```

## 📌 3. title()
👉 Makes the first letter of every word uppercase

```python

name = input("Enter your name: ")
name = name.title()

print(name)

```

## 📌 4. lower() and upper()
👉 Convert entire string to lowercase or uppercase

```python

name = input("Enter your name: ")

print(name.lower())
print(name.upper())

```

## 📌 5. Method Chaining 🔥
👉 Multiple methods in one line

```python

name = input("Enter your name: ").strip().title()

print(name)

```

👉 Order matters:
	•	First .strip() → removes spaces
	•	Then .title() → formats text


## 📌 6. split()
👉 Splits string into multiple parts

```python

first, last = input("Enter your full name: ").split(" ")

print(f"First name: {first}")
print(f"Last name: {last}")

```

## 📌 7. replace()
👉 Replaces a word or character

```python

text = "I like tea"
text = text.replace("tea", "coffee")

print(text)

```

## 📌 8. find()
👉 Finds position of a character/word

```python

text = "Hello"

print(text.find("e"))  # Output: 1

```
👉 Returns -1 if not found