import pandas as pd

CAMINHO_CSV = "data/clientes.csv"   

df = pd.read_csv(CAMINHO_CSV, skipinitialspace=True)
df.columns = df.columns.str.strip()

categorias = {}  # dict[str, dict[str, int]]

for col in df.columns:
    serie = df[col].astype(str).str.strip()

    tem_letra = serie.str.contains(r"[A-Za-zÀ-ÿ_]", regex=True, na=False).any()

    if tem_letra:
        categorias[col] = {}

        for v in serie:
            if v and v.lower() not in ("nan", "none"):

                if v not in categorias[col]:
                    categorias[col][v] = 1
                else:
                    categorias[col][v] += 1


# PRINT
for col, valores in categorias.items():
    aux = 0 
    print(f"\n=== {col} ===")
    for categoria, qtd in sorted(valores.items(), key=lambda x: x[1], reverse=True):
        aux += qtd
        print(f"{categoria} -> {qtd}")
    print(f"Total: {aux}")

