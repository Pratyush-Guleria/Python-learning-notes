# ✂️ String Slicing in Python

## 🧠 What is Slicing?
Slicing is used to extract a **part (substring)** of a string.

👉 Instead of taking full string, you can take only required portion.

---

## 🎯 Why is it important?
- Extract specific data  
- Process text efficiently  
- Used in real-world apps (search, parsing, ML)  

---

# 📌 Basic Syntax

```python

string[start : end]

```

👉 start → included
👉 end → excluded


# 📌 Example 1: Basic Slicing

```python

a = "Hello world"

print(a[2:5])  # Output: llo

```
```python

👉 Index:

H  e  l  l  o     w  o  r  l  d
0  1  2  3  4     6  7  8  9  10

```

>⚠️ Important : Spaces are also counted and Index starts from 0

# 📌 Example 2: Slicing from Start

```python

b = "Hey buddy how are you"

print(b[:6])  # Output: Hey bu

```

>⚠️ Important : 👉 If start is missing → Python assumes 0

# 📌 Example 3: Slicing to the End

```python

c = "Hello World"

print(c[2:])  # Output: llo World

```

>⚠️ Important : 👉 If end is missing → Python goes till last.

# 📌 Example 4: Negative Indexing

```python

e = "Hello World"

print(e[-5:-2])  # Output: Wor

```

```python

👉 Negative index starts from end:

H  e  l  l  o     W  o  r  l  d
-11 ...          -5 -4 -3 -2 -1

```
# 📌 Example 5: Step (Advanced 🔥)

```python

text = "Python"

print(text[0:6:2])  # Output: Pto

```

👉 Step = how many jumps
👉 2 → skip every second character