# 🔁 While Loop in Python

## What is a While Loop?
A while loop executes a block of code repeatedly **as long as the condition is True**.

---

## What problem does it solve?
A while loop is used when:
- You don’t know how many times the loop should run.
- You want to repeat code until a condition becomes False.

---

## Example 1: Input Validation

```python

name = input("Enter your name: ").strip().title()

while name == "":
    print("You didn't enter your name")
    name = input("Enter your name: ").strip().title()

print(f"Your name is {name}")

```

## Example 2: Infinite Loop + break

```python

while True:
    name = input("Enter your name: ")
    if name != "":
        break

```
> ⚠️ Important :- break exits the loop completely.

## Example 3: continue 

```python

number = 1

while number < 10:
    number += 1
    if number == 3:
        continue
    print(number)

```
> ⚠️ Important :- continue skips the current iteration.

## Example 4: pass

```python 

n = 1

while n <= 5:
    if n == 2:
        pass
    else:
        print(n)
    n += 1

```
> ⚠️ Important :- pass does nothing (placeholder).

---

## 📁 `for_loop.md`

```markdown
# 🔁 For Loop in Python

## What is a For Loop?
A for loop is used to execute a block of code **a fixed number of times**.

You can iterate over:
- range()
- lists
- strings
- other sequences

---

## What problem does it solve?
It helps when:
- You know how many times to run the loop.
- You want to iterate over a collection (list, string, etc.).

---

## Syntax

```python

for variable in range(start, stop, step):
    print(variable)

```

## Example 1 : Using range()

```python

for i in range(2, 22, 2):
    print(i)

```

## Example 2: Loop through list

```python

names = ["Rahul", "Amit", "Ankit"]

for name in names:
    print(name)

```

## Example 3: Loop through string

```python

word = "Hello"

for letter in word:
    print(letter)

```

## Example 4: Real-world example

```python

prices = [100, 500, 1000]

for p in prices:
    print(f"Discounted price: {p - 50}")
    
```
