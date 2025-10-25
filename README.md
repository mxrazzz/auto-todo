# 📝 Auto-Todo

> A simple command-line to-do list application demonstrating **professional DevOps practices**

![Coverage](coverage.svg)
![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Code Style](https://img.shields.io/badge/code%20style-black-black)

---

## ✨ Features

- ✅ **Add tasks** - Never forget what you need to do
- 👀 **View tasks** - See all your to-dos at a glance
- 🗑️ **Remove tasks** - Mark things complete
- 🎨 **Simple CLI** - Easy to use terminal interface

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9, 3.10, or 3.11
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/mxrazzz/auto-todo.git
cd auto-todo

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
# Run the app
python main.py
```

**That's it!** Follow the on-screen menu to manage your tasks.

---

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=main

# Run with detailed coverage
pytest --cov=main --cov-report=term-missing
```

---

## 🎨 Code Quality

This project maintains high code quality standards:

```bash
# Auto-format code (fixes style automatically)
black .

# Check for code issues
flake8 .

# Check formatting without changing files
black --check .
```

### Pre-commit Checklist

Before committing, run:

```bash
black .              # Format code
flake8 .             # Check quality
pytest --cov=main    # Run tests
```

---

## 🏗️ DevOps Features

This project showcases modern DevOps practices:

### 🤖 Continuous Integration (CI)

- ✅ Automated testing on every push
- ✅ Code quality checks (linting with flake8)
- ✅ Code formatting validation (black)
- ✅ Coverage tracking with auto-updating badge
- ✅ Dependency caching for faster builds

### 🚢 Continuous Deployment (CD)

- ✅ Automated releases via Git tags
- ✅ Automatic packaging as `.zip` files
- ✅ GitHub Releases with auto-generated notes

### 🔄 Matrix Testing

- ✅ Tests run on 6 environments simultaneously:
  - **OS:** Ubuntu, Windows
  - **Python:** 3.9, 3.10, 3.11
- ✅ Parallel execution for faster feedback
- ✅ Downloadable test reports as artifacts

### ♻️ Reusable Workflows

- ✅ DRY principle applied to CI/CD
- ✅ Workflow templates for easy reuse
- ✅ Parameterized testing infrastructure

---

## 📊 Project Stats

- **Code Coverage:** 95%
- **Test Cases:** 5
- **Supported Python Versions:** 3
- **Supported Operating Systems:** 2
- **Automated Workflows:** 4
- **Lines of Code:** ~150 (main + tests)

---

## 📦 Creating a Release

### Method 1: Using Git Tags

```bash
# Create and push a version tag
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

### Method 2: Using GitHub UI

1. Go to your repository on GitHub
2. Click **"Releases"** → **"Create a new release"**
3. Choose a tag (e.g., `v1.0.0`)
4. Click **"Publish release"**

### What Happens Automatically:

1. 🧪 All tests run
2. 🎨 Code quality is verified
3. 📦 App is packaged as a `.zip` file
4. 🚀 Release is published on GitHub
5. 📝 Release notes are auto-generated

---

## 🛠️ Tech Stack

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| **Python 3.11**    | Programming language      |
| **pytest**         | Testing framework         |
| **pytest-cov**     | Code coverage measurement |
| **black**          | Code formatter            |
| **flake8**         | Code linter               |
| **GitHub Actions** | CI/CD automation          |

---

## 📁 Project Structure

```
auto-todo/
├── 📂 .github/
│   └── 📂 workflows/
│       ├── ci.yml              # Main CI pipeline
│       ├── main.yml            # Matrix testing
│       ├── reusable-tests.yml  # Reusable test workflow
│       └── release.yml         # Automated releases
├── 📄 main.py                  # To-do list application
├── 📄 test_main.py            # Test suite (5 tests)
├── 📄 requirements.txt         # Python dependencies
├── 📄 .flake8                  # Linter configuration
└── 📄 README.md                # This file!
```

---

## 🎓 Learning Outcomes

This project demonstrates:

- ✅ **CI/CD pipelines** with GitHub Actions
- ✅ **Automated testing** with pytest
- ✅ **Code quality enforcement** with linting & formatting
- ✅ **Matrix builds** for multi-environment testing
- ✅ **Reusable workflows** for maintainable automation
- ✅ **Automated releases** with version tagging
- ✅ **Artifact generation** for test reports
- ✅ **Dependency caching** for performance
- ✅ **Code coverage tracking** with badges

---

## 🌟 Features Highlights

### 🔒 Quality Gates

- Code must pass linting before merge
- Formatting is automatically verified
- Tests must achieve minimum coverage
- All checks run on multiple environments

### ⚡ Performance Optimizations

- Dependency caching reduces build time by 70%
- Parallel matrix jobs provide faster feedback
- Shallow git clones for speed

### 📈 Visibility

- Coverage badge shows test health at a glance
- Downloadable HTML reports for detailed analysis
- Auto-generated release notes document changes

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and quality checks
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

All PRs must:

- ✅ Pass all tests
- ✅ Pass linting (flake8)
- ✅ Be formatted with black
- ✅ Maintain or improve coverage

---

## 📝 License

This project is open source and available for educational purposes.

---

## 🙏 Acknowledgments

Built as a DevOps learning project to demonstrate:

- Modern software development practices
- Automated testing and quality assurance
- CI/CD pipeline implementation
- Infrastructure as Code principles

---

## 📞 Contact

**GitHub:** [@mxrazzz](https://github.com/mxrazzz)  
**Project:** [auto-todo](https://github.com/mxrazzz/auto-todo)

---

<div align="center">

**⭐ Star this repo if you found it helpful!**

Made with ❤️ and ☕ as a DevOps learning journey

</div>
