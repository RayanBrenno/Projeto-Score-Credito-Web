import numpy as np
import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

COL_ALVO = "score_credito"
COL_ID = "id_cliente"
RANDOM_STATE = 1

BASE_DIR = Path(__file__).resolve().parent.parent
TRAIN_CSV = BASE_DIR / "data" / "clientes_limpo.csv"
OUT_MODEL = BASE_DIR / "models" / "modelo_score_credito.joblib"


def main():
    if not TRAIN_CSV.exists():
        raise FileNotFoundError(f"Arquivo de treino não encontrado: {TRAIN_CSV}")

    df = pd.read_csv(TRAIN_CSV, skipinitialspace=True)
    df.columns = df.columns.str.strip()

    if COL_ALVO not in df.columns:
        raise ValueError(f"A coluna alvo '{COL_ALVO}' não foi encontrada no arquivo.")

    for c in df.columns:
        if df[c].dtype == "object" or str(df[c].dtype).startswith("string"):
            df[c] = df[c].fillna("DESCONHECIDO").astype(str).str.strip()

    drop_cols = [COL_ALVO]
    if COL_ID in df.columns:
        drop_cols.append(COL_ID)

    X = df.drop(columns=drop_cols).copy()
    y = df[COL_ALVO].fillna("DESCONHECIDO").astype(str).str.strip()

    for c in X.columns:
        conv = pd.to_numeric(X[c], errors="coerce")
        if conv.notna().mean() >= 0.70:
            X[c] = conv
        else:
            X[c] = X[c].fillna("DESCONHECIDO").astype(str).str.strip()

    encoders = {}
    numeric_medians = {}

    for c in X.columns:
        if pd.api.types.is_numeric_dtype(X[c]):
            med = float(X[c].median()) if X[c].notna().any() else 0.0
            numeric_medians[c] = med
            X[c] = X[c].fillna(med)
        else:
            serie = X[c].fillna("DESCONHECIDO").astype(str).str.strip()
            le = LabelEncoder()
            X[c] = le.fit_transform(serie)
            le.classes_ = np.array(le.classes_, dtype=str)
            encoders[c] = le

    x_train, x_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    modelo = RandomForestClassifier(
        n_estimators=500,
        random_state=RANDOM_STATE,
        n_jobs=-1,
    )

    modelo.fit(x_train, y_train)

    pred = modelo.predict(x_test)
    acc = accuracy_score(y_test, pred)

    OUT_MODEL.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(
        {
            "model": modelo,
            "encoders": encoders,
            "numeric_medians": numeric_medians,
            "columns": list(X.columns),
            "meta": {
                "COL_ALVO": COL_ALVO,
                "COL_ID": COL_ID,
                "RANDOM_STATE": RANDOM_STATE,
                "accuracy_holdout": float(acc),
            },
        },
        OUT_MODEL,
    )

    print(f"✅ Modelo salvo em: {OUT_MODEL}")
    print(f"📊 Accuracy RandomForest: {acc:.4f}")


if __name__ == "__main__":
    main()