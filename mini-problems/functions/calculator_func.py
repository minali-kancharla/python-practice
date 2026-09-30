a = int(input("Enter number #1: "))
b = int(input("Enter number #2: "))

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

function = input("operation: ")

if function == "add":
    result = add(a, b)
elif function == "subtract":
    result = subtract(a, b)
elif function == "multiply":
    result = multiply(a, b)
elif function == "divide":
    result = divide(a, b)

print(result)
