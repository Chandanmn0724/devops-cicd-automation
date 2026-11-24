
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venom&height=200&color=0:0B1020,50:123B65,100:06B6D4&text=DEVOPS%20CI%2FCD%20AUTOMATION&fontColor=FFFFFF&fontSize=34&fontAlignY=43&desc=CONTAINERIZED%20TASK%20MANAGER&descSize=17&descAlignY=65" width="100%" />

<br/>

<img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?style=for-the-badge&logo=jenkins&logoColor=white"/>
<img src="https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white"/>

<br/><br/>

**Automating application testing and containerization with Jenkins and Docker.**

</div>

---

## 📌 Project Overview

DevOps CI/CD Automation is a project that demonstrates the development and automation of a Python Flask-based Task Manager application.

The application is containerized using Docker and integrated with Jenkins to automate the development and testing workflow. Pytest is used for automated testing, while Docker provides a consistent environment for running the application.

The project demonstrates practical concepts of application development, containerization, CI/CD automation and deployment.

## 🎯 Project Objectives

- Develop a Python Flask-based Task Manager application.
- Create REST API endpoints for application functionality.
- Containerize the application using Docker.
- Configure Jenkins for CI/CD automation.
- Automate application testing using Pytest.
- Work with application deployment and health checks.

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    A["Developer"] --> B["GitHub Repository"]
    B --> C["Jenkins Pipeline"]

    C --> D["Checkout Source Code"]
    D --> E["Install Dependencies"]
    E --> F["Run Automated Tests - Pytest"]

    F --> G["Docker Image Build"]
    G --> H["Docker Container"]
    H --> I["Flask Task Manager API"]
    I --> J["Application Health Check"]

    style A fill:#123B65,color:#fff,stroke:#38BDF8
    style B fill:#123B65,color:#fff,stroke:#38BDF8
    style C fill:#164E63,color:#fff,stroke:#22D3EE
    style F fill:#164E63,color:#fff,stroke:#22D3EE
    style H fill:#164E63,color:#fff,stroke:#22D3EE
    style J fill:#14532D,color:#fff,stroke:#4ADE80
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.12 | Application development |
| Flask | REST API backend |
| Docker | Application containerization |
| Jenkins | CI/CD pipeline automation |
| Pytest | Automated testing |
| Gunicorn | Python application server |
| Linux | Development environment |
| Git & GitHub | Version control and source code management |
| Docker Compose | Container management |

---

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

---

## ⚙️ CI/CD Pipeline

The project uses Jenkins to automate important stages of the application workflow.

### Pipeline Stages

**1. Source Code Checkout**

- Retrieves the application source code from GitHub.
- Provides the source code required for the pipeline.

**2. Install Dependencies**

- Installs the required Python dependencies.
- Prepares the environment for application testing.

**3. Automated Testing**

- Executes test cases using Pytest.
- Helps verify application functionality.

**4. Docker Image Build**

- Builds a Docker image for the Flask application.
- Packages the application and its dependencies.

**5. Deployment and Health Checks**

- Uses the configured deployment process.
- Checks application availability through its health endpoint.

---

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/ChandanMN0724/devops-cicd-automation.git

cd devops-cicd-automation
```

### 2. Build the Docker Image

```bash
docker build -t devops-task-manager .
```

### 3. Run the Docker Container

```bash
docker run -d -p 5001:5000 --name devops-task-manager devops-task-manager
```

### 4. Verify Application Health

```bash
curl http://localhost:5001/health
```

### 5. Run Automated Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Execute tests:

```bash
pytest
```

---

## 🔗 Application Endpoints

The Flask application includes the following endpoints:

| Endpoint | Description |
|---|---|
| `/` | Application home endpoint |
| `/health` | Application health check |
| `/tasks` | Task management endpoint |

---

## 📸 Project Screenshots

Screenshots of the application, Docker containers and Jenkins pipeline execution will be added here.

| Component | Screenshot |
|---|---|
| Jenkins Pipeline | Coming soon |
| Docker Container | Coming soon |
| Flask Application | Coming soon |

---

## 📚 Key Learning Outcomes

- Understanding CI/CD pipeline concepts.
- Building and managing Docker images and containers.
- Automating Python application testing with Pytest.
- Integrating GitHub with Jenkins.
- Working with Flask REST APIs.
- Understanding application deployment and health checks.
- Working with Linux and containerized environments.

---

## 👨‍💻 About the Developer

**Chandan M N**

B.E. Graduate in Artificial Intelligence and Data Science  
Srinivas Institute of Technology

Interested in Python Development, Backend Engineering, Software Development and DevOps.

<div align="center">

<a href="https://github.com/ChandanMN0724">
<img src="https://img.shields.io/badge/GitHub-View_Profile-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<a href="https://www.linkedin.com/in/chandanmn07">
<img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

<a href="mailto:mnchandan605@gmail.com">
<img src="https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/>
</a>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:06B6D4,100:123B65&height=100&section=footer" width="100%"/>

**BUILD • AUTOMATE • DEPLOY • IMPROVE**

</div>
