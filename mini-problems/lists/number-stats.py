numbers = []
count = int(input("How many numbers? "))
for i in range(count):
    value = int(input("Enter a number: "))
    numbers.append(value)

total = 0
smallest = numbers[0]
largest = numbers[0]
even = 0
odd = 0

for num in numbers:
    total = total + num

    if num < smallest:
        smallest = num

    if num > largest:
        largest = num
    
    if num%2 == 0:
        even = even + 1
    
    if num%2 != 0:
        odd = odd + 1

average = total / len(numbers)

print(f"Total: {total}")
print(f"Average: {average}")
print(f"Minimum: {smallest}")
print(f"Maximum: {largest}")
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")