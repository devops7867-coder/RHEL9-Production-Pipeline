pipeline {
    agent any
    triggers { pollSCM('H/2 * * * *') }
    environment {
        APP_SERVER = "192.168.56.104" 
        IMAGE_NAME = "docker.io/muhammadisabir/rhel9-app"
        SSH_CRED_ID = "vm2-ssh-key"
        DOCKER_CRED_ID = "dockerhub-creds"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build & Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${DOCKER_CRED_ID}", usernameVariable: 'U', passwordVariable: 'P')]) {
                    sh """
                    sudo podman build -t ${IMAGE_NAME}:latest .
                    echo "$P" | sudo podman login docker.io -u "$U" --password-stdin
                    sudo podman push ${IMAGE_NAME}:latest
                    """
                }
            }
        }
        stage('Deploy to VM2') {
            steps {
                sshagent(["${SSH_CRED_ID}"]) {
                    sh "ssh -o StrictHostKeyChecking=no root@${APP_SERVER} 'sudo podman pull ${IMAGE_NAME}:latest && sudo podman stop my-app || true && sudo podman rm my-app || true && sudo podman run -d --name my-app -p 5000:5000 ${IMAGE_NAME}:latest'"
                }
            }
        }
    }
}
