# Purpose: Generate a multiplication table up to a user-specified number.
# Concepts: For loops, range(), variables, input, integers, arithmetic.

x = int(input("Number: "))
y = int(input("How many times: "))

for i in range(1, y+1):
    print(f"{x} x {i} = {x * i}")