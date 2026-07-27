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

1. Install and configure Jenkins on a local machine or server.
2. Create a sample application.
3. Write a `Dockerfile` to containerize the application.
4. Create a `Jenkinsfile` that performs:
   - Source code checkout
   - Build the application
   - Run automated tests
   - Build the Docker image
   - Push the Docker image (optional)
   - Deploy the application to a cloud platform (AWS/GCP) or a local Docker environment
5. Configure Jenkins with the Git repository.
6. Enable automatic build triggers for code commits or Pull Requests.
7. Execute the pipeline successfully.

---

## Tools Required

- Jenkins
- Docker
- Git
- GitHub
- Visual Studio Code
- Java (JDK)
- AWS / Google Cloud Platform (or Local Docker Deployment)

---

## Files Required

- Dockerfile
- Jenkinsfile
- Application Source Code
- README.md (optional)

---

## Sample Jenkins Pipeline Stages

1. Checkout Source Code
2. Build Application
3. Run Unit Tests
4. Build Docker Image
5. Push Docker Image (Optional)
6. Deploy Application
7. Verify Deployment

---

## Sample Jenkins Commands

### Start Jenkins

```bash
java -jar jenkins.war
```

### Build Docker Image

```bash
docker build -t sample-app .
```

### Run Docker Container

```bash
docker run -d -p 8080:80 sample-app
```

### Verify Running Containers

```bash
docker ps
```

---

## Deliverables

- Jenkins Installed and Configured
- Dockerfile
- Jenkinsfile
- Successful Jenkins Build
- Docker Image
- Running Container
- Deployment to Cloud or Local Environment
- Screenshot of Jenkins Pipeline Execution
- Screenshot of Running Application

---

## Expected Outcome

A fully functional CI/CD pipeline is successfully implemented using Jenkins. The pipeline automatically builds, tests, containerizes, and deploys the application whenever changes are committed to the source code repository, demonstrating an automated DevOps workflow.
