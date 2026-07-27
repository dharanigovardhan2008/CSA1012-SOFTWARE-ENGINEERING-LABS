# Experiment 23 – Deploy a Multi-Container Application Using Kubernetes

## Aim

To deploy a multi-container application using Kubernetes by creating Deployment and Service YAML files, monitoring the deployed resources, and scaling the application to handle increased user load.

---

## Problem Statement

Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. Multi-container applications typically consist of a frontend, backend, and database that work together to provide complete functionality. Kubernetes manages these components efficiently through Deployments and Services.

In this experiment, create a multi-container application consisting of a frontend, backend, and database. Deploy the application using Kubernetes YAML files, monitor the status of pods and services, scale the frontend deployment, and verify the successful operation of the application.

---

## Objectives

- Understand Kubernetes architecture and orchestration.
- Deploy a multi-container application using Kubernetes.
- Create Deployment and Service YAML files.
- Monitor Kubernetes Pods and Services.
- Scale application deployments.
- Verify successful deployment and scaling.

---

## Requirements

Perform the following tasks:

1. Create a multi-container application consisting of:
   - Frontend
   - Backend
   - Database
2. Create Kubernetes Deployment YAML files for each component.
3. Create Kubernetes Service YAML files to expose the application.
4. Deploy the application using `kubectl` commands.
5. Monitor the status of Pods and Services.
6. Scale the frontend deployment to handle increased traffic.
7. Submit the YAML files and screenshots of the Kubernetes Dashboard.

---

## Tools Required

- Docker
- Kubernetes
- kubectl
- Docker Desktop / Minikube / Kind
- Visual Studio Code

---

## Files Required

- frontend-deployment.yaml
- frontend-service.yaml
- backend-deployment.yaml
- backend-service.yaml
- database-deployment.yaml
- database-service.yaml
- README.md (Optional)

---

## Sample Kubernetes Commands

### Apply Deployments

```bash
kubectl apply -f frontend-deployment.yaml
kubectl apply -f backend-deployment.yaml
kubectl apply -f database-deployment.yaml
```

### Apply Services

```bash
kubectl apply -f frontend-service.yaml
kubectl apply -f backend-service.yaml
kubectl apply -f database-service.yaml
```

### View Pods

```bash
kubectl get pods
```

### View Services

```bash
kubectl get svc
```

### Scale Frontend Deployment

```bash
kubectl scale deployment frontend --replicas=3
```

### Verify Scaling

```bash
kubectl get deployments
```

---

## Deliverables

- Frontend Deployment YAML
- Backend Deployment YAML
- Database Deployment YAML
- Service YAML Files
- Running Kubernetes Pods
- Running Kubernetes Services
- Scaled Frontend Deployment
- Screenshots of:
  - Kubernetes Dashboard
  - Running Pods
  - Running Services
  - Scaled Deployment

---

## Expected Outcome

A multi-container application is successfully deployed using Kubernetes. The frontend, backend, and database communicate through Kubernetes Services, while the frontend deployment is successfully scaled to handle increased load. The application demonstrates effective container orchestration and management using Kubernetes.
