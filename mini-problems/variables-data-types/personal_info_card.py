# Purpose: Collect and display basic personal information.
# Concepts: Variables, strings, integers, input, type conversion, f-strings.

first = input("First Name: ")
last = input("Last Name: ")
age = int(input("Age: "))
height = int(input("Height (in): "))
color = input("Favorite color: ")

print(f"Name: {first} {last}")
print(f"Age: {age}")
print(f"Height: {height} inches")
print(f"Favorite color: {color}")
print(f"Age in five years: {age+5}")