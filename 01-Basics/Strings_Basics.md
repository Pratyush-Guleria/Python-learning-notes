# 🔤 Strings Basics in Python

## 🧠 What is a String?
A string is a sequence of characters enclosed in quotes.

👉 Example:

```python
text = "Hello"
```

## 🎯 Why are strings important?
	•	Used for user input
	•	Used in text processing
	•	Used in almost every real-world program

# 📌 1. Strings are Array-like (Indexing)
👉 Strings behave like arrays → you can access characters using index

```python

a = "Hey Buddy"

print(a[0])  # Output: H

```
>⚠️ Important : Index starts from 0

# 📌 2. Looping Through a String
👉 You can loop through each character using a for loop

```python

for x in "Stars":
    print(x)

👉 Output:
S
t
a
r
s

```

# 📌 3. String Length (len)
👉 To find length of a string

```python

a = "Happy Birthday"

print(len(a))  # Output: 14

```
>⚠️ Important: Space are also counted.


# 📌 4. Check Value in String (in)
👉 Used to check if a word/character exists

```python

x = "The best things in life are free"

print("free" in x)  # Output: True

```

# 📌 Using with if statement

```python

y = "Nothing is hard and nothing is for free"

if "free" in y:
    print("Yes, 'free' is present")

```


# 📌 5. Check Value NOT in String (not in)
👉 Used to check if something is NOT present

```python

z = "Yes bro you can do it"

print("free" not in z)  # Output: True

```

# 📌 Using with if statement

```python

z = "Yes bro you can do it"

if "She/He" not in z:
    print("No 'She/He' is not present in this string")

```