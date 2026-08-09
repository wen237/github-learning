# GitHub Learning

This repository is used to practice Git and GitHub workflows.

## Goals

- Learn basic Git commands
- Connect VS Code with GitHub
- Practice commits, pushes, and pulls

## Progress

### Day 1

- Created the repository
- Added `README.md`
- Added `hello.py`
- Learned `git init`, `git add`, `git commit`, and `git push`

### Day 2

- Learned how to use `git diff`
- Understood the staging area
- Added a `goodbye()` function
- Practiced writing meaningful commit messages

### Day 3

- Transform into project management
- Split the project into `main.py` and `greeting.py`
- Added `.gitignore`
- Learned why `__pycache__` and `.pyc` files should not be committed

### Day 4

- Git stores project history instead of simply saving files.
- `git restore` restores changes from Git history.
- `git rm` removes a file from both the working directory and the staging area.
- Understanding the working directory, staging area, and commit history is essential.

### Day 5

- `git show` is for viewing what a particular commit did.
- Git preserves the story of a project. Reading commit history is just as important as creating commits.

### Day 6

- `git switch` is amazing!
- Every commit is a complete snapshot of the project, allowing Git to restore the entire repository to any point in its history.

### Day 7

- Learned the concept of Git branches
- Created the first feature branch
- Developed and committed a feature without modifying `main`
- Practiced switching between `main` and a feature branch
- Pushed a feature branch to GitHub

### Day 8

- Created the first Pull Request on GitHub
- Reviewed changes before merging
- Merged a feature branch into `main`
- Synchronized the remote changes with the local repository
- Deleted the completed feature branch

## Key Takeaways

### Git

- Git is not just a backup tool—it records the evolution of a project through meaningful commits.
- A good commit records one meaningful change with a clear message, making project history easy to understand.
- Organizing code into modules and using `.gitignore` keeps a Python project clean, maintainable, and focused on source code rather than generated files.
- Git manages changes across the working directory, staging area, and commit history, so understanding where a file exists is just as important as knowing which command to use.
- A Git branch provides an independent line of development by pointing to its own commit history, allowing new features to evolve without changing the stable `main` branch.
- A Pull Request provides a structured process for reviewing and integrating changes from a feature branch into the main development line.

### Python

- Use modules to organize reusable code.
- Ignore `__pycache__` and `.pyc` files with `.gitignore`.
