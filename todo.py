class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔️" if self.completed else "❌"
        return f"{status} {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_completed()
            print(f"Task {task_number} marked as completed!")
        else:
            print("Invalid task number.")


def main():
    todo = ToDoList()
    
    while True:
        print("\nTo-Do List Options:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            desc = input("Enter task description: ")
            todo.add_task(desc)
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            todo.view_tasks()
            task_num = int(input("Enter task number to complete: "))
            todo.complete_task(task_num)
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
