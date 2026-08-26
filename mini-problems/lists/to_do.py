# Purpose: Create a to-do list where users can add, remove, view, clear, and complete tasks.
# Concepts: Lists, .append(), .pop(), .clear(), indexing, len(), range(), for/while loops,
# break, conditionals, input/type conversion, and f-strings.

tasks = []
print('''
1. Add task
2. Remove task
3. View tasks
4. Quit
5. Clear all tasks
6. Mark task as complete
    ''')
while True:
    choice = int(input("Choose an option: "))
    if choice == 1: 
        task = input("Add task: ")
        tasks.append(task)
    elif choice == 2:
        task_number = int(input("Remove task #: "))
        tasks.pop(task_number - 1)
    elif choice == 3:
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
    elif choice == 4:
        break
    elif choice == 5:
        tasks.clear()
    elif choice == 6:
        for i in range(len(tasks)):
            tasks[i] = tasks[i] + " (complete)"
    else:        
        print("Invalid choice.")
