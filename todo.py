tasks = []

def show_menu():
    print("\n📋 To-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        if not tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "✅" if task['done'] else "❌"
                print(f"{i}. {task['task']} - {status}")

    elif choice == '2':
        new_task = input("Enter task name: ")
        tasks.append({"task": new_task, "done": False})
        print(f"✅ Task '{new_task}' added!")

    elif choice == '3':
        task_no = int(input("Enter task number to mark as done: "))
        if 0 < task_no <= len(tasks):
            tasks[task_no - 1]['done'] = True
            print(f"✅ Task {task_no} marked as done!")
        else:
            print("⚠️ Invalid task number.")

    elif choice == '4':
        task_no = int(input("Enter task number to delete: "))
        if 0 < task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"🗑️ Task '{removed['task']}' deleted.")
        else:
            print("⚠️ Invalid task number.")

    elif choice == '5':
        print("👋 Exiting To-Do App. Bye!")
        break

    else:
        print("❌ Invalid choice. Please enter 1–5.")
