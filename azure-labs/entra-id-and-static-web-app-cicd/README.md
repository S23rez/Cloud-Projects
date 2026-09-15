# 🚀 Azure IAM Setup & Azure Static Web App CI/CD Deployment Guide

[![Azure](https://img.shields.io/badge/Microsoft_Azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org/)
[![Security](https://img.shields.io/badge/IAM-Least_Privilege-green?style=for-the-badge&logo=azure-active-directory&logoColor=white)](https://learn.microsoft.com/en-us/azure/active-directory/)

A comprehensive, production-grade graphical guide detailing the end-to-end setup of **Least-Privilege Identity & Access Management (IAM)** in Microsoft Entra ID and automated deployment of a **React Frontend Application** to **Azure Static Web Apps** via **GitHub Actions CI/CD**.

---

## 📊 End-to-End Architecture & Workflow

```mermaid
flowchart TD
    classDef azure fill:#0078D4,stroke:#004578,color:#fff,font-weight:bold;
    classDef github fill:#24292e,stroke:#1b1f23,color:#fff,font-weight:bold;
    classDef security fill:#107C41,stroke:#0b5a2f,color:#fff,font-weight:bold;
    classDef user fill:#6B69D6,stroke:#4B49B6,color:#fff,font-weight:bold;

    subgraph Phase1 ["🔒 Phase 1 & 2: Least-Privilege IAM Provisioning"]
        U1["Global Admin / Owner"]:::user -->|1. Access Microsoft Entra ID| E1["Tenant: Default Directory"]:::azure
        E1 -->|2. Provision User| U2["Dev Admin (Developer@...)"]:::azure
        U2 -->|3. Scope Role Assignment| IAM["Subscription Access Control (IAM)"]:::security
        IAM -->|4. Grant Role| R1["Role: Contributor"]:::security
    end

    subgraph Phase2 ["🛡️ Phase 3: Identity Protection & Verification"]
        U2 -->|5. Sign In with Temp Password| MFA1["Password Reset Prompt"]:::security
        MFA1 -->|6. Register Device| MFA2["Microsoft Authenticator App"]:::security
        MFA2 -->|7. Verify Portal Access| DASH["Dev Admin Portal (No Credit Access)"]:::azure
    end

    subgraph Phase3 ["⚡ Phase 4: SWA Provisioning & CI/CD Deployment"]
        DASH -->|8. Create Resource| SWA["Azure Static Web App (toc-fashion-store)"]:::azure
        SWA -->|9. OAuth Authorization| GH["GitHub Org: S23rez"]:::github
        GH -->|10. Link Repository| REPO["Repository: toc-fashion-store-production"]:::github
        SWA -->|11. Auto-Inject Workflow| WF[".github/workflows/azure-static-web-apps-*.yml"]:::github
        WF -->|12. Trigger CI/CD Build| ACT["GitHub Actions Agent (React: ./toc-store -> dist)"]:::github
        ACT -->|13. Deploy Static Assets| CDN["Azure Global CDN Edge Endpoint"]:::azure
    end
```

---

## 🗂️ Detailed Sequence Diagram

```mermaid
sequenceDiagram
    autonumber
    actor Admin as Global Admin / Owner
    actor Dev as Developer (Dev Admin)
    participant Entra as Microsoft Entra ID
    participant IAM as Azure Subscription IAM
    participant SWA as Azure Static Web App
    participant GH as GitHub Actions

    Admin->>Entra: Create User "Dev Admin" (Developer@SuarezOdu...)
    Entra-->>Admin: Return Temp Password (********)
    Admin->>IAM: Assign "Contributor" Role to "Dev Admin"
    IAM-->>Admin: Role Assignment Confirmed
    
    Dev->>Entra: First Sign-in with Temp Credentials
    Entra->>Dev: Prompt for Password Change & MFA Registration
    Dev->>Entra: Complete Microsoft Authenticator Enrollment
    Entra-->>Dev: MFA Verified & Portal Token Issued
    
    Dev->>SWA: Provision Static Web App ("toc-fashion-store")
    SWA->>GH: Authenticate via OAuth & Link "toc-fashion-store-production"
    GH-->>SWA: Repository Authorized (Branch: main)
    SWA->>GH: Commit Workflow File (.github/workflows)
    GH->>GH: Execute Build (npm run build -> dist)
    GH->>SWA: Deploy Compiled Assets to Global CDN
    SWA-->>Dev: Deployment Successful (URL Generated)
```

---

## 📋 Comprehensive Execution Matrix

| Step # | Phase | Operation | Component | Exact Value / Parameter                               | Security Purpose |
| :---: | :--- | :--- | :--- |:------------------------------------------------------| :--- |
| **01** | IAM Setup | Tenant Inspection | Microsoft Entra ID | Tenant ID: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`     | Verify target directory scope before changes |
| **02** | IAM Setup | User Navigation | Users Blade | `+ New user` -> `Create new user`                     | Begin non-root user creation workflow |
| **03** | IAM Setup | Identity Fields | Create User Wizard | UPN: `[Your-Domain].onmicrosoft.com`     | Create dedicated developer identity |
| **04** | IAM Setup | Review Credentials | Create User Wizard | Display Name: `Dev Admin`                             | Generate temporary credentials securely |
| **05** | IAM Scope | Subscription Review | Subscriptions | ID: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`                                                | Confirm target subscription container |
| **06** | IAM Scope | IAM Navigation | Access Control (IAM) | `Add role assignment`                                 | Initiate role delegation workflow |
| **07** | IAM Scope | Role Assignment | Add Role Assignment | Role: `Contributor`                                   | Enforce zero-billing non-root access |
| **08** | IAM Scope | Verification | Role Assignments | Scope: `This resource` (Subscription)                 | Confirm rule binding in RBAC |
| **09** | MFA | Authentication | Authenticator App | Microsoft Authenticator App linked                    | Enforce 2FA/MFA compliance |
| **10** | MFA | Access Verification | Portal Dashboard | Notice: `"You don't have permission to view credits"` | Validate least-privilege scoping working |
| **11** | Deployment | Resource Creation | Static Web Apps | Name: `toc-fashion-store`, Plan: `Free`               | Initiate global static site hosting |
| **12** | Deployment | GitHub Link | Build Config | Repo: `S23rez/toc-fashion-store-production`           | Connect source repository & branch |
| **13** | Deployment | Build Preset | Build Presets | Preset: `React`, App location: `./toc-store`          | Specify build directory and output (`dist`) |
| **14** | Deployment | Verification | Azure Deployment | Status: `Your deployment is complete`                 | CI/CD pipeline live on Azure CDN |

---

## 📸 Step-by-Step Graphical Walkthrough

### Phase 1: Least-Privilege IAM User Creation

#### Step 1: Access Microsoft Entra ID
![Step 1 - Microsoft Entra ID Overview](./1.jpg)
- **Directory**: `Default Directory`
- **Tenant ID**: `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
- **Primary Domain**: `[Your-Domain].onmicrosoft.com`

---

#### Step 2: Navigate to User Management
![Step 2 - Users Blade](./2.jpg)
- Open the **Users** blade in Entra ID and select **+ New user** -> **Create new user**.

---

#### Step 3: Configure User Principal Name
![Step 3 - Identity Fields](./3.jpg)
- **User principal name**: `[Your-Domain].onmicrosoft.com`
- **Mail nickname**: `Developer`
- Select **Auto-generate password** and ensure **Account enabled** is checked.

---

#### Step 4: Save Temporary Credentials & Create User
![Step 4 - Review & Create Account](./4.jpg)
- **Display name**: `Dev Admin`
- **User type**: `Member`
- Securely copy the temporary password before clicking **Create**.

---

### Phase 2: Role Assignment & Access Control (IAM)

#### Step 5: Access Target Subscription
![Step 5 - Subscription Overview](./5.jpg)
- Navigate to **Subscriptions** -> **Azure subscription 1** (`be62833e-22d5-43d0-aaad-02b0338022aa`).

---

#### Step 6: Open Access Control (IAM)
![Step 6 - Access Control Blade](./6.jpg)
- Select **Access control (IAM)** from the subscription sidebar and click **Add role assignment**.

---

#### Step 7: Assign Contributor Role to Dev Admin
![Step 7 - Add Role Assignment](./7.jpg)
- **Role**: `Contributor`
- **Member**: `Dev Admin` (`[Your-Domain].onmicrosoft.com`)
- **Description**: `"Identity Access Management - Having a non root privileged account"`

---

#### Step 8: Confirm Role Scope
![Step 8 - Role Assignment Verification](./8.jpg)
- Verify `Dev Admin` holds the `Contributor` role scoped to `This resource`.

---

### Phase 3: MFA & Identity Protection

#### Step 9: Register Microsoft Authenticator App
![Step 9 - Authenticator MFA Success](./9.jpg)
- Sign in as `Dev Admin`, change temporary password, and scan QR code with **Microsoft Authenticator**.

---

#### Step 10: Verify Least-Privilege Restricted Access
![Step 10 - Dev Admin Portal Welcome](./10.jpg)
- Verify portal welcome banner and notification: *"You don't have permission to view credits"* — proving RBAC restrictions are active.

---

### Phase 4: Azure Static Web App & CI/CD Deployment

#### Step 11: Create Static Web App Resource
![Step 11 - Create SWA Basics](./11.jpg)
- **Resource Name**: `toc-fashion-store`
- **Region**: `Global`
- **Plan**: `Free`
- **Source**: `GitHub`

---

#### Step 12: Connect GitHub Repository & Configure Build
![Step 12 - GitHub Repo and Build Configuration](./12.jpg)
- **Organization**: `S23rez`
- **Repository**: `toc-fashion-store-production`
- **Branch**: `main`
- **Build Preset**: `React (detected)`
- **App location**: `./toc-store`

---

#### Step 13: Review & Submit Deployment
![Step 13 - Review and Validate](./13.jpg)
- Review validation details:
  - **Output location**: `dist`
  - **Resource Group**: `toc-fashion-store_group`
- Click **Create**.

---

#### Step 14: Deployment Complete
![Step 14 - Deployment Successful](./14.jpg)
- Status: **"Your deployment is complete"**
- Azure automatically injected a GitHub Actions workflow into the repository, compiled the React application, and hosted it on Azure's global CDN.

---

## 🛡️ Security & DevOps Best Practices

> [!IMPORTANT]
> **Never use Root / Owner accounts for daily deployments.** Creating dedicated developer accounts with `Contributor` roles isolates resource management from billing and administrative operations.

> [!TIP]
> **Monorepo / Subfolder Builds**: When your frontend project lives inside a subfolder (e.g. `./toc-store`), explicitly configure `App location: ./toc-store` so the GitHub Actions runner navigates to the correct directory before executing `npm install` and `npm run build`.

> [!NOTE]
> **Automated Secret Rotation**: Azure Static Web Apps automatically generates and rotates deployment tokens stored securely inside GitHub Repository Secrets (`AZURE_STATIC_WEB_APPS_API_TOKEN_*`).

---
*Created for Azure Architecture & Deployment Documentation.*
