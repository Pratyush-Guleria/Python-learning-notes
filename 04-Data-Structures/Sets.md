# 🧩 Sets in Python

## 🔹 What is a Set?

A **set** is a collection used to store multiple items in a single variable.

👉 It is:
- Unordered (no fixed sequence)
- Mutable (can be changed)
- Does NOT allow duplicate values
- Not indexed (no indexing or slicing)

---

## 🔹 Creating a Set

We use **curly braces `{}`** to create a set.

```python

numbers = {1, 2, 3, 4}
print(numbers)

```

# 🔹 No Duplicate Values ⚠️
👉 Sets automatically remove duplicates.

```python

numbers = {1, 2, 2, 3, 4, 4}
print(numbers)  # Output: {1, 2, 3, 4}

```

# 🔹 Unordered Nature
👉 Elements do NOT follow a fixed order.

```python

names = {"John", "Bob", "Sam"}
print(names)

```
💡 Output order may change every time.

# 🔹 No Indexing ❌
👉 You cannot access elements using index.

```python

numbers = {1, 2, 3}

print(numbers[0])  # ❌ ERROR

```

# 🔹 Adding Elements

```python

numbers = {1, 2, 3}

numbers.add(4)
print(numbers)

```

# 🔹 Removing Elements

```python

numbers = {1, 2, 3}

numbers.remove(2)
print(numbers)

```

# 🔹 Looping Through a Set

```python

numbers = {1, 2, 3}

for num in numbers:
    print(num)

```

# 🔹 Length of Set

```python

numbers = {1, 2, 3}
print(len(numbers))  # Output: 3

```

🔹 Empty Set (Important ⚠️)

```python

empty = set()   # ✅ Correct way
print(type(empty))  # set

```

❌ Wrong:

```python

empty = {}
print(type(empty))  # dict

```

⸻

# 🔹 Why Use Sets?

Use sets when:
	•	You want unique values only
	•	You don’t care about order
	•	You need fast membership checking