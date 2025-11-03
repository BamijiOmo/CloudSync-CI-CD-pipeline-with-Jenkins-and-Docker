# ☁️ CloudSync

CloudSync is a cloud-native file synchronization backend built with Node.js, Docker, and Jenkins. It showcases automated CI/CD, containerized deployment, and scalable cloud infrastructure 

## 🚀 Tech Stack

- **Backend**: Node.js (Express)
- **CI/CD**: Jenkins
- **Containerization**: Docker
- **Cloud Deployment**: AWS EC2 (t3.large)

## 📦 Features

- RESTful API for file sync and status checks
- Dockerized backend for consistent deployment
- Jenkins pipeline with multi-stage automation:
  - Dependency installation
  - App runtime validation
  - Docker image build
  - Deployment placeholder for EC2/Kubernetes

## 🔧 CI/CD Pipeline Overview

**Flow:**  
GitHub Push → Jenkins Trigger → Install Dependencies → Run App & Validate → Docker Build → Deploy to EC2

## 📂 Project Structure

CloudSync/ ├── src/ │ └── server.js ├── Dockerfile ├── Jenkinsfile ├── package.json └── README.md


## 🧪 Sample Output

```bash
curl http://localhost:3000
☁️ CloudSync backend is live — CI/CD pipeline initialized.
