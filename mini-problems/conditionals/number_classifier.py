# Purpose: Determine whether a number is positive, negative, or zero and whether it is even or odd.
# Concepts: Conditionals, comparison operators, modulo, input, integers.

x = int(input("Enter number: "))

if x > 0:
    print("Positive")
elif x<0:
    print("Negative")
else: 
    print("Zero")

if x%2 == 0:
    print("Even")
else:
    print("Odd")