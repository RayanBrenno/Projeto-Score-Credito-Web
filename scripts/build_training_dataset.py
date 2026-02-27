import pandas as pd

ARQUIVO_ENTRADA = "data/clientes.csv"
ARQUIVO_SAIDA = "data/clientes_limpo.csv"
ID_COL = "id_cliente"

COLUNAS_REMOVER = [
    "emprestimo_carro",
    "emprestimo_casa",
    "emprestimo_pessoal",
    "emprestimo_credito",
    "emprestimo_estudantil",
    "mes"
]

# =========================
# 1) LER CSV
# =========================
df = pd.read_csv(ARQUIVO_ENTRADA, skipinitialspace=True)

# Remove espaços extras nos nomes das colunas
df.columns = df.columns.str.strip()

# =========================
# 2) REMOVER COLUNAS
# =========================
df = df.drop(columns=COLUNAS_REMOVER, errors="ignore")

unique_ids = df[ID_COL].unique()


def calculate_mean(series):
    return series.mean()


def most_frequent(series):
    mode = series.mode()
    return mode.iloc[0] if not mode.empty else None


numeric_cols = df.select_dtypes(include="number").columns.tolist()
text_cols = df.select_dtypes(include="object").columns.tolist()
numeric_cols.remove(ID_COL)

consolidated_rows = []

for client_id in unique_ids:
    client_rows = df[df[ID_COL] == client_id]
    consolidated_record = {"id_client": client_id}
    
    # Mean for numeric columns
    for col in numeric_cols:
        consolidated_record[col] = calculate_mean(client_rows[col]).round(3)

    # Most frequent for text columns
    for col in text_cols:
        consolidated_record[col] = most_frequent(client_rows[col]).strip()

    consolidated_rows.append(consolidated_record)

consolidated_df = pd.DataFrame(consolidated_rows)

# =========================
# 3) SALVAR NOVO CSV
# =========================
consolidated_df.to_csv(ARQUIVO_SAIDA, index=False)

print("\nCSV limpo salvo com sucesso!")