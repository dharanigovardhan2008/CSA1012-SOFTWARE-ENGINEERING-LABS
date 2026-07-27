# Experiment 17 – Create a Python Flask API, Containerize it using Docker, Push the Image to Docker Hub, and Deploy it using Kubernetes

## Aim

To develop a simple Python Flask REST API, containerize the application using Docker, push the Docker image to Docker Hub, and deploy the application on Kubernetes using Deployment and Service manifests.

---

## Problem Statement

Modern cloud-native applications are commonly deployed as containers using Docker and orchestrated using Kubernetes. Containerization ensures consistency across environments, while Kubernetes provides scalability, load balancing, and efficient management of containerized applications.

In this experiment, create a simple Flask API, package it into a Docker container, upload the image to Docker Hub, and deploy it on a Kubernetes cluster using Deployment and Service YAML files. Finally, access the API through a NodePort service.

---

## Objectives

- Develop a simple REST API using Python Flask.
- Containerize the Flask application using Docker.
- Build a Docker image.
- Push the Docker image to Docker Hub.
- Create Kubernetes Deployment and Service manifests.
- Deploy the application on Kubernetes.
- Access the API using a NodePort service.

---

## Requirements

Perform the following tasks:

1. Create a Flask application (`app.py`) with basic API endpoints.
2. Create a `requirements.txt` file containing the required Python packages.
3. Write a `Dockerfile` to containerize the Flask application.
4. Build the Docker image using Docker.
5. Push the Docker image to Docker Hub.
6. Create Kubernetes Deployment (`deployment.yaml`).
7. Create Kubernetes Service (`service.yaml`) using NodePort.
8. Apply the Kubernetes manifests.
9. Verify the deployment and access the API through the assigned NodePort.

---

## Tools Required

- Python 3.x
- Flask
- Docker Desktop
- Docker Hub Account
- Kubernetes (Minikube, Docker Desktop Kubernetes, or Kind)
- kubectl
- Visual Studio Code

---

## Files Required

- app.py
- requirements.txt
- Dockerfile
- deployment.yaml
- service.yaml

---

## Sample Docker Commands

### Build Docker Image

```bash
docker build -t flask-api .
```

### Run Docker Container

```bash
docker run -d -p 5000:5000 flask-api
```

### Tag Image

```bash
docker tag flask-api username/flask-api:v1
```

### Push Image

```bash
docker push username/flask-api:v1
```

---

## Sample Kubernetes Commands

### Deploy Application

```bash
kubectl apply -f deployment.yaml
```

### Create Service

```bash
kubectl apply -f service.yaml
```

### Verify Pods

```bash
kubectl get pods
```

### Verify Services

```bash
kubectl get svc
```

---

## Deliverables

- Flask API (`app.py`)
- `requirements.txt`
- Dockerfile
- Docker Image
- Docker Hub Repository
- Kubernetes Deployment YAML
- Kubernetes Service YAML
- Running Kubernetes Pods
- Running Service
- Screenshot of API running in Browser/Postman
- Screenshot of Docker Hub Repository

---

## Expected Outcome

A Python Flask REST API is successfully containerized using Docker, uploaded to Docker Hub, and deployed on a Kubernetes cluster using Deployment and Service manifests. The application should be accessible through a NodePort service, demonstrating successful cloud-native application deployment.
