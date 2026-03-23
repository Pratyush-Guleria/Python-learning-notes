# Return Statement

## 1. What does return do?

The `return` keyword sends data from inside a function to the outside world.

It allows us to:
- Store the result
- Reuse the result
- Perform further calculations

---

## 2. Why is return important?

Without return:
- A function only displays output
- We cannot reuse the result

With return:
- We can store the output in a variable
- We can reuse it multiple times
- It is heavily used in real-world projects

---

## 3. Example

def add(a, b):
    return a * a, a + b

x = add(10, 10)
print(x)

We can reuse the returned value:

a = x
print(a)

---

## 4. Print vs Return

### Using Print

def add(a, b):
    print(a + b)

x = add(10, 10)
print(x)

Output:
20
None

Explanation:
- print() only displays data
- It does NOT give usable data back
- So x becomes None

---

### Using Return

def add(a, b):
    return a + b

x = add(10, 10)
print(x)

Output:
20

Here:
- return gives back usable data
- We can store it and reuse it

---

## Important Concept

`print()` → Only shows output  
`return` → Gives data for reuse