# Experiment 30 – Collaborate Using GitHub Fork, Branches, and Pull Requests

## Aim

To understand collaborative software development using Git and GitHub by implementing the Fork and Pull Request workflow, creating feature branches, and contributing changes to an existing repository.

---

## Problem Statement

GitHub provides a collaborative platform where developers can contribute to projects without directly modifying the original repository. The Fork and Pull Request workflow enables contributors to work independently by creating their own copy of a repository, implementing changes in separate branches, and submitting Pull Requests for review and integration.

In this experiment, fork an existing GitHub repository, clone it to the local machine, create a new feature branch, implement a new feature, push the changes to the forked repository, and submit a Pull Request to the original repository.

---

## Objectives

- Understand the Fork and Pull Request workflow.
- Fork an existing GitHub repository.
- Clone a remote repository to the local machine.
- Create and manage feature branches.
- Implement and commit new features.
- Push changes to a forked repository.
- Submit a Pull Request to the original repository.

---

## Requirements

Perform the following tasks:

1. Fork an existing GitHub repository.
2. Clone the forked repository to the local machine.
3. Create a new branch for implementing a feature.
4. Develop the required feature without affecting the existing code.
5. Stage and commit the changes.
6. Push the feature branch to the forked repository.
7. Create a Pull Request from the forked repository to the original repository.
8. Verify that the Pull Request is successfully submitted.

---

## Tools Required

- Git
- GitHub
- Visual Studio Code (or any text editor)
- Git Bash / Terminal

---

## Files Required

- Source Code Files
- README.md (if modified)

---

## Sample Git Commands

### Clone Forked Repository

```bash
git clone https://github.com/<username>/<repository-name>.git
```

### Navigate to Repository

```bash
cd <repository-name>
```

### Create a Feature Branch

```bash
git checkout -b feature-new
```

### Stage Changes

```bash
git add .
```

### Commit Changes

```bash
git commit -m "Implemented new feature"
```

### Push Feature Branch

```bash
git push origin feature-new
```

### Create Pull Request

Open GitHub and create a Pull Request from the **feature-new** branch in your forked repository to the **main** branch of the original repository.

---

## Deliverables

- Forked GitHub Repository
- Feature Branch
- Source Code Changes
- Git Commit History
- Pull Request
- Pull Request Link
- Screenshots of:
  - Forked repository
  - Feature branch
  - Successful push
  - Pull Request creation
  - Pull Request submitted

---

## Expected Outcome

A repository is successfully forked, cloned, and modified using a feature branch. The implemented feature is committed, pushed to the forked repository, and submitted to the original repository through a Pull Request, demonstrating collaborative development using Git and GitHub.
