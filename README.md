# Cyber Intrusion Detection - Azure MLOps Pipeline

This project focuses on building an end-to-end MLOps pipeline for detecting cybersecurity intrusions using Azure Machine Learning. 

## Project Highlights

- Full MLOps pipeline (data ingestion, model training, deployment)
- Batch inference using Azure Batch Endpoints
- MLflow model packaging
- Environment tracking using conda environments
- Data output for batch scoring

## Folder Structure

- `code/`: Batch drivers and scoring scripts
- `cyber_intrusion_model_/`: Saved MLflow model and dependencies
- `environment/`: Conda environment files
- `named-outputs/`: Batch scoring outputs
- `data_exploration.ipynb`: Data analysis and exploration
- `mlflow-for-batch-tabular.ipynb`: Batch deployment and inference pipeline

## Dataset

The dataset used simulates cybersecurity intrusion patterns based on network session data.

## How to Reproduce

1. Configure Azure ML Workspace
2. Upload the model to Azure ML
3. Create a batch endpoint
4. Deploy and trigger batch scoring jobs
5. Monitor outputs and logs

---
