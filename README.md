# Real-Time Cyber Threat Detection System using Hybrid ML and Explainable AI deployed with Azure MLOps

**Author**: Hon Wa Ng  
**Date**: April 2025

## Overview

This project builds a real-time Cyber Threat Detection System by leveraging Azure Machine Learning's MLOps capabilities, AutoML pipelines, and Explainable AI (XAI) techniques.

The solution covers the full lifecycle:
- Data ingestion and preprocessing
- Automated model training using Azure AutoML
- Model registration and versioning
- Batch scoring and endpoint deployment via Azure SDK and Azure ML Designer
- Model evaluation and operational metric analysis

---

## Objectives

- Build an intelligent cyber intrusion detection system combining supervised classification with explainability.
- Automate the end-to-end machine learning workflow using Azure MLOps tools (SDK & GUI).
- Register and manage models for production readiness with version control.
- Deploy batch endpoints for large-scale inference on unseen network session data.
- Evaluate model performance (accuracy, F1-score, AUC) and validate reproducibility principles.

---

## Repository Structure
```bash
real-time-cyber-threat-detection-system-azure-mlops/
│── notebooks/                         # Final deliverables
│   ├── data_exploration.ipynb          # Data exploration and preprocessing
│   ├── mlflow-for-batch-tabular.ipynb  # MLflow batch deployment and inference pipelines
│
│── assets/                            # Supporting files
│   ├── cybersecurity_intrusion_data.csv   # Sample intrusion detection dataset
│   ├── evaluation_results.png             # Model evaluation results
│
│── for-assignment-turnins/              # Presentation PDF, assignment deliverables
│
│── LICENSE                              # License information
│── README.md                            # Project overview and usage guide
```
---
---

## Installation & Usage

### 1. Clone the Repository
```
git clone https://github.com/edwardnhw/Real-Time-Cyber-Threat-Detection-System-using-Hybrid-ML-and-Explainable-AI-deployed-with-Azure-MLOps.git
cd Real-Time-Cyber-Threat-Detection-System-using-Hybrid-ML-and-Explainable-AI-deployed-with-Azure-MLOps

```
Ensure you have Python 3.9+ installed with the following major packages:
- pandas
- scikit-learn
- mlflow
- matplotlib

### 2. Explore and preprocess the dataset:


```
Run notebooks/data_exploration.ipynb

```
Load the pretrained MLflow model and evaluate:

```
Run notebooks/mlflow-for-batch-tabular.ipynb

```



---
## How to Run the Project
- Perform dataset exploration, feature engineering, and scaling.
- Train baseline models if needed inside Kaggle (Logistic Regression / Random Forest).
- Load pretrained Azure MLflow models when available.
- Evaluate model using accuracy, F1-score, ROC AUC metrics.
- Refer to GitHub for Azure batch endpoint deployment scripts and workflows.
---
## Methods Used

1. Machine Learning Operations (MLOps)
- Azure ML SDK (Python) and Azure ML Studio (Designer GUI).
- AutoML classification experiments for optimal model discovery.
- Batch inference endpoint deployment.

2. Explainability
- Model transparency for cybersecurity risk assessments.
- Potential extensions to SHAP or LIME explainability.

3. Data Preprocessing
- One-hot encoding of categorical variables.
- Min-Max scaling of numerical features.

4. Model Evaluation
- scikit-learn metrics (Accuracy, F1 Score, ROC AUC).
- Confusion matrix, classification reports for performance analysis.

---

## Results & Analysis

- Achieved 89.36% Accuracy, 88.57% AUC Macro, and 89.11% Weighted F1-score using Azure AutoML pipelines.
- Successfully registered MLflow models and deployed batch endpoints for scalable intrusion detection.
- Confirmed model performance using standard evaluation metrics.
- Established operational workflows suitable for real-world cybersecurity monitoring applications.

---
## License
This project is licensed under the MIT License.
