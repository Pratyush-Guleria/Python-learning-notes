# 📄 Multi-line Strings in Python

## 🧠 What are Multi-line Strings?
Multi-line strings allow you to store **text that spans multiple lines** in a single variable.

👉 Useful when:
- Writing paragraphs  
- Storing large text  
- Formatting output  

---

## 🎯 Why are they important?
- Improve readability  
- Avoid using `\n` again and again  
- Useful in real-world text handling  

---

# 📌 How to Create Multi-line Strings

👉 You can use:
- Triple double quotes `""" """`  
- Triple single quotes `''' '''`  

---

## 📌 Example 1

```python

a = """Hello my name is Pratyush Guleria  
I am 17 years old  
I am a student"""

print(a)

```


## 📌 Example 2 (Using single quotes)

```python

text = '''This is a multi-line string
You can write multiple lines
Without using \n'''

print(text)

```


## ⚡ Important Behavior
👉 Line breaks are automatically preserved

```python

print("""Hello     
World""")                     

```


## 📌 Multi-line String as Comments (Docstrings)
👉 Used to describe functions (very important in real projects)

```python

def greet():
    """This function prints a greeting message"""
    print("Hello!")

```