def main():
    """
    A simple command-line To-Do List application.
    """

    tasks = []

    def add_task():
        """Adds a new task to the to-do list."""
        task = input("Enter the task to add: ")
        tasks.append(task)
        print(f"Task '{task}' added successfully!")

    def view_tasks():
        """Displays the current tasks in the to-do list."""
        if not tasks:
            print("No tasks in the to-do list.")
            return

        print("\n--- To-Do List ---")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")
        print("------------------\n")

    def delete_task():
        """Deletes a task from the to-do list based on its index."""
        if not tasks:
            print("No tasks to delete.")
            return

        view_tasks()  # Show tasks with indices for easy selection

        try:
            task_index = int(input("Enter the number of the task to delete: "))
            if 1 <= task_index <= len(tasks):
                deleted_task = tasks.pop(task_index - 1)
                print(f"Task '{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        print("\n--- Menu ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                add_task()
            elif choice == '2':
                view_tasks()
            elif choice == '3':
                delete_task()
            elif choice == '4':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Useful for cleanup operations (not needed in this simple example).
            pass

if __name__ == "__main__":
    main()