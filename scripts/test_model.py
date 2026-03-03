import numpy as np
import pandas as pd
import joblib


COL_ID = "id_cliente"

# =========================
# CARREGAR MODELO SALVO
# =========================
data = joblib.load("models/modelo_score_credito_clientes_limpo.joblib")

modelo = data["model"]
encoders = data["encoders"]
numeric_medians = data["numeric_medians"]
columns = data["columns"]

# =========================
# LER NOVOS CLIENTES
# =========================
novos = pd.read_csv("data/novos_clientes.csv", skipinitialspace=True)
novos.columns = novos.columns.str.strip()

for c in novos.columns:
    if novos[c].dtype == "object":
        novos[c] = novos[c].astype(str).str.strip()

if COL_ID in novos.columns:
    novos = novos.drop(columns=[COL_ID])

# Garante mesmas colunas do treino
novos = novos.reindex(columns=columns, fill_value=np.nan)

# =========================
# APLICAR MESMA TRANSFORMAÇÃO DO TREINO
# =========================
for c in novos.columns:
    if c in numeric_medians:
        novos[c] = pd.to_numeric(novos[c], errors="coerce")
        novos[c] = novos[c].fillna(numeric_medians[c])
    else:
        le = encoders[c]
        serie = novos[c].fillna("DESCONHECIDO").astype(str)

        serie = serie.apply(
            lambda v: v if v in le.classes_ else "DESCONHECIDO"
        )

        novos[c] = le.transform(serie)

# =========================
# PREVISÃO
# =========================
previsoes = modelo.predict(novos)

print("Previsões novos clientes:")
print(previsoes)

# =========================
# IMPORTÂNCIA DAS FEATURES
# =========================

importancias = modelo.feature_importances_

df_importancias = pd.DataFrame({
    "feature": columns,
    "importance": importancias
})

df_importancias["percentual_%"] = (
    df_importancias["importance"] / df_importancias["importance"].sum()
) * 100

df_importancias = df_importancias.sort_values(
    by="percentual_%", ascending=False
)

print("\nImportância das Features:")
print(df_importancias)

# =========================
# PROBABILIDADE POR CLASSE
# =========================
probs = modelo.predict_proba(novos)

df_probs = pd.DataFrame(
    probs,
    columns=modelo.classes_
)

print("\nProbabilidade por classe:")
print(df_probs)