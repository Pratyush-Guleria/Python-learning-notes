# 📦 Lists in Python

## 🧠 What is a List?
A list is a collection of multiple items stored in a single variable.

👉 Lists are:
- Ordered  
- Mutable (can be changed)  
- Allow duplicate values  

---

## 🎯 What problem do they solve?
- Store multiple values in one variable  
- Easy data management  
- Used in almost every real-world program  

---

## 📌 Creating a List

```python

names = ["John", "Bob", "Richu", "Sam", "Mary"]
print(names)      # Output: ["John", "Bob", "Richu", "Sam", "Mary"]

```
## 📌 Accessing Elements (Indexing)

```python

names = ["John", "Bob", "Richu", "Sam", "Mary"]

print(names[0])   # Output: John

```
>⚠️ Important :- Index starts form 0

## 📌 Negative Indexing

```python

names = ["John", "Bob", "Richu", "Sam", "Mary"]
print(names[-1])  # Output: Mary

```
>⚠️ Important :- -1 means last element.


## 📌 Updating List (Mutable Nature)

```python

names = ["John", "Bob", "Richu", "Sam", "Mary"]

names[0] = "Jon"
print(names).     # Output: ["Jon", "Bob", "Richu", "Sam", Mary"]

```

>⚠️ Important :- Lists can be modified after creation.


## 📌 Slicing (Range Selection)

```python

names = ["John", "Bob", "Richu", "Sam", "Mary"]

print(names[0:3])   # Output : ["John", "Bob", "Richu"]

```

# ⚙️ List Methods

## 📌 1. append()

```python 

numbers = [1, 2, 3, 4, 5]

numbers.append(6)
print(numbers)      # Output : [1, 2, 3, 4, 5, 6]

```

>⚠️ Important :- .append() Adds element at the end.

## 📌 2. insert()

```python

numbers = [1, 2, 3, 4, 5]

numbers.insert(0, -10)
print(numbers)      # Output : [-10, 1, 2, 3, 4, 5]

```

>⚠️ Important :- insert() Adds element at a specific index.

## 📌 3. remove()

```python

numbers = [1, 2, 3, 4, 5]

numbers.remove(2)
print(numbers)      # Output : [1, 3, 4, 5]

```
>⚠️ Important :- Removes the first occurrence of the value.