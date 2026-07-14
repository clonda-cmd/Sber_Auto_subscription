# predict.py
import catboost
import pandas as pd
import json
from config import Config
from preprocessing import preprocess_input

_model = None
_threshold = None


def load_model():
    global _model
    if _model is None:
        _model = catboost.CatBoostClassifier()
        _model.load_model(Config.MODEL_PATH)
    return _model


def load_threshold():
    global _threshold
    if _threshold is None:
        with open(Config.MODEL_CONFIG_PATH, "r") as f:
            _threshold = json.load(f)["threshold"]
    return _threshold


def predict_visit(input_data) -> dict:
    if isinstance(input_data, dict):
        df = pd.DataFrame([input_data])
    elif isinstance(input_data, pd.DataFrame):
        df = input_data.copy()
    elif isinstance(input_data, str):
        if input_data.endswith(".csv"):
            df = pd.read_csv(input_data)
        elif input_data.endswith(".pkl"):
            df = pd.read_pickle(input_data)
        else:
            raise ValueError("Only .csv or .pkl supported")
    else:
        raise TypeError("input_data must be dict, DataFrame or file path")

    df = preprocess_input(df)

    model = load_model()
    threshold = load_threshold()

    proba = model.predict_proba(df)[0, 1]
    pred = int(proba >= threshold)

    return {
        "prediction": pred,
        "probability": float(proba)
    }
