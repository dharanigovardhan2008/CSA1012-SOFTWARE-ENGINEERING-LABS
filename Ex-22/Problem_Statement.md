# Experiment 22 – Push and Pull Docker Images Using Docker Hub

## Aim

To create a Docker image for a static HTML website, push the image to Docker Hub, pull it from Docker Hub on another machine, and run the container successfully.

---

## Problem Statement

Docker Hub is a cloud-based container registry that allows developers to store, share, and distribute Docker images. By pushing Docker images to Docker Hub, applications can be easily deployed and executed on different systems. This experiment demonstrates the process of creating a Docker image for a static HTML website, uploading it to Docker Hub, downloading it on another machine, and running the container.

---

## Objectives

- Understand Docker image creation and management.
- Create a Docker image for a static HTML website.
- Tag Docker images using Docker naming conventions.
- Push Docker images to Docker Hub.
- Pull Docker images from Docker Hub.
- Run Docker containers from downloaded images.

---

## Requirements

Perform the following tasks:

1. Create a Docker image for a static HTML website.
2. Tag the Docker image with your Docker Hub username.
3. Push the Docker image to Docker Hub.
4. Pull the Docker image from Docker Hub on another machine.
5. Run the Docker container and verify that the website is accessible.
6. Submit the Docker commands and screenshots for each step.

---

## Tools Required

- Docker Desktop
- Docker Hub Account
- Visual Studio Code
- Web Browser

---

## Files Required

- index.html
- Dockerfile
- README.md (Optional)

---

## Sample Docker Commands

### Build Docker Image

```bash
docker build -t static-website .
```

### Tag Docker Image

```bash
docker tag static-website <dockerhub-username>/static-website:v1
```

### Push Docker Image

```bash
docker push <dockerhub-username>/static-website:v1
```

### Pull Docker Image

```bash
docker pull <dockerhub-username>/static-website:v1
```

### Run Docker Container

```bash
docker run -d -p 8080:80 <dockerhub-username>/static-website:v1
```

### Verify Running Containers

```bash
docker ps
```

---

## Deliverables

- Static HTML Website
- Dockerfile
- Docker Image
- Docker Hub Repository
- Docker Commands Used
- Screenshots of:
  - Docker image build
  - Docker image push
  - Docker image pull
  - Running Docker container
  - Website opened in a web browser

---

## Expected Outcome

A Docker image for a static HTML website is successfully created, tagged, and pushed to Docker Hub. The image is then pulled onto another machine and executed successfully, demonstrating Docker image sharing and deployment through Docker Hub.
