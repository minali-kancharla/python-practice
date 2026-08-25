students = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 97,
    "David": 88
}

print(students)

highest = 0

for student, grade in students.items():
    if grade > highest:
        highest = grade
        highest_student = student
print(f"Highest grade: {highest_student} - {highest}")

average = sum(students.values()) / len(students)
print(f"Class average: {average}")

ask_search = input("Students search? (y/n): ")

if ask_search == "y":

    search = input("Enter student name: ")

    if search in students:
        print(f"{search} - {students[search]}")

    else:
        print("Student does not exist.")

while True: 
    add_student = input("Enter student (y/n): ")
    if add_student == "y":
        new_student = input("New student: ")
        newstu_grade = int(input("New student grade: "))
        students[new_student] = newstu_grade
    else:
        break