# Purpose: Convert a numerical grade into a letter grade and pass/fail result.
# Concepts: Conditionals, comparison operators, input, integers.

grade = int(input("Grade (0-100): "))

if 90 <= grade <= 100:
    print("Grade: A")
    print("Pass")
elif grade >= 80:
    print("Grade: B")
    print("Pass")
elif grade >= 70:
    print("Grade: C")
    print("Pass")
elif grade >= 60:
    print("Grade: D")
    print("Pass")
elif grade >= 0:
    print("Grade: F")
    print("Fail")
else:
    print("Not possible!")