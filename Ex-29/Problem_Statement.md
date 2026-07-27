# Experiment 29 – Create a Feature Branch, Implement a Login Function, and Merge Using a Pull Request

## Aim

To understand Git branching and collaboration by creating a feature branch, implementing a login function, committing changes, pushing them to GitHub, and merging the feature into the main branch using a Pull Request.

---

## Problem Statement

Branching is an important feature of Git that enables developers to work on new features independently without affecting the main codebase. Once the feature is completed, the changes are reviewed through a Pull Request before being merged into the main branch. This workflow promotes collaboration, code quality, and efficient version control.

In this experiment, create a new branch named **feature-login**, implement a simple login function in a Python file, commit and push the changes to GitHub, create a Pull Request, and merge the feature branch into the main branch.

---

## Objectives

- Understand Git branching concepts.
- Create and switch to a new Git branch.
- Implement a simple Python login function.
- Commit and push changes to GitHub.
- Create and merge a Pull Request.
- Learn collaborative development using GitHub.

---

## Requirements

Perform the following tasks:

1. Create a new branch named **feature-login**.
2. Create a file named **login.py**.
3. Implement a simple login function in the file.
4. Stage the changes using Git.
5. Commit the changes with an appropriate commit message.
6. Push the **feature-login** branch to GitHub.
7. Create a Pull Request from **feature-login** to **main**.
8. Review and merge the Pull Request.
9. Verify that the changes are available in the **main** branch.

---

## Tools Required

- Git
- GitHub
- Python 3.x
- Visual Studio Code (or any text editor)
- Git Bash / Terminal

---

## Files Required

- login.py
- README.md (Optional)

---

## Sample Git Commands

### Create a New Branch

```bash
git checkout -b feature-login
```

### Stage Changes

```bash
git add login.py
```

### Commit Changes

```bash
git commit -m "Added login functionality"
```

### Push Feature Branch

```bash
git push origin feature-login
```

### Create Pull Request

Create a Pull Request on GitHub from **feature-login** to **main**, review the changes, and merge the Pull Request.

---

## Deliverables

- Feature Branch (**feature-login**)
- login.py File
- Git Commit History
- Pull Request
- Merged Branch
- Screenshots of:
  - Branch creation
  - Commit history
  - Pull Request
  - Successful merge into the main branch

---

## Expected Outcome

A new feature branch named **feature-login** is successfully created, a login function is implemented in **login.py**, and the changes are committed, pushed, reviewed through a Pull Request, and merged into the **main** branch. This demonstrates the standard GitHub feature branch workflow used in collaborative software development.
