# score.py for Real-Time Online Endpoint

import os
import logging
import json
import mlflow
import pandas as pd

def init():
    global model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model')
    model = mlflow.pyfunc.load_model(model_path)
    logging.info("Model loaded successfully")

def run(data):
    try:
        # Assume input is JSON with "data" field: list of dicts
        df = pd.DataFrame(data.get("data", []))
        preds = model.predict(df)
        return {"predictions": preds.tolist()}
    except Exception as e:
        logging.error(f"Prediction error: {str(e)}")
        return {"error": str(e)}
