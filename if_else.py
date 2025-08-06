# check even or odd number

def even_odd(a):
    if a %2 == 0:
        return "even"
    else:
        return "odd"
    
print("Enter a number to check if it's even or odd:")
num = int(input("Number: "))
print(f"The number {num} is {even_odd(num)}.")


#check greater or smaller number
def greater_smaller(a, b):
    if a > b:
        return f"{a} is greater than {b}."
    elif a < b:
        return f"{a} is smaller than {b}."
    else:
        return f"{a} is equal to {b}."
print("Enter two numbers to compare:")
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
print(greater_smaller(num1, num2))

# function to return square of a number
def square(a):
    return a * a

print("Enter a number to find its square:")
num = float(input("Number: "))
print("the square of", num, "is", square(num))