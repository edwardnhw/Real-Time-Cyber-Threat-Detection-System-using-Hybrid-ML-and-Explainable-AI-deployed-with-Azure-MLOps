import mlflow
import pandas as pd
import os

# Load MLflow model
model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model")
model = mlflow.pyfunc.load_model(model_path)

def run(mini_batch: pd.DataFrame) -> pd.DataFrame:
    # Run inference
    predictions = model.predict(mini_batch)
    
    # Return predictions in DataFrame format
    result = mini_batch.copy()
    result["prediction"] = predictions
    return result
