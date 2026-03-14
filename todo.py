def display_menu():
    print("\n===== TO DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Exit")


def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for i, t in enumerate(tasks):
        status = "✓" if t["done"] else "✗"
        print(f"{i+1}. {t['task']} [{status}]")


def mark_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("Enter task number to mark completed: "))
        tasks[num-1]["done"] = True
        print("Task marked as completed.")
    except:
        print("Invalid input.")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        print("Task deleted.")
    except:
        print("Invalid input.")


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task(tasks)

        elif choice == '2':
            view_tasks(tasks)

        elif choice == '3':
            mark_completed(tasks)

        elif choice == '4':
            delete_task(tasks)

        elif choice == '5':
            print("Exiting application...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()