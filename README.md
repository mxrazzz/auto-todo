# auto-todo

A simple command-line to-do list application written in Python.

![Coverage](coverage.svg)

## Features

- Add tasks
- View tasks
- Remove tasks

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/auto-todo.git
   ```
2. Navigate to the project directory:
   ```sh
   cd auto-todo
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

### Usage

Run the application:

```sh
python main.py
```

### Running Tests

To run the tests, use pytest:

```sh
pytest
```

To run the tests with coverage, use pytest-cov:

```sh
pytest --cov=main
```

### Code Quality

This project uses `flake8` for linting and `black` for formatting.

**Check code quality (linting):**

```sh
flake8 .
```

**Check code formatting:**

```sh
black --check .
```

**Auto-format your code:**

```sh
black .
```

**Run all checks before committing:**

```sh
# Format code
black .
# Check linting
flake8 .
# Run tests with coverage
pytest --cov=main
```

## Deployment

This project uses automated deployment via GitHub Actions.

### Creating a Release

1. **Create a tag:**

   ```sh
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

2. **Or create a release on GitHub:**

   - Go to your repository on GitHub
   - Click "Releases" → "Create a new release"
   - Choose a tag version (e.g., `v1.0.0`)
   - Click "Publish release"

3. **What happens automatically:**
   - GitHub Actions runs all tests
   - If tests pass, it creates a `.zip` file of your app
   - The `.zip` is automatically attached to your release
   - Anyone can download the packaged app from the Releases page!
