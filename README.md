# Feedback App – DevOps Assignment 🚀

## 📋 Overview

This is a simple **Flask-based Feedback API** developed and deployed as part of a DevOps Engineer assignment. The project demonstrates containerization using **Docker**, orchestration with **Kubernetes on AWS EKS**, and automation via **GitHub Actions** for a complete **CI/CD pipeline**.

---

## 🧠 Features

- Accept feedback via `POST /feedback`
- Retrieve all feedback via `GET /feedbacks`
- Dockerized Python Flask application
- Kubernetes manifests (Deployment + Service)
- CI/CD pipeline with GitHub Actions
- Deployment on AWS EKS using a `LoadBalancer` service

---
## GitHub Actions

[GitHub Actions] --> (CI) --> [Docker Hub] --> (CD) --> [AWS EKS Cluster] --> [LoadBalancer] --> [Flask API Pod]


---

## ⚙️ Tech Stack

- **Language**: Python + Flask
- **Containerization**: Docker
- **Orchestration**: Kubernetes (EKS)
- **CI/CD**: GitHub Actions
- **Cloud Provider**: AWS (EKS with LoadBalancer)

---

## 🔧 Setup Instructions

### 🐳 Docker

To run locally with Docker:

```bash
docker build -t feedback-app .
docker run -p 5000:5000 feedback-app

Test it at http://localhost:5000/feedback
```

## Apply Manifest

kubectl apply -f k8s/

## Get LoadBalancer

kubectl get svc feedback-service
Access the application using the external IP on port 80.

# Use PostMan to POST/feedback
  Json
{
  "name": "Abhi",
  "message": "Great app!"
}

# Get all Records
GET/feedbacks

