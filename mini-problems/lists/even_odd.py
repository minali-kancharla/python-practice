# Purpose: Separate numbers into even and odd lists and calculate their averages.
# Concepts: Lists, for loops, conditionals, modulo (%), .append(), sum(), len(), and f-strings.

numbers = [12, 7, 18, 25, 30, 41, 52, 63]

even_numbers = []
odd_numbers = []

for num in numbers:
    if num%2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
    
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
print(f"Average of evens: {sum(even_numbers)/len(even_numbers)}")
print(f"Average of odds: {sum(odd_numbers)/len(odd_numbers)}")