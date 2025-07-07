# 📊 Analysis of Ignored Fields

This project is designed to analyze the behavior of included, excluded, and ignored fields in XML-based scenarios and compute field-level statistics across multiple configurations.

---

## 🐍 Python Setup

### 1. Install Python

Download Python (version 3.13 or higher) from your local software center or from the official website:  
👉 https://www.python.org/downloads/

> ✅ Ensure you check **"Add Python to PATH"** during installation.

---

### 2. Configure Artifactory Access (Environment Variables)

This project uses internal packages hosted on JFrog Artifactory.

#### 🔐 Steps:

1. Go to [JFrog Artifactory Login](https://artifactory.cib.echonet/ui/login/)
2. Generate your identity token
3. Set the following environment variables:

```bash
ARTIFACTORY_KEY=your_identity_token
ARTIFACTORY_USER=your_username
'''
# 📦 pip_cib Setup for Artifactory Access

This guide explains how to define and use the `pip_cib` variable to install Python packages from the internal Artifactory repository.

---

## 🔧 Define the `pip_cib` Environment Variable

Set the following environment variable in your system:

```bash

pip_cib=--trusted-host artifactory.cib.echonet --index-url https://<uid>:<key>@artifactory.cib.echonet/artifactory/api/pypi/pypi/simple
