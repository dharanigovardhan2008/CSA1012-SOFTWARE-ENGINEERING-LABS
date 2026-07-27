# Experiment 28 – Pull the Latest Changes from a GitHub Repository

## Aim

To learn how to synchronize a local Git repository with its remote GitHub repository by pulling the latest changes made by collaborators.

---

## Problem Statement

In collaborative software development, multiple developers work on the same GitHub repository. When a collaborator pushes new changes to the remote repository, other team members must update their local repositories to stay synchronized. Git provides the `git pull` command to fetch and merge the latest changes from the remote repository into the local working directory.

In this experiment, clone a GitHub repository, allow a collaborator to make changes and push them to GitHub, pull the latest updates using Git, and verify that the collaborator's changes are reflected in the local repository.

---

## Objectives

- Understand collaborative development using Git and GitHub.
- Learn how to fetch and merge remote changes.
- Use the `git pull` command.
- Synchronize a local repository with the remote repository.
- Verify updates made by collaborators.

---

## Requirements

Perform the following tasks:

1. Clone an existing GitHub repository.
2. Ask a collaborator to modify a file and push the changes to GitHub.
3. Open the local repository.
4. Pull the latest changes using:

   ```bash
   git pull origin main
   ```

5. Verify that the collaborator's changes are successfully merged into the local repository.
6. Confirm the repository is up to date.

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

### Pull Latest Changes

```bash
git pull origin main
```

### Verify Repository Status

```bash
git status
```

---

## Deliverables

- Cloned GitHub Repository
- Updated Local Repository
- Successfully Pulled Changes
- Screenshots of:
  - Collaborator's changes on GitHub
  - Successful `git pull`
  - Updated local repository
  - `git status` showing the repository is up to date

---

## Expected Outcome

The latest changes from the remote GitHub repository are successfully pulled into the local repository. The collaborator's modifications appear in the local copy, demonstrating effective synchronization and collaboration using Git and GitHub.
