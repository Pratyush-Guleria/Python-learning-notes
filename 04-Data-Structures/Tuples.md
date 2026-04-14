# 📦 Tuples in Python

## 🔹 What is a Tuple?

A **tuple** is a collection used to store multiple items in a single variable.

👉 It is:
- Ordered  
- Immutable (cannot be changed after creation)  
- Allows duplicate values  

---

## 🔹 Creating a Tuple

We use **round brackets `()`** to create a tuple.

```python

names = ("John", "Bob", "Sam")
print(names)

```
## 🔹 Accessing Elements

Tuples use indexing (starting from 0).

```python

names = ("John", "Bob", "Sam")

print(names[0])   # Output: John
print(names[-1])  # Output: Sam

```

## 🔹 Immutability (Important ⚠️)

👉 Tuples cannot be changed after creation.

```python

names = ("John", "Bob", "Sam")

names[0] = "Jon"   # ❌ ERROR

```
💡 This will give an error because tuples are immutable.

## 🔹 Length of Tuple

```python

names = ("John", "Bob", "Sam")
print(len(names))   # Output: 3

```

## 🔹 Looping Through a Tuple

```python

names = ("John", "Bob", "Sam")

for name in names:
    print(name)

```

## 🔹 Tuple with One Item (Important ⚠️)

```python

single = ("Hello",)
print(type(single))  # tuple

```

❌ Without comma:

```python

single = ("Hello")
print(type(single))  # str

```

# 🔹 Why Use Tuples?

Use tuples when:
	•	Data should not change
	•	You want faster performance than lists
	•	You want fixed data (like coordinates, config values)
