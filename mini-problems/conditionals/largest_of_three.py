# Purpose: Find the largest of three numbers, including ties.
# Concepts: Conditionals, comparison operators, equality, input, integers.

x = int(input("First number (x): "))
y = int(input("Second number (y): "))
z = int(input("Third number (z): "))

if x == y == z:
    print("All three numbers are equal")
elif x == y and x > z:
    print("x and y are equal and are the largest numbers")
elif x == z and x > y:
    print("x and z are equal and are the largest numbers")
elif y == z and y > x:
    print("y and z are equal and are the largest numbers")
elif x > y and x > z:
    print("x is the largest number")
elif y > x and y > z:
    print("y is the largest number")
else:
    print("z is the largest number")