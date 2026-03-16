# What is a While loop ?
#While loop executes a block of code repeatedly as long as the condition remains True.


# What problem does while loop solves ?
# While loops is used to execute some code for infinite times untile some condition is true.

# Example : 1

name = input("Enter your name :").strip().title()

while name =="":
        print("You didn't enter your name")
        name = input("Enter your name :").title().strip()
print(f"Your name is {name}")

# Example : 2 (infinite loop)
# break = used to exit the loop entirely

while True:
    name = input("Enter your name :")
    if name !="": 
        break
        
# Example :3 
# continue = skips the next iteration of the loop

number = 1

while number < 10 :
     number +=1
     if number ==3:
          continue 
     print(number)

# Example :4
# pass = does nothing just act as a placeholder 
n = 1
while n <=5:
     if n == 2:
          pass
     else:
          print(n)
     n +=1

# For loop

# What is for loop ?
# for loop is a loop is used to exuted some code for fixed number of times.
# You can interate over a range, string, sequence.

# What problem does it solves?
# It helps to exucute a block of code for fixed number of time. 

# Syntax of for loop :

# for variable_name in range (start,stop,step):
#     print(variable_name)

# Example 1:

for i in range (2,22,2):
     print(i)

# Exmaple 2:

name = ["Rahul", "Amit", "Ankit"]
for i in name:
     print(i)

# Example 3:
letter = "Hello"
for i in letter:
     print(i)

# Example 4:

prices = [100, 500, 1000]

for p in prices:
    print(f"Naya price: {p - 50}")
