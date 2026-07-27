# Experiment 16 – Create a Static Website and Containerize it using Docker

## Aim

To create a simple static website and deploy it using Docker by containerizing the website with the Nginx web server.

---

## Problem Statement

Docker is a popular containerization platform that allows applications to run consistently across different environments. By packaging a static website along with the Nginx web server into a Docker container, developers can quickly deploy and serve web applications without worrying about system dependencies.

Using **Docker**, create a simple static website, containerize it with Nginx, build a Docker image, run the container, and access the website through a web browser.

---

## Objectives

- Understand the basics of Docker containerization.
- Create a simple static HTML website.
- Write a Dockerfile using the Nginx base image.
- Build a Docker image.
- Run the Docker container.
- Access the deployed website through a browser.

---

## Requirements

Perform the following tasks:

1. Create a simple static website (`index.html`) with basic HTML content.
2. Write a `Dockerfile` to serve the website using the Nginx web server.
3. Build the Docker image.
4. Run the Docker container.
5. Verify that the website is accessible through a web browser.

---

## Tools Required

- Docker Desktop
- Visual Studio Code (or any text editor)
- Web Browser (Google Chrome, Microsoft Edge, Firefox, etc.)

---

## Files Required

### index.html

A simple HTML page containing the website content.

### Dockerfile

A Dockerfile that uses the official Nginx image and copies the website files into the Nginx web directory.

---

## Sample Docker Commands

### Build Docker Image

```bash
docker build -t static-website .
```

### Run Docker Container

```bash
docker run -d -p 8080:80 --name static-site static-website
```

### Verify Running Containers

```bash
docker ps
```

### Stop Container

```bash
docker stop static-site
```

### Remove Container

```bash
docker rm static-site
```

---

## Deliverables

- index.html
- Dockerfile
- Docker Image
- Running Docker Container
- Screenshot of the Website in Browser
- Screenshot of Docker Desktop or Terminal showing the running container

---

## Expected Outcome

A simple static website is successfully containerized using Docker and served through the Nginx web server. The website should be accessible from a web browser using:

```
http://localhost:8080
```

demonstrating successful containerization and deployment using Docker.
