import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

COL_ALVO = "score_credito"
COL_ID = "id_cliente"
RANDOM_STATE = 1

# =========================
# 1) LER E LIMPAR BASE
# =========================
df = pd.read_csv("clientes.csv", skipinitialspace=True)
df.columns = df.columns.str.strip()

for c in df.columns:
    if df[c].dtype == "object" or str(df[c].dtype).startswith("string"):
        df[c] = df[c].astype(str).str.strip()


# =========================
# 2) SEPARAR X / Y
# =========================
drop_cols = [COL_ALVO]
if COL_ID in df.columns:
    drop_cols.append(COL_ID)

X = df.drop(columns=drop_cols).copy()
y = df[COL_ALVO].astype(str).str.strip()

# =========================
# 3) CONVERTER NUMÉRICAS QUANDO FIZER SENTIDO
# =========================
for c in X.columns:
    conv = pd.to_numeric(X[c], errors="coerce")
    if conv.notna().mean() >= 0.70:
        X[c] = conv
    else:
        X[c] = X[c].astype(str).str.strip()

# =========================
# 4) ENCODING + NaN
# =========================
encoders = {}

for c in X.columns:
    if pd.api.types.is_numeric_dtype(X[c]):
        if X[c].isna().any():
            X[c] = X[c].fillna(X[c].median())
    else:
        le = LabelEncoder()
        serie = X[c].astype(str).str.strip().fillna("DESCONHECIDO")
        X[c] = le.fit_transform(serie)
        le.classes_ = np.array(le.classes_, dtype=str)
        encoders[c] = le

# =========================
# 5) TREINO / TESTE
# =========================
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
)

modelo = RandomForestClassifier(
    n_estimators=300,
    random_state=RANDOM_STATE,
    n_jobs=-1
)

modelo.fit(X_tr, y_tr)

pred = modelo.predict(X_te)
acc = accuracy_score(y_te, pred)
print("Accuracy RandomForest:", acc)

# =========================
# 6) PREVER NOVOS CLIENTES
# =========================
novos = pd.read_csv("novos_clientes.csv", skipinitialspace=True)
novos.columns = novos.columns.str.strip()

for c in novos.columns:
    if novos[c].dtype == "object" or str(novos[c].dtype).startswith("string"):
        novos[c] = novos[c].astype(str).str.strip()

if COL_ID in novos.columns:
    novos = novos.drop(columns=[COL_ID])

# garante mesmas colunas do treino
novos = novos.reindex(columns=X.columns, fill_value=np.nan)

for c in novos.columns:
    if pd.api.types.is_numeric_dtype(X[c]):
        novos[c] = pd.to_numeric(novos[c], errors="coerce")
        if novos[c].isna().any():
            novos[c] = novos[c].fillna(X[c].median())
    else:
        le = encoders[c]
        serie = novos[c].astype(str).str.strip().fillna("DESCONHECIDO")

        classes_treino = set(le.classes_.tolist())
        serie = serie.apply(lambda v: v if v in classes_treino else "DESCONHECIDO")

        if "DESCONHECIDO" not in classes_treino:
            le.classes_ = np.array(list(le.classes_) + ["DESCONHECIDO"], dtype=str)

        novos[c] = le.transform(np.array(serie, dtype=str))

previsoes = modelo.predict(novos)
print("Previsões novos clientes:", previsoes)