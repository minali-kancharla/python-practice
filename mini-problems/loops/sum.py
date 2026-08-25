numbers = []

while True:
    value = input("Enter a number (or 'done' to finish): ")

    if value == "done":
        break
    
    numbers.append(int(value))
    
print(f"Sum: {sum(numbers)}")