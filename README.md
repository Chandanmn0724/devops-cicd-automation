
<div align="center">

# 🚀 DevOps CI/CD Automation

### Containerized Task Manager using Python, Docker & Jenkins

<img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?logo=jenkins&logoColor=white"/>
<img src="https://img.shields.io/badge/Pytest-Testing-0A9EDC?logo=pytest&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-Backend-black?logo=flask&logoColor=white"/>

</div>

---

## 📌 Project Overview

This project demonstrates the implementation of a CI/CD pipeline for a Python Flask-based Task Manager application.

The application is containerized using Docker, tested using Pytest, and integrated with Jenkins to automate the software build and testing workflow.

## 🎯 Objectives

- Develop a Python Flask-based REST API.
- Containerize the application using Docker.
- Automate application testing using Pytest.
- Configure a Jenkins pipeline.
- Explore application deployment and health checks.

## 🏗️ Project Architecture

```text
          Developer
              |
              v
          GitHub Repo
              |
              v
         Jenkins Pipeline
              |
       +------+------+
       |             |
       v             v
 Install          Run Tests
 Dependencies      (Pytest)
       |             |
       +------+------+
              |
              v
         Docker Build
              |
              v
       Containerized App
              |
              v
       Application Health
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | REST API backend |
| Docker | Containerization |
| Jenkins | CI/CD automation |
| Pytest | Automated testing |
| Linux | Development environment |
| GitHub | Source code management |
| Gunicorn | Python application server |

## 📂 Project Structure

```text
devops-cicd-automation/
│
├── app/
│   └── Application source code
│
├── tests/
│   └── Automated test cases
│
├── Dockerfile
├── Jenkinsfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
└── .gitignore
```

## ⚙️ CI/CD Pipeline

The Jenkins pipeline automates the following stages:

1. **Checkout:** Retrieves source code from GitHub.
2. **Install Dependencies:** Installs required Python packages.
3. **Run Tests:** Executes automated tests using Pytest.
4. **Docker Build:** Builds the container image.
5. **Deployment:** Supports application deployment and health checks as configured.

## 🚀 Run the Application Locally

### 1. Clone the repository

```bash
git clone https://github.com/ChandanMN0724/devops-cicd-automation.git

cd devops-cicd-automation
```

### 2. Build the Docker image

```bash
docker build -t devops-task-manager .
```

### 3. Run the container

```bash
docker run -d -p 5001:5000 --name devops-task-manager devops-task-manager
```

### 4. Check application health

```bash
curl http://localhost:5001/health
```

### 5. Run automated tests

```bash
pip install -r requirements.txt
pytest
```

## 🔍 Key Learning Outcomes

- Understanding CI/CD pipeline implementation.
- Working with Docker images and containers.
- Automating Python application testing.
- Integrating GitHub with Jenkins.
- Understanding application deployment and health checks.

## 👨‍💻 Author

**Chandan M N**

B.E. Artificial Intelligence and Data Science

[GitHub](https://github.com/ChandanMN0724) | [LinkedIn](https://www.linkedin.com/in/chandanmn07)

