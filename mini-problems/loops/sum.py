# Purpose: Collect numbers from the user and calculate their total.
# Concepts: Lists, while loops, break, sentinel values, input/type conversion, .append(), sum(), and f-strings.

numbers = []

while True:
    value = input("Enter a number (or 'done' to finish): ")

    if value == "done":
        break
    
    numbers.append(int(value))
    
print(f"Sum: {sum(numbers)}")