# Purpose: Generate a pyramid pattern of # symbols based on the user's chosen height.
# Concepts: for loops, range(), string multiplication, arithmetic, input/type conversion, and print formatting.

height = int(input("Height: "))

for i in range(height):
    print(" " * (height - i - 1) , "#" * (i + 1), "#" * (i + 1))
