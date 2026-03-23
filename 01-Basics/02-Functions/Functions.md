## Functions 
What are functions ?
Functions are reusable blocks of code that perform a specific task. They can take input (parameters) and return output.


## What problem does it solves 
    • Easier debugging and Testing
    • Code repetition
    • Maintainability 
    
## Example :-

```python
def abc():
    print("Hello Bro")
abc()
```


> ⚠️ Imporatant : A function must be called to execute. Defining a function alone does not run it.

## Example :-

```python
def Entry(age):    
        if age <= 0:
        return "Invalid age"

    elif age < 18:
        return "You are not an adult, You can't enter"

    elif age >= 50:
        return "You are too old, You can't enter"

    else:
        return "You can enter"
user_age = int(input("Enter your age :"))
message = Entry(user_age)
print(message)
``` 
