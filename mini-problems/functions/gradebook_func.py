import statistics

students = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 97,
    "David": 88
}

def calculate_average(students):
    return statistics.mean(students.values())

def find_highest(students):
    return max(students.values())

def find_lowest(students):
    return min(students.values())

average = calculate_average(students)
highest = find_highest(students)
lowest = find_lowest(students)
for student, grade in students.items():
    print(f"{student} -- {grade}")

print(f"{average}\n {highest}\n {lowest}")