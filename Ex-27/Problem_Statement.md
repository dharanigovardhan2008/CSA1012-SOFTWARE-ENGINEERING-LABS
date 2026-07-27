# Experiment 27 – Commit and Push Changes to a GitHub Repository

## Aim

To learn how to stage, commit, and push changes made to a cloned GitHub repository using Git version control.

---

## Problem Statement

Git is a distributed version control system that enables developers to track changes, maintain project history, and collaborate effectively. After modifying files in a local repository, the changes must be staged, committed, and pushed to the remote GitHub repository. This workflow ensures that updates are safely stored and shared with other collaborators.

In this experiment, clone a GitHub repository, modify a file, stage the changes, commit them with an appropriate commit message, and push the changes to GitHub.

---

## Objectives

- Understand the Git workflow.
- Stage modified files using Git.
- Commit changes with meaningful commit messages.
- Push local commits to a remote GitHub repository.
- Verify the updated repository on GitHub.

---

## Requirements

Perform the following tasks:

1. Clone an existing GitHub repository.
2. Modify a file (e.g., `README.md`).
3. Stage the modified file using:
   ```bash
   git add .
   ```
   or
   ```bash
   git add README.md
   ```
4. Commit the changes using:
   ```bash
   git commit -m "Updated README"
   ```
5. Push the changes to GitHub using:
   ```bash
   git push origin main
   ```
6. Verify that the changes are reflected in the GitHub repository.

---

## Tools Required

- Git
- GitHub
- Visual Studio Code (or any text editor)
- Git Bash / Terminal

---

## Files Required

- README.md (or any modified project file)

---

## Sample Git Commands

### Clone Repository

```bash
git clone https://github.com/<username>/<repository-name>.git
```

### Navigate to Repository

```bash
cd <repository-name>
```

### Check Status

```bash
git status
```

### Stage Changes

```bash
git add README.md
```

### Commit Changes

```bash
git commit -m "Updated README"
```

### Push Changes

```bash
git push origin main
```

---

## Deliverables

- Cloned Repository
- Modified File
- Git Commit
- Updated GitHub Repository
- Screenshots of:
  - Modified file
  - Git status
  - Successful commit
  - Successful push
  - Updated GitHub repository

---

## Expected Outcome

The modified file is successfully staged, committed, and pushed to the remote GitHub repository. The updated changes are reflected on GitHub, demonstrating the complete Git workflow for committing and sharing project updates.
