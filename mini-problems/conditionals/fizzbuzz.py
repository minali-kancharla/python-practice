# Purpose: Print Fizz, Buzz, or FizzBuzz based on divisibility.
# Concepts: Conditionals, modulo, comparison operators, input.

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
  print("FizzBuzz")
elif number % 5 == 0:
  print("Buzz")
elif number % 3 ==0:
  print("Fizz")
else:
  print(number)
  
