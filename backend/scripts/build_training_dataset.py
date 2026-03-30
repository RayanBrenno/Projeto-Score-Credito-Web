import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_ENTRADA = BASE_DIR / "data" / "clientes.csv"
ARQUIVO_SAIDA = BASE_DIR / "data" / "clientes_limpo.csv"
ID_COL = "id_cliente"

COLUNAS_REMOVER = [
    "emprestimo_carro",
    "emprestimo_casa",
    "emprestimo_pessoal",
    "emprestimo_credito",
    "emprestimo_estudantil",
    "mes",
]


def calculate_mean(series: pd.Series):
    return series.mean()


def most_frequent(series: pd.Series):
    mode = series.mode(dropna=True)
    return mode.iloc[0] if not mode.empty else None


def main():
    if not ARQUIVO_ENTRADA.exists():
        raise FileNotFoundError(f"Arquivo de entrada não encontrado: {ARQUIVO_ENTRADA}")

    df = pd.read_csv(ARQUIVO_ENTRADA, skipinitialspace=True)

    df.columns = df.columns.str.strip()

    if ID_COL not in df.columns:
        raise ValueError(f"A coluna de ID '{ID_COL}' não foi encontrada no arquivo.")

    df = df.drop(columns=COLUNAS_REMOVER, errors="ignore")

    unique_ids = df[ID_COL].dropna().unique()

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    text_cols = df.select_dtypes(include=["object", "string"]).columns.tolist()

    if ID_COL in numeric_cols:
        numeric_cols.remove(ID_COL)

    if ID_COL in text_cols:
        text_cols.remove(ID_COL)

    consolidated_rows = []

    for client_id in unique_ids:
        client_rows = df[df[ID_COL] == client_id]
        consolidated_record = {ID_COL: client_id}

        # média para colunas numéricas
        for col in numeric_cols:
            value = calculate_mean(client_rows[col])
            consolidated_record[col] = round(float(value), 3) if pd.notna(value) else None

        # valor mais frequente para colunas textuais
        for col in text_cols:
            value = most_frequent(client_rows[col])
            if isinstance(value, str):
                value = value.strip()
            consolidated_record[col] = value

        consolidated_rows.append(consolidated_record)

    consolidated_df = pd.DataFrame(consolidated_rows)

    ARQUIVO_SAIDA.parent.mkdir(parents=True, exist_ok=True)
    consolidated_df.to_csv(ARQUIVO_SAIDA, index=False)

    print(f"✅ CSV limpo salvo com sucesso em: {ARQUIVO_SAIDA}")
    print(f"📊 Total de clientes consolidados: {len(consolidated_df)}")


if __name__ == "__main__":
    main()