# Experiment 19 – Implement Continuous Deployment using GitHub Actions for a Dockerized Application

## Aim

To implement a Continuous Deployment (CD) pipeline using GitHub Actions that automatically builds, pushes, and deploys a Dockerized application to a cloud platform.

---

## Problem Statement

Continuous Deployment (CD) is a DevOps practice that automates the deployment of applications whenever changes are pushed to the source code repository. GitHub Actions provides a powerful workflow automation platform that integrates seamlessly with GitHub repositories. Combined with Docker, it enables automated building, testing, and deployment of containerized applications.

In this experiment, create a Dockerized application, configure GitHub Actions to automatically build and push the Docker image to Docker Hub or GitHub Container Registry, and deploy the application to a cloud platform such as AWS ECS, Azure Kubernetes Service (AKS), or Google Kubernetes Engine (GKE). Finally, verify that the deployment occurs automatically whenever new code is pushed to the repository.

---

## Objectives

- Understand Continuous Deployment using GitHub Actions.
- Containerize an application using Docker.
- Create GitHub Actions workflows.
- Automate Docker image build and push.
- Deploy the application automatically to a cloud platform.
- Verify automated deployment after code changes.

---

## Requirements

Perform the following tasks:

1. Create a GitHub repository and push a simple Dockerized application.
2. Create a GitHub Actions workflow to:
   - Checkout the source code.
   - Build the Docker image.
   - Push the Docker image to Docker Hub or GitHub Container Registry.
3. Configure automatic deployment to a cloud platform such as:
   - AWS Elastic Container Service (ECS)
   - Azure Kubernetes Service (AKS)
   - Google Kubernetes Engine (GKE)
4. Test the CI/CD pipeline by pushing new code changes.
5. Verify that the application is automatically rebuilt and deployed.

---

## Tools Required

- Git
- GitHub
- GitHub Actions
- Docker
- Docker Hub or GitHub Container Registry
- Visual Studio Code
- AWS ECS / Azure AKS / Google GKE (or another supported cloud platform)

---

## Files Required

- Dockerfile
- GitHub Actions Workflow (`.github/workflows/deploy.yml`)
- Application Source Code
- README.md

---

## Deliverables

- GitHub Repository
- Dockerized Application
- Dockerfile
- GitHub Actions Workflow
- Docker Image in Docker Hub or GitHub Container Registry
- Successful Workflow Execution
- Automated Cloud Deployment
- Repository Link
- Screenshots of:
  - GitHub Actions workflow
  - Docker image repository
  - Successfully deployed application

---

## Expected Outcome

A Dockerized application is successfully deployed using GitHub Actions. Whenever code changes are pushed to the GitHub repository, the workflow automatically builds the Docker image, pushes it to a container registry, and deploys the latest version of the application to the configured cloud platform, demonstrating an automated Continuous Deployment pipeline.
