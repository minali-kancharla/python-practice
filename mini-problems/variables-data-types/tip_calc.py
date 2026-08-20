# Purpose: Calculate the tip, total bill, and cost per person.
# Concepts: Variables, floats, arithmetic, input, type conversion, f-strings.

bill = float(input("Bill: "))
tip = float(input("Tip (%): "))
people = int(input("Number of people: "))

tip_amount = bill * (tip*0.01)
total_bill = bill + tip_amount
each_person = total_bill/people

print(f"Tip: ${tip_amount:.2f}")
print(f"Total: ${total_bill:.2f}")
print(f"Each person: ${each_person:.2f}")