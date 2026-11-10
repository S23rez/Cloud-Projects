# 🐍 Cloud Infrastructure Automation & Security Tooling

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://python.org)
[![Author](https://img.shields.io/badge/Developer-Odunuga%20Fatai%20Olayinka-0A66C2.svg?logo=linkedin)](https://github.com/S23rez)
[![Domain](https://img.shields.io/badge/Domain-Cloud%20Automation%20%26%20SecOps-red.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

A collection of lightweight Python automation and security validation scripts developed by **Odunuga Fatai Olayinka**. These tools illustrate foundational principles of remote cloud environment fingerprinting, programmatic identity verification, brute-force lockout throttling, and role-based clearance validation.

---

## 🛠️ Tool Catalog & Technical Capabilities

### 1. 🔍 Cloud Server Telemetry & Environment Probe
* 📄 **File:** [`check_server.py`](file:///c:/Users/Suarez/My-Portfolios/Cloud-Projects/Cloud_Automation/check_server.py)
* **Objective:** Programmatically discovers and audits the host operating system, logged-in identity, and execution context of a deployed cloud instance (e.g., DigitalOcean Droplet, AWS EC2, or Azure VM).
* **Technical Details:** Uses Python standard libraries `platform` and `os` to report:
  * Operating system distribution and kernel release version.
  * Active execution user identity (`os.getlogin()`).
  * Current working directory (`os.getcwd()`).
* **Security Use Case:** Cloud instance post-provisioning sanity check and configuration drift auditing.

---

### 2. 🛡️ Role-Based Access Clearance Validator
* 📄 **File:** [`Architect.py`](file:///c:/Users/Suarez/My-Portfolios/Cloud-Projects/Cloud_Automation/Architect.py)
* **Objective:** Implements an interactive multi-tier identity challenge system with brute-force threshold detection and input validation.
* **Technical Details:**
  * **Input Sanitization:** Intercepts raw user input, enforces strict string-to-numeric type validation (`isdigit()`), and prevents unhandled type exceptions.
  * **Brute-Force Countermeasures:** Tracks unauthorized clearance attempts (`strikes`) and terminates execution with a `"Lockdown"` state upon reaching 3 failed attempts.
  * **Role-Based Clearance Routing:** Evaluates numeric clearance tiers (0: Alarm, <100: Low Priority, >=100: High Priority).
  * **Administrative Privilege Check:** Recognizes administrative identities (`Suarez`, `Admin Shutdown`) with zero-fault reset logic.

---

### 3. 🚨 Challenge & Lockdown Security Engine
* 📄 **File:** [`scrap.py`](file:///c:/Users/Suarez/My-Portfolios/Cloud-Projects/Cloud_Automation/scrap.py)
* **Objective:** An expanded security challenge engine demonstrating modular functional design, input truthiness verification, and emergency shutdown mechanisms.
* **Technical Details:**
  * **Modular Clearance Sensor:** Encapsulates security evaluation inside a parameterized `clearance_sensor(strikes)` function returning status tokens (`SUCCESS`, `FAIL`, `ALARM`, `RETRY`).
  * **Alarm Tripwires:** Immediate break on zero clearance injection (representing tripwire trip).
  * **Graceful Exit Handling:** Implements `sys.exit()` for controlled administrative terminations.

---

## 🚀 Execution Instructions

```bash
# Navigate to the automation directory
cd Cloud-Projects/Cloud_Automation

# 1. Audit server execution environment
python check_server.py

# 2. Run the Architect clearance gatekeeper
python Architect.py

# 3. Run the modular challenge engine
python scrap.py
```

---

## 👤 Author

**Odunuga Fatai Olayinka**  
Cybersecurity Specialist | Systems & Cloud Security Engineer  
* GitHub: [@S23rez](https://github.com/S23rez)
