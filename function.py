# functions in python

def greet(name):
   print("Hello," + name + "!")

   greet("Alice")
   greet("Bob")

   #declare seperate functions for add , sub, mul, div, input num1 and num2 return operations

print("enter two numbers for arithmetic operations")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
   

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b



print("Addition:", add(num1, num2))
print("Subtraction:", sub(num1, num2))
print("Multiplication:", mul(num1, num2))
print("Division:", div(num1, num2))