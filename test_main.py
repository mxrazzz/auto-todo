# Welcome to your test file, now using pytest!
# Pytest is a very popular testing library that makes writing tests simpler.
# One of the best features of pytest is that it requires less "boilerplate" code.

# We still need to import a few things.
import io
import sys
from unittest.mock import patch

# We import the 'main' function from your application.
from main import main

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
    from main import tasks
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
