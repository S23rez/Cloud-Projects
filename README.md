# ☁️ Cloud Security & Infrastructure Engineering Portfolio

[![Author](https://img.shields.io/badge/Developer-Odunuga%20Fatai%20Olayinka-0A66C2.svg?logo=linkedin)](https://github.com/S23rez)
[![AWS](https://img.shields.io/badge/AWS-19%20Security%20Labs-FF9900.svg?logo=amazon-aws)](https://aws.amazon.com)
[![Azure](https://img.shields.io/badge/Azure-Entra%20ID%20%7C%20VNets-0078D4.svg?logo=microsoft-azure)](https://azure.microsoft.com)
[![Docker](https://img.shields.io/badge/Containerization-Docker-2496ED.svg?logo=docker)](https://docker.com)
[![CI/CD](https://img.shields.io/badge/DevSecOps-GitHub%20Actions-2088FF.svg?logo=github-actions)](https://github.com/features/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

A comprehensive cloud security and infrastructure engineering portfolio developed by **Odunuga Fatai Olayinka**. This repository hosts extensive, hands-on implementations covering cloud architecture, identity governance, network isolation, threat monitoring, cryptographic protection, automated DevSecOps pipelines, and microservice containerization across **Amazon Web Services (AWS)** and **Microsoft Azure**.

---

## 🏗️ Repository Architecture

```text
Cloud-Projects/
├── 📄 README.md                        <- Master Cloud Portfolio Guide
├── 📂 aws-labs/                        <- 19 AWS Security, Networking & Workload Labs
│   ├── 📄 README.md                    <- Master Index of all 19 AWS Labs
│   ├── 📂 Cloud Security with AWS IAM/
│   ├── 📂 Threat Detection with GuardDuty/
│   ├── 📂 Encrypt a Database with AWS KMS/
│   ├── 📂 Secure Secret with Secret Manager/
│   ├── 📂 VPC Monitoring with Flow Logs/
│   ├── 📂 VPC Endpoints/
│   ├── 📂 VPC Peering/
│   ├── 📂 VPC Traffic Flow and Security/
│   └── 📂 ... (11 additional AWS infrastructure & database labs)
├── 📂 azure-labs/                      <- Microsoft Azure Identity & Virtual Network Infrastructure
│   ├── 📄 README.md
│   ├── 📂 entra-id-and-static-web-app-cicd/
│   └── 📂 windows-secnet-vm/
├── 📂 CI-CD Pipeline/                  <- DevSecOps Automation Pipelines
│   ├── 📄 README.md
│   └── 📂 T.O.C-Online-Fashion-Store/
├── 📂 Cloud_Automation/                <- Python Cloud Reconnaissance & Security Clearance Scripts
│   ├── 📄 README.md
│   ├── 📄 Architect.py
│   ├── 📄 check_server.py
│   └── 📄 scrap.py
├── 📂 Docker/                          <- Hardened Containerization Architectures
│   ├── 📄 README.md
│   ├── 📄 Dockerfile
│   └── 📄 app.py
├── 📂 kubernetes-manifests/            <- Declarative Workload & Network Policy Blueprints
│   └── 📄 README.md
└── 📂 terraform-deployments/           <- Infrastructure as Code (IaC) Security Baselines
    └── 📄 README.md
```

---

## 🛠️ Domain Modules & Key Implementations

### 1. 🔶 AWS Cloud Security & Architecture Labs (`aws-labs/`)
* **Scope:** 19 thoroughly tested labs establishing production-style cloud environments.
* **Core Domains:**
  * **Identity & Data Protection:** AWS IAM least-privilege policies, AWS KMS Customer-Managed Key (CMK) encryption at rest, and AWS Secrets Manager automated rotation.
  * **VPC Network Defense:** Multi-tier VPC topologies, public/private subnets, NAT Gateways, VPC Flow Logs analysis, VPC Peering with non-overlapping CIDRs, and VPC Gateway Endpoints for private AWS service communication.
  * **Threat Detection:** AWS GuardDuty continuous threat intelligence monitoring, simulated DNS exfiltration alerts, and compromised credential detection.
  * **Databases & Workloads:** Amazon EC2 secure provisioning, Amazon Aurora high-availability clusters, Amazon S3 static website security, and DynamoDB NoSQL querying.
* 🔗 **Full Catalog:** [aws-labs/README.md](file:///c:/Users/Suarez/My-Portfolios/Cloud-Projects/aws-labs/README.md)

---

### 2. 🔷 Microsoft Azure Identity & Infrastructure (`azure-labs/`)
* **Microsoft Entra ID (Azure AD) & Static Web App CI/CD:** Enterprise cloud identity governance, User Principal Names (UPN), Role-Based Access Control (RBAC), and automated GitHub Actions deployment.
* **Hardened Windows Virtual Network VM:** Azure VNet subnet segmentation, Network Security Groups (NSGs) with priority-based filtering, Azure Bastion integration, and RDP attack surface reduction.
* 🔗 **Full Guide:** [azure-labs/README.md](file:///c:/Users/Suarez/My-Portfolios/Cloud-Projects/azure-labs/README.md)

---

### 3. 🚀 DevSecOps & Automated CI/CD (`CI-CD Pipeline/`)
* **End-to-End Delivery Pipeline:** Production CI/CD workflow leveraging GitHub Actions (`azure-static-web-apps-lively-beach-0ac7b7303.yml`) for continuous testing, build verification, and deployment to Azure Static Web Apps.
* **Secure Application Architecture:** Integration with Firebase Authentication (`authService.js`), environmental secret isolation, and containerized Docker execution.
* 🔗 **Full Guide:** [CI-CD Pipeline/README.md](file:///c:/Users/Suarez/My-Portfolios/Cloud-Projects/CI-CD%20Pipeline/README.md)

---

### 4. 🐍 Cloud Automation & Security Tooling (`Cloud_Automation/`)
* **Telemetry & Discovery:** [`check_server.py`](file:///c:/Users/Suarez/My-Portfolios/Cloud-Projects/Cloud_Automation/check_server.py) for remote server OS fingerprinting, user clearance inspection, and execution context verification.
* **Challenge & Access Control:** [`Architect.py`](file:///c:/Users/Suarez/My-Portfolios/Cloud-Projects/Cloud_Automation/Architect.py) and [`scrap.py`](file:///c:/Users/Suarez/My-Portfolios/Cloud-Projects/Cloud_Automation/scrap.py) implementing brute-force strike tracking, lockout tripwires, clearance code validation, and privilege-level routing.
* 🔗 **Full Guide:** [Cloud_Automation/README.md](file:///c:/Users/Suarez/My-Portfolios/Cloud-Projects/Cloud_Automation/README.md)

---

### 5. 🐳 Container Security & Docker (`Docker/`)
* **Lightweight Isolation:** Minimal attack surface containerization using official `python:3.11-slim` images.
* **Security Practices:** Layer caching optimization, zero extraneous build tools in runtime containers, explicit port mapping (`EXPOSE 5000`), and non-root execution preparation.
* 🔗 **Full Guide:** [Docker/README.md](file:///c:/Users/Suarez/My-Portfolios/Cloud-Projects/Docker/README.md)

---

### 6. ☸️ Kubernetes & Infrastructure as Code (`kubernetes-manifests/` & `terraform-deployments/`)
* **Kubernetes Hardening:** Pod Security Standards, Namespace isolation, NetworkPolicies for east-west traffic containment, and secret management.
* **Terraform IaC Baselines:** Declarative infrastructure provisioning ensuring reproducible, compliant, and auditable cloud deployments.
* 🔗 **Guides:** [kubernetes-manifests/README.md](file:///c:/Users/Suarez/My-Portfolios/Cloud-Projects/kubernetes-manifests/README.md) | [terraform-deployments/README.md](file:///c:/Users/Suarez/My-Portfolios/Cloud-Projects/terraform-deployments/README.md)

---

## 🛡️ Cloud Security Competency Matrix

| Cloud Security Control | Implementation Location | Practical Evidence |
| :--- | :--- | :--- |
| **Identity & Access Management** | `aws-labs/Cloud Security with AWS IAM`, `azure-labs/entra-id-and-static-web-app-cicd` | Least-privilege IAM policies, Entra ID RBAC roles, MFA enforcement |
| **Network Segmentation** | `aws-labs/Build a Virtual Private Cloud`, `azure-labs/windows-secnet-vm` | Private subnets, NAT Gateways, Azure NSG inbound rule whitelisting |
| **Private Transit & Isolation** | `aws-labs/VPC Endpoints`, `aws-labs/Access S3 from a VPC` | AWS PrivateLink, Gateway Endpoints without public internet traversal |
| **Cryptography at Rest** | `aws-labs/Encrypt a Database with AWS KMS`, `Secure Secret with Secret Manager` | Customer-Managed Keys (CMK), envelope encryption, automatic secret rotation |
| **Threat Detection & Logging** | `aws-labs/Threat Detection with GuardDuty`, `VPC Monitoring with Flow Logs` | Flow Log streaming to CloudWatch, ML-based GuardDuty finding analysis |
| **Automated DevSecOps** | `CI-CD Pipeline/T.O.C-Online-Fashion-Store` | GitHub Actions workflow, secret isolation, container build checks |

---

## 👤 Author

**Odunuga Fatai Olayinka**  
Cybersecurity Specialist | Systems & Cloud Security Engineer  
* GitHub: [@S23rez](https://github.com/S23rez)
