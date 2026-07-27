# Experiment 18 – Set Up a CI/CD Pipeline using Jenkins, Docker, and Cloud Deployment

## Aim

To implement a Continuous Integration and Continuous Deployment (CI/CD) pipeline using Jenkins for automating the build, testing, and deployment of a containerized application.

---

## Problem Statement

Continuous Integration and Continuous Deployment (CI/CD) are essential DevOps practices that automate software development workflows. Jenkins is a widely used automation server that integrates with Git repositories, Docker, and cloud platforms to automate application building, testing, and deployment.

In this experiment, set up Jenkins, containerize a sample application using Docker, create a Jenkins pipeline to automate the build and deployment process, and configure Jenkins to trigger builds automatically when code changes are pushed to a Git repository.

---

## Objectives

- Understand the concepts of CI/CD.
- Install and configure Jenkins.
- Containerize an application using Docker.
- Create a Jenkins Pipeline using a Jenkinsfile.
- Automate application build, testing, and deployment.
- Configure Jenkins to trigger builds on Git commits or Pull Requests.

---

## Requirements

Perform the following tasks:

1. Set up Jenkins on a local machine or server.
2. Create a Dockerfile to containerize a sample application.
3. Write a Jenkinsfile to automate the following:
   - Checkout source code
   - Build the application
   - Run automated tests
   - Build the Docker image
   - Deploy the application to a cloud platform (AWS/GCP) or a local Docker environment
4. Configure Jenkins to automatically trigger builds whenever code is committed or a Pull Request is created.
5. Execute the pipeline successfully and verify the deployment.

---

## Tools Required

- Jenkins
- Docker
- Git
- GitHub
- Visual Studio Code
- Java (JDK)
- AWS / Google Cloud Platform (Optional)

---

## Files Required

- Dockerfile
- Jenkinsfile
- Application Source Code
- README.md (Optional)

---

## Sample Pipeline Stages

1. Source Code Checkout
2. Build Application
3. Run Unit Tests
4. Build Docker Image
5. Push Docker Image (Optional)
6. Deploy Application
7. Verify Deployment

---

## Sample Commands

### Build Docker Image

```bash
docker build -t sample-app .
```

### Run Docker Container

```bash
docker run -d -p 8080:80 sample-app
```

### View Running Containers

```bash
docker ps
```

---

## Deliverables

- Jenkins Installation
- Dockerfile
- Jenkinsfile
- Docker Image
- Successful Jenkins Pipeline
- Running Docker Container
- Deployment to Cloud or Local Environment
- Screenshots of Jenkins Pipeline Execution
- Screenshot of Running Application

---

## Expected Outcome

A CI/CD pipeline is successfully configured using Jenkins to automate the building, testing, containerization, and deployment of a sample application. The pipeline should automatically execute whenever changes are pushed to the Git repository, demonstrating an efficient DevOps workflow.
