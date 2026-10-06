# Cloud Application Deployment (IT 3200)

**Student Name:** Jordan Naegle  
**Student ID:** 10778552  
**Institution:** Utah Valley University  
**Technology Stack:** Python Flask, Docker, AWS EC2 (Ubuntu Linux)

---

## 📌 Project Overview
This repository contains a containerized Python Flask web application deployed to an AWS EC2 Linux virtual machine. It demonstrates end-to-end containerization, cloud networking configuration, and public service deployment.

## 🚀 Local Development & Docker Testing

### 1. Build Docker Image
```bash
docker build -t student-app .
```

### 2. Run Container
```bash
docker run -d -p 3000:3000 --name student-app student-app
```

### 3. Verify
Access the app in your browser at:
`http://localhost:3000`

---

## ☁️ Cloud Deployment (AWS EC2)

1. Launch an **Ubuntu 24.04/22.04 LTS** EC2 instance (`t2.micro` or `t3.micro`).
2. Configure the **Security Group** to allow inbound traffic:
   - **Port 22 (SSH)** from your IP.
   - **Port 3000 (Custom TCP)** from `0.0.0.0/0` (Anywhere).
3. Connect via SSH:
   ```bash
   ssh -i your-key.pem ubuntu@<EC2-PUBLIC-IP>
   ```
4. Install Docker Engine on Ubuntu:
   ```bash
   sudo apt update
   sudo apt install -y docker.io
   sudo systemctl enable --now docker
   sudo usermod -aG docker ubuntu
   ```
5. Clone and run:
   ```bash
   git clone https://github.com/<YOUR-USERNAME>/<YOUR-REPO-NAME>.git
   cd <YOUR-REPO-NAME>
   sudo docker build -t student-app .
   sudo docker run -d -p 3000:3000 --name student-app student-app
   ```
6. Access in your browser:
   `http://<EC2-PUBLIC-IP>:3000`
