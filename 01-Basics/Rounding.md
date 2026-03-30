# 🔢 Rounding in Python

---

## 🧠 What is Rounding?
Rounding means converting a number to its **nearest value**.

👉 It is used to:
- Reduce decimal places  
- Make numbers more readable  
- Get approximate values  

---

## 🎯 Why is it important?
- Used in finance (prices, taxes)  
- Used in data science (clean data)  
- Improves readability of numbers  

---

# 📌 Syntax

```python

round(number, digits)

```

### 📌 Example 1: Basic Rounding

```python

num = 5.5
result = round(num)

print(result)  # Output: 6

```
👉 Rounds to nearest integer

### 📌 Example 2: Decimal Places

```python

num = 5.459
result = round(num, 2)

print(result)  # Output: 5.46

```
👉 Keeps 2 digits after decimal

### 📌 Example 3: Nearest 10

```python

num = 674
result = round(num, -1)

print(result)  # Output: 670

```
👉 -1 means round to nearest 10

### 📌 Example 4: Nearest 100

```python

num = 674
result = round(num, -2)

print(result)  # Output: 700

```
👉 -2 means round to nearest 100

⚠️ Important Concept (Banker’s Rounding)

```python

print(round(2.5))  # Output: 2
print(round(3.5))  # Output: 4

```
👉 Python uses “Banker’s Rounding”:
	•	Nearest even number is chosen