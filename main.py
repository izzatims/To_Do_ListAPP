FILE_NAME = "tasks.txt"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError: # to avoid system crash
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(tasks):
    task = input("Enter your task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully")


def view_task(tasks):
    if not tasks:
        print("No task available")
        return

    print("\n ........ Your Tasks ........")

    for i, task in enumerate(tasks, start=1):
        status = "/" if task.startswith("/") else " "        
        clean_task = task.replace("/", "").strip()
        print(f"{i}. [{status}] {clean_task}")


def delete_task(tasks):
    if not tasks:
        print("No task exist")
        return

    view_task(tasks)

    try:
        num = int(input("Enter task number to delete: "))

        if num < 1 or num > len(tasks):
            print("Invalid task number")
            return

        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted {removed}")

    except ValueError:
        print("Please enter a number")
        
        
def complete_task(tasks):
    view_task(tasks)

    try:
        num = int(input("Enter task number to mark as done: "))

        if num < 1 or num > len(tasks):
            print("Invalid task number")
            return

        if tasks[num - 1].startswith("/"):
            print("Task already completed")
        else:
            tasks[num - 1] = "/ " + tasks[num - 1]
            save_tasks(tasks)
            print("Task marked as done!")

    except ValueError:
        print("Please enter a number")    


# MAIN
tasks = load_tasks()

while True:
    print("\n........ TO DO LIST ........")
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")    
    
    choice = input("Choose action: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_task(tasks)
    elif choice == "3":
        complete_task(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        print("See you again!")
        break