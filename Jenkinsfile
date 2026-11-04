pipeline {
    agent any

    environment {
        IMAGE_NAME = 'chandan0724/devops-task-manager'
        APP_CONTAINER = 'devops-task-manager-cd'
    }

    stages {
        stage('Install Dependencies') {
            agent {
                docker {
                    image 'python:3.12-slim'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            agent {
                docker {
                    image 'python:3.12-slim'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
                sh 'docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    sh '''
                        echo "$DOCKERHUB_TOKEN" | docker login \
                            -u "$DOCKERHUB_USER" --password-stdin

                        docker push ${IMAGE_NAME}:${BUILD_NUMBER}
                        docker push ${IMAGE_NAME}:latest

                        docker logout
                    '''
                }
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    docker pull ${IMAGE_NAME}:${BUILD_NUMBER}

                    docker rm -f ${APP_CONTAINER}-new || true

                    docker run -d \
                        --name ${APP_CONTAINER}-new \
                        -p 5003:5000 \
                        ${IMAGE_NAME}:${BUILD_NUMBER}
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    for i in $(seq 1 10); do
                        if curl -fsS http://localhost:5003/health; then
                            echo "Application is healthy!"
                            exit 0
                        fi
                        echo "Waiting for application..."
                        sleep 3
                    done

                    echo "Health check failed!"
                    exit 1
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline and deployment completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
