# 🔷 Microsoft Azure Identity, Infrastructure & Security Labs

[![Azure](https://img.shields.io/badge/Microsoft%20Azure-Enterprise%20Labs-0078D4.svg?logo=microsoft-azure)](https://azure.microsoft.com)
[![Author](https://img.shields.io/badge/Developer-Odunuga%20Fatai%20Olayinka-0A66C2.svg?logo=linkedin)](https://github.com/S23rez)
[![Entra ID](https://img.shields.io/badge/Identity-Microsoft%20Entra%20ID-blue.svg)](#)
[![VNet](https://img.shields.io/badge/Networking-Azure%20VNet%20%26%20NSG-green.svg)](#)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF.svg?logo=github-actions)](https://github.com)

A specialized laboratory suite documenting production-validated enterprise cloud architectures on **Microsoft Azure**, developed and documented with photographic evidence by **Odunuga Fatai Olayinka**.

This repository focuses on two essential pillars of enterprise cloud security:
1. **Cloud Identity Governance & Automated Application Deployment** via Microsoft Entra ID and GitHub Actions CI/CD.
2. **Hardened Virtual Machine & Network Defense** via Virtual Networks (VNets), strict Network Security Groups (NSGs), and perimeter access controls.

---

## 📁 Laboratory Modules

```text
azure-labs/
├── 📄 README.md                                  <- Master Azure Labs Guide
├── 📂 entra-id-and-static-web-app-cicd/          <- Entra ID, RBAC & Azure Static Web App CI/CD
│   ├── 📄 README.md                              <- Comprehensive Lab Documentation (10.6 KB)
│   └── 🖼️ 1.jpg - 14.jpg                         <- Photographic Execution Evidence
└── 📂 windows-secnet-vm/                         <- Hardened Windows VM & Network Security Groups
    ├── 📄 README.md                              <- Comprehensive Lab Documentation (9.1 KB)
    └── 🖼️ 1.jpg - 12.jpg                         <- Photographic Execution Evidence
```

---

## 🛠️ Lab Overviews & Security Implementations

### 1. 🔑 Microsoft Entra ID (Azure AD) & Static Web App CI/CD
* 🔗 **Full Documentation:** [entra-id-and-static-web-app-cicd/README.md](file:///c:/Users/Suarez/My-Portfolios/Cloud-Projects/azure-labs/entra-id-and-static-web-app-cicd/README.md)
* **Architectural Scope:** Enterprise identity management integrated with a modern GitOps continuous deployment pipeline.
* **Key Security & Engineering Features:**
  * **Microsoft Entra ID Provisioning:** Configures directory tenants, User Principal Names (UPN), security groups, and Role-Based Access Control (RBAC) role assignments.
  * **Automated CI/CD Pipeline:** Connects GitHub Actions with Azure Static Web Apps, executing automated workflow builds on `main` push and staging preview deployments for pull requests.
  * **Secret Management & Token Security:** Secures deployment tokens using GitHub repository secrets, preventing credential exposure.
  * **Custom Domain & SSL Enforcement:** Validates automatic TLS/SSL certificate issuance and HTTPS enforcement.
* **Verification:** Validated with 14 photographic screenshots documenting each step from tenant configuration to live deployment.

---

### 2. 🛡️ Hardened Windows Virtual Network & NSG Architecture
* 🔗 **Full Documentation:** [windows-secnet-vm/README.md](file:///c:/Users/Suarez/My-Portfolios/Cloud-Projects/azure-labs/windows-secnet-vm/README.md)
* **Architectural Scope:** Isolated cloud computing infrastructure protected by stateful packet filtering and network micro-segmentation.
* **Key Security & Engineering Features:**
  * **Virtual Network (VNet) Design:** Custom address spaces (`10.0.0.0/16`) segmented into dedicated compute subnets.
  * **Network Security Groups (NSGs):** Priority-ordered inbound and outbound security rules enforcing strict least-privilege traffic flow.
  * **RDP Attack Surface Reduction:** Disallows wide-open inbound port 3389 rules; implements IP whitelisting and Bastion host architecture to prevent automated brute-force attacks.
  * **System Hardening & Baseline Testing:** Deploys a Windows Server VM, verifies interface bindings, and conducts connectivity testing using PowerShell and network monitoring utilities.
* **Verification:** Validated with 12 photographic screenshots documenting network topology, NSG rule creation, and VM verification.

---

## 🏛️ Enterprise Security Correlation

| Security Control | Entra ID CI/CD Lab | Windows SecNet VM Lab |
| :--- | :--- | :--- |
| **Authentication & Authorization** | Microsoft Entra ID, OAuth2, RBAC | Windows local accounts & Active Directory integration |
| **Perimeter & Transit Defense** | HTTPS/TLS 1.3, Azure CDN Edge | Azure Network Security Groups, Stateful Firewall |
| **Supply Chain / DevSecOps** | GitHub Actions automated build checks | Immutable VM image baselines |
| **Auditability & Forensics** | Azure deployment audit logs | Azure Network Watcher & NSG flow logs |

---

## 👤 Author

**Odunuga Fatai Olayinka**  
Cybersecurity Specialist | Systems & Cloud Security Engineer  
* GitHub: [@S23rez](https://github.com/S23rez)
