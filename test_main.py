# Welcome to your test file, now using pytest!
# Pytest is a very popular testing library that makes writing tests simpler.
# One of the best features of pytest is that it requires less "boilerplate" code.

# We still need to import a few things.
import io
import sys
from unittest.mock import patch

# We import the 'main' function from your application.
from main import main, tasks

# --- What is 'monkeypatch'? ---
# 'monkeypatch' is a special tool provided by pytest. It's similar to unittest.mock.patch.
# It allows us to temporarily change the behavior of functions, which is perfect for simulating user input.

# --- What is 'capsys'? ---
# 'capsys' is another pytest tool. It stands for "capture system output".
# It automatically collects anything your program prints to the screen, so we can check it.

def test_full_application_flow_with_pytest(monkeypatch, capsys):
    """
    This single test simulates a full user session using pytest's tools.
    1. Add two tasks.
    2. View the list to see them.
    3. Remove one task.
    4. View the list again to confirm removal.
    5. Exit.
    """
    # --- Step 1: Simulate User Input with monkeypatch ---
    # We need to provide a sequence of inputs for our "robot user".
    # We'll create a list of the inputs in the order they should be "typed".
    user_inputs = [
        '1', 'Buy groceries',  # Add "Buy groceries"
        '1', 'Walk the dog',   # Add "Walk the dog"
        '2',                   # View tasks
        '3', '1',              # Remove the first task
        '2',                   # View tasks again
        '4'                    # Exit
    ]
    # The 'iter' function turns our list into an iterator, so 'input()' gets the next item each time.
    input_iterator = iter(user_inputs)
    # Here, we tell monkeypatch: "Whenever 'builtins.input' is called, use our iterator to provide the value."
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # --- Step 2: Run the main application ---
    # We need to make sure the task list is empty before we start.
    tasks.clear()
    # Now, we run your 'main()' function. Monkeypatch will handle all the 'input()' calls.
    main()

    # --- Step 3: Get the captured output from capsys ---
    # Pytest's 'capsys' has been silently capturing all the 'print()' statements.
    # 'capsys.readouterr()' gives us everything that was printed.
    captured = capsys.readouterr()
    output = captured.out

    # --- Step 4: Check if everything happened as expected ---
    # Just like before, we use 'assert' to check if the output contains the text we expect.
    # If any of these 'assert' statements fail, pytest will report an error.

    # Check for the "add task" messages.
    assert "Task 'Buy groceries' added." in output
    assert "Task 'Walk the dog' added." in output

    # Check that the tasks were displayed correctly the first time.
    assert "1. Buy groceries" in output
    assert "2. Walk the dog" in output

    # Check for the "remove task" message.
    assert "Task 'Buy groceries' removed." in output

    # Check the final state of the task list.
    # We find the last time "--- Your Tasks ---" was printed to isolate the final list view.
    last_task_view = output[output.rfind("--- Your Tasks ---"):]
    assert "1. Walk the dog" in last_task_view
    assert "Buy groceries" not in last_task_view  # Make sure the removed task is gone.

    # Check for the exit message.
    assert "Exiting the To-Do List. Goodbye!" in output

# --- A NEW UNIT TEST ---
# This test focuses on only ONE function: add_task.
def test_add_task_unit(monkeypatch):
    """
    This is a UNIT TEST. It checks only the add_task function in isolation.
    """
    # Step 1: Set up the test conditions.
    # We need to make sure the tasks list is empty before we start.
    tasks.clear()
    
    # Step 2: Simulate the user typing "Learn Pytest".
    # We use monkeypatch to tell the program that the next time 'input()' is called,
    # it should return "Learn Pytest".
    monkeypatch.setattr('builtins.input', lambda _: "Learn Pytest")
    
    # Step 3: Call the function we are testing.
    # We are NOT running the whole 'main()' application, just the single 'add_task' function.
    # To do this, we need to import it first.
    from main import add_task
    add_task()
    
    # Step 4: Check the result.
    # We assert two things to be sure it worked:
    # 1. The tasks list should now contain exactly one item.
    # 2. The first item in the list should be the string "Learn Pytest".
    assert len(tasks) == 1
    assert tasks[0] == "Learn Pytest"

# --- ANOTHER NEW UNIT TEST ---
# This test focuses on the view_tasks function when there are no tasks.
def test_view_tasks_empty(capsys):
    """
    Test the view_tasks function when the tasks list is empty.
    """
    # Step 1: Clear the tasks list to ensure it's empty.
    tasks.clear()

    # Step 2: Call the view_tasks function.
    from main import view_tasks
    view_tasks()

    # Step 3: Capture the printed output using capsys.
    captured = capsys.readouterr()
    output = captured.out

    # Step 4: Assert that the correct message is printed.
    assert "You have no tasks." in output

# --- TEST FOR INVALID MENU CHOICE ---
def test_invalid_menu_choice(monkeypatch, capsys):
    """
    Test that the program handles invalid menu choices correctly.
    """
    tasks.clear()
    user_inputs = [
        '5',  # Invalid choice
        '4'   # Exit
    ]
    input_iterator = iter(user_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))
    
    main()
    
    captured = capsys.readouterr()
    output = captured.out
    assert "Invalid choice. Please enter a number between 1 and 4." in output

# --- TEST FOR REMOVING A TASK WITH INVALID INPUT ---
def test_remove_task_invalid_input(monkeypatch, capsys):
    """
    Test that remove_task handles non-numeric input correctly.
    """
    tasks.clear()
    tasks.append("Test Task")
    
    user_inputs = ['abc']  # Invalid input (not a number)
    input_iterator = iter(user_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))
    
    from main import remove_task
    remove_task()
    
    captured = capsys.readouterr()
    output = captured.out
    assert "Invalid input. Please enter a number." in output
