# Cybersecurity Threat Detection using Hybrid ML and Azure MLOps

This project implements a machine learning-based Intrusion Detection System (IDS) tailored for banking cybersecurity environments. It combines **unsupervised anomaly detection** and **supervised classification** models, deployed with full MLOps lifecycle automation using **Azure Machine Learning** and other Azure services.

## 🔍 Project Overview

Financial institutions face continuous threats, including:
- Brute-force attacks
- Credential stuffing
- Insider threats
- Lateral movement and zero-day exploits

This system learns both **known** and **unknown** threat behaviors using structured network and user behavior data.

---

## 🎯 Objectives

- Build and deploy an ML-powered IDS using supervised and unsupervised learning
- Detect zero-day anomalies and known attack patterns
- Provide explainable alerts to support SOC (Security Operations Center) analysts
- Enable full CI/CD automation using Azure DevOps and Azure ML Pipelines
- Ensure secure, compliant data handling using Azure-native governance tools

---

## 🧠 ML Tasks & Models

### Anomaly Detection (Unsupervised)
- **Goal**: Detect unknown or novel threats
- **Algorithms**: Isolation Forest, Autoencoders
- **Use Cases**: Zero-day exploits, insider threats

### Binary Classification (Supervised)
- **Goal**: Detect known threats using labeled data
- **Algorithms**: Random Forest, XGBoost, Logistic Regression
- **Use Cases**: Brute-force login attempts, known malicious IP usage

### Explainability
- **Tools**: SHAP
- **Integration**: Explanation included in inference pipeline

---

## ⚙️ Azure Architecture

| Component                  | Azure Service                                      |
|---------------------------|----------------------------------------------------|
| Data Storage              | Azure Blob Storage or Azure Data Lake Storage Gen2 |
| Data Exploration          | Azure Databricks                                   |
| Training & Experimentation| Azure Machine Learning + MLflow                    |
| Model Versioning          | Azure ML Model Registry                            |
| Real-Time Deployment      | Azure Kubernetes Service (AKS)                     |
| Batch Inference           | Azure Functions / Azure Batch                      |
| Monitoring & Alerts       | Azure Monitor + Application Insights               |
| CI/CD Automation          | Azure DevOps Pipelines / GitHub Actions            |
| Security & Secrets        | Azure Key Vault, Private Endpoints, RBAC           |

---

## 📏 Evaluation Metrics

### For Classification:
- Precision
- Recall
- F1-Score
- ROC-AUC

### For Anomaly Detection:
- Detection Rate
- Precision at N
- Latency

All metrics are logged using MLflow/Azure ML logging functions.

---

## 🔐 Security & Compliance

- Data anonymization (PII masking, IP hashing)
- Storage encryption (at rest and in transit)
- Access control via Azure RBAC and Private Endpoints
- Secrets managed via Azure Key Vault
- Logging and audit trail enabled for scoring and monitoring
