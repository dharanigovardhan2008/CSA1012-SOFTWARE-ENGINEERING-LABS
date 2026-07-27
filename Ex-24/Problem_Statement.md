# Experiment 24 – Create a CI/CD Pipeline Using GitHub Actions

## Aim

To create a Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub Actions for a containerized Flask application by automating the build, testing, Docker image creation, and deployment process.

---

## Problem Statement

Continuous Integration and Continuous Deployment (CI/CD) improve software development by automating the processes of building, testing, and deploying applications. GitHub Actions provides a powerful automation platform that integrates directly with GitHub repositories, enabling developers to create workflows that execute automatically when code changes are pushed.

In this experiment, create a GitHub repository containing a Dockerized Flask application. Configure a GitHub Actions workflow to automatically build, test, and push Docker images to Docker Hub. Finally, deploy the application to a cloud platform such as Heroku or Amazon Web Services (AWS) and verify successful deployment.

---

## Objectives

- Understand the concepts of CI/CD.
- Create a GitHub Actions workflow.
- Automate application testing and Docker image building.
- Push Docker images to Docker Hub.
- Deploy a Dockerized Flask application to a cloud platform.
- Verify successful automated deployment.

---

## Requirements

Perform the following tasks:

1. Set up a GitHub repository for a containerized Flask application.
2. Create a GitHub Actions workflow file.
3. Configure the workflow to:
   - Checkout the source code.
   - Install dependencies.
   - Run application tests.
   - Build the Docker image.
   - Push the Docker image to Docker Hub.
4. Deploy the application to a cloud platform such as Heroku or AWS.
5. Verify that the deployment is successful.
6. Submit the GitHub Actions workflow file and the deployment link.

---

## Tools Required

- Git
- GitHub
- GitHub Actions
- Docker
- Docker Hub
- Python 3.x
- Flask
- Visual Studio Code
- Heroku or AWS

---

## Files Required

- app.py
- requirements.txt
- Dockerfile
- .github/workflows/main.yml
- README.md

---

## Deliverables

- GitHub Repository
- Flask Application
- Dockerfile
- GitHub Actions Workflow
- Docker Image in Docker Hub
- Successfully Deployed Application
- Deployment URL
- Screenshots of:
  - GitHub Actions workflow execution
  - Docker Hub repository
  - Running application

---

## Expected Outcome

A Dockerized Flask application is successfully integrated with GitHub Actions to automate testing, Docker image creation, and deployment. Whenever changes are pushed to the GitHub repository, the workflow automatically executes, builds the Docker image, pushes it to Docker Hub, and deploys the latest version of the application to the selected cloud platform.
