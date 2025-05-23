
import os
import glob
import mlflow
import pandas as pd


def init():
    global model
    global model_input_types
    global model_output_names

    # AZUREML_MODEL_DIR is an environment variable created during deployment
    # It is the path to the model folder
    # Please provide your model's folder name if there's one
    model_path = glob.glob(os.environ["AZUREML_MODEL_DIR"] + "/*/")[0]

    # Load the model, it's input types and output names
    model = mlflow.pyfunc.load(model_path)
    if model.metadata.signature.inputs:
        model_input_types = dict(
            zip(
                model.metadata.signature.inputs.input_names(),
                model.metadata.signature.inputs.pandas_types(),
            )
        )
    if model.metadata.signature.outputs:
        if model.metadata.signature.outputs.has_input_names():
            model_output_names = model.metadata.signature.outputs.input_names()
        elif len(model.metadata.signature.outputs.input_names()) == 1:
            model_output_names = ["prediction"]


def run(mini_batch):
    print(f"run method start: {__file__}, run({len(mini_batch)} files)")

    data = pd.concat(
        map(
            lambda fp: pd.read_csv(fp).assign(filename=os.path.basename(fp)), mini_batch
        )
    )
    if model_input_types:
        data = data.astype(model_input_types)

    pred = model.predict(data)

    if pred is not pd.DataFrame:
        if not model_output_names:
            model_output_names = ["pred_col" + str(i) for i in range(pred.shape[1])]
        pred = pd.DataFrame(pred, columns=model_output_names)

    return pd.concat([data, pred], axis=1)
