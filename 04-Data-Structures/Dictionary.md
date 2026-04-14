# 📚 Dictionaries in Python

## 🔹 What is a Dictionary?

A **dictionary** is a collection used to store data in **key-value pairs**.

👉 It is:
- Mutable (can be changed)
- Unordered (no fixed sequence)
- Stores data as `key : value`
- Keys must be unique

---

## 🔹 Creating a Dictionary

We use **curly braces `{}`** with key-value pairs.

```python

person = {
    "name": "John",
    "age": 25,
    "city": "Delhi"
}

print(person)

```

# 🔹 Accessing Values
👉 We use keys to access values.

```python

person = {
    "name": "John",
    "age": 25
}

print(person["name"])  # Output: John

```

# 🔹 Adding / Updating Values

```python

person = {
    "name": "John",
    "age": 25
}

person["age"] = 30      # Update
person["city"] = "Delhi"  # Add

print(person)

```

# 🔹 Removing Items

```python 

person = {
    "name": "John",
    "age": 25
}

person.pop("age")
print(person)

```

# 🔹 Looping Through Dictionary

```python 

person = {
    "name": "John",
    "age": 25
}

for key in person:
    print(key, person[key])

```

# 🔹 Length of Dictionary

```python

person = {
    "name": "John",
    "age": 25
}

print(len(person))  # Output: 2

```

# 🔹 Keys Must Be Unique ⚠️

```python

data = {
    "name": "John",
    "name": "Bob"
}

print(data)  # Output: {'name': 'Bob'}

```
👉 Duplicate keys overwrite previous values.

# 🔹 Different Data Types

```python

data = {
    "name": "John",
    "age": 25,
    "is_student": True
}

```
👉 Values can be of any data type.


# 🔹 Why Use Dictionaries?

Use dictionaries when:
	•	You need mapping (key → value)
	•	You want fast lookup by key
	•	Data has labels (like name, age, etc.)