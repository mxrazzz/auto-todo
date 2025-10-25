# This is an empty list that will store our to-do items (tasks).
tasks = []

# This function will print the menu of options for the user.
def show_menu():
    # Prints the title of the menu.
    print("\n--- To-Do List Menu ---")
    # Prints the option for adding a task.
    print("1. Add a task")
    # Prints the option for viewing all tasks.
    print("2. View tasks")
    # Prints the option for removing a task.
    print("3. Remove a task")
    # Prints the option for exiting the program.
    print("4. Exit")

# This function handles adding a new task to the list.
def add_task():
    # Prompts the user to type in a task and waits for their input.
    task = input("Enter the task: ")
    # Adds the user's input (the task) to the end of the 'tasks' list.
    tasks.append(task)
    # Prints a confirmation message to show the task was added successfully.
    print(f"Task '{task}' added.")

# This function displays all the tasks currently in the list.
def view_tasks():
    # Prints a header for the task list.
    print("\n--- Your Tasks ---")
    # Checks if the 'tasks' list is empty.
    if not tasks:
        # If there are no tasks, it prints a message saying so.
        print("You have no tasks.")
    # If the list is not empty, the code inside 'else' will run.
    else:
        # This loop goes through each task in the 'tasks' list.
        # 'enumerate' gets both the index (i) and the item (task). We start counting from 1.
        for i, task in enumerate(tasks, start=1):
            # Prints the task number and the task itself.
            print(f"{i}. {task}")

# This function handles removing a task from the list.
def remove_task():
    # Calls the 'view_tasks' function to show the user the current tasks first.
    view_tasks()
    # Checks if there are any tasks in the list to remove.
    if tasks:
        # This 'try' block lets us handle potential errors, like if the user doesn't enter a number.
        try:
            # Prompts the user to enter the number of the task they want to remove.
            task_num_to_remove = int(input("Enter the number of the task to remove: "))
            # Checks if the number entered by the user is a valid task number.
            if 1 <= task_num_to_remove <= len(tasks):
                # Removes the task from the list. We subtract 1 because list indices start at 0.
                # The 'pop' method removes the item and also returns it, so we can use it in the message.
                removed_task = tasks.pop(task_num_to_remove - 1)
                # Prints a confirmation message showing which task was removed.
                print(f"Task '{removed_task}' removed.")
            # If the number is not valid (e.g., too high or too low).
            else:
                # Prints an error message.
                print("Invalid task number.")
        # This 'except' block catches the error if the user enters something that's not a whole number.
        except ValueError:
            # Prints an error message asking for a valid number.
            print("Invalid input. Please enter a number.")

# This is the main part of the program that runs in a loop.
def main():
    # This 'while True' creates an infinite loop, so the program keeps running until we explicitly exit.
    while True:
        # Calls the function to show the menu options.
        show_menu()
        # Asks the user to choose an option from the menu.
        choice = input("Enter your choice (1-4): ")

        # Checks if the user's choice is '1'.
        if choice == '1':
            # If it is, it calls the function to add a task.
            add_task()
        # Checks if the user's choice is '2'.
        elif choice == '2':
            # If it is, it calls the function to view the tasks.
            view_tasks()
        # Checks if the user's choice is '3'.
        elif choice == '3':
            # If it is, it calls the function to remove a task.
            remove_task()
        # Checks if the user's choice is '4'.
        elif choice == '4':
            # Prints a goodbye message.
            print("Exiting the To-Do List. Goodbye!")
            # 'break' stops the 'while' loop and ends the program.
            break
        # If the user enters anything other than 1, 2, 3, or 4.
        else:
            # Prints an error message asking for a valid choice.
            print("Invalid choice. Please enter a number between 1 and 4.")

# This standard Python construct checks if the script is being run directly.
# If it is, it calls the 'main' function to start the program.
if __name__ == "__main__":
    # Calls the main function to run the application.
    main()