# 📦 Arrays (Concept Understanding)

> Note: In Python, we don't use traditional arrays like in C/C++.
> Instead, we use **lists**, which are more flexible.

---

## 🧠 What is an Array?

An array is a data structure that stores multiple values in a single variable.

In low-level languages (like C/C++):
- All elements must be of the same type
- Size is fixed
- Memory is continuous

---

## 🐍 Arrays in Python

Python does not use strict arrays by default.  
Instead, it provides:

### 👉 List (Most Common)

```python
arr = [1, 2, 3, 4]
```

✔ Can store different data types
✔ Dynamic size (can grow/shrink)
✔ Easy to use

```python
arr = [1, "hello", 3.14, True]  # valid in Python
```

👉 Real Array (from array module)

```python
import array

arr = array.array('i', [1, 2, 3])
```

✔ Only same data type allowed
✔ More memory efficient than lists

⸻

## ⚙️ Operations on Arrays / Lists

### 🔹 Access element

```python
arr[0]
```

### 🔹 Update element

```python
arr[1] = 10
```

### 🔹 Delete element

```python
arr.pop(1)      # remove by index
arr.remove(3)   # remove by value
```

## ⚠️ Memory Concept

* Python lists use dynamic memory allocation
* Sometimes extra memory is reserved for future growth
* This avoids frequent resizing

⸻

## ❗ Common Mistakes

❌ Thinking Python list = C array
❌ Assuming fixed size
❌ Assuming same data type only

✔ Python list is more flexible than traditional arrays

## 🧠 Summary

* Arrays = fixed, same type (low-level languages)
* Lists = dynamic, flexible (Python)
* Use lists in most real-world Python code