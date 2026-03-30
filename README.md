# 🚀 RHEL 9.6 Automated CI/CD Production Pipeline

This project demonstrates a full-stack DevOps automation workflow using **Ansible**, **Jenkins**, and **Podman** on **Red Hat Enterprise Linux 9.6**.

## 🏗️ Architecture
- **Jenkins Controller (VM1):** Orchestrates builds and deployments.
- **App Server (VM2):** Runs Nginx Reverse Proxy and Podman containers.
- **Docker Hub:** Centralized image registry.

## 🛠️ Tech Stack
- **Automation:** Ansible (IaC), Jenkins (CI/CD)
- **Containerization:** Podman (Rootless/RHEL Native)
- **Web Server:** Nginx (Reverse Proxy & SELinux Hardened)
- **Cloud:** GitHub, Docker Hub

## 🚀 Quick Start
1. Update `inventory.ini` with your server IPs.
2. Run `ansible-playbook deploy_infrastructure.yml` to provision the servers.
3. Configure Jenkins to point to this GitHub repo.
4. Push code to trigger an automated deployment.
