# 🔐 SSH Log Analyzer

A lightweight Python script designed to detect **failed login attempts** from Linux `auth.log` files. Perfect for manual server security audits and keeping an eye on suspicious activity.

---

## 📋 Requirements

* **Python 3.6+**
* **Zero External Dependencies**: Uses only built-in Python modules (`os`, `re`).
* **Root/Sudo Access**: Only required if you are reading directly from `/var/log/auth.log`.

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone [https://github.com/username/ssh-log-analyzer.git](https://github.com/username/ssh-log-analyzer.git)
cd ssh-log-analyzer
