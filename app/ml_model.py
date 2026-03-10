import os
import joblib
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH")
_model_bundle = None


def load_model():
    global _model_bundle
    if _model_bundle is None:
        _model_bundle = joblib.load(MODEL_PATH)
    return _model_bundle


def preprocess_input(data: dict) -> pd.DataFrame:
    bundle = load_model()

    encoders = bundle.get("encoders", {})
    numeric_medians = bundle.get("numeric_medians", {})
    training_columns = bundle.get("columns", [])

    df = pd.DataFrame([data])

    for col, median in numeric_medians.items():
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df[col] = df[col].fillna(median)

    for col, encoder in encoders.items():
        if col not in df.columns:
            df[col] = "DESCONHECIDO"

        df[col] = df[col].astype(str)
        classes = set(encoder.classes_)
        fallback = "DESCONHECIDO" if "DESCONHECIDO" in classes else list(classes)[0]
        df[col] = df[col].apply(lambda x: x if x in classes else fallback)
        df[col] = encoder.transform(df[col])

    df = df.reindex(columns=training_columns, fill_value=0)
    return df


def predict_credit_score(data: dict) -> str:
    bundle = load_model()
    model = bundle["model"]

    df = preprocess_input(data)
    prediction = model.predict(df)[0]

    return str(prediction)