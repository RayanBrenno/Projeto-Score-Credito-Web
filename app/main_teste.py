from fastapi.testclient import TestClient
import pandas as pd

from app.main import app
from app.database import clientes_collection, analises_collection

client = TestClient(app)


def testar_rotas_com_csv():
    clientes_collection.delete_many({})
    analises_collection.delete_many({})

    df = pd.read_csv("data/novos_clientes.csv", skipinitialspace=True)
    df.columns = df.columns.str.strip()

    for c in df.columns:
        if df[c].dtype == "object":
            df[c] = df[c].astype(str).str.strip()

    resultados = []

    for _, row in df.iterrows():
        payload_cliente = {
            "nome": str(row["nome"]) if "nome" in df.columns else "Sem nome",
            "idade": int(row["idade"]),
            "profissao": str(row["profissao"]),
            "salario_anual": float(row["salario_anual"]),
            "num_contas": int(row["num_contas"]),
            "num_cartoes": int(row["num_cartoes"]),
            "juros_emprestimo": float(row["juros_emprestimo"]),
            "num_emprestimos": int(row["num_emprestimos"]),
            "dias_atraso": int(row["dias_atraso"]),
            "num_pagamentos_atrasados": int(row["num_pagamentos_atrasados"]),
            "num_verificacoes_credito": int(row["num_verificacoes_credito"]),
            "mix_credito": str(row["mix_credito"]),
            "divida_total": float(row["divida_total"]),
            "taxa_uso_credito": float(row["taxa_uso_credito"]),
            "idade_historico_credito": float(row["idade_historico_credito"]),
            "investimento_mensal": float(row["investimento_mensal"]),
            "comportamento_pagamento": str(row["comportamento_pagamento"]),
            "saldo_final_mes": float(row["saldo_final_mes"])
        }

        resposta_cliente = client.post("/clientes/", json=payload_cliente)

        cliente_criado = resposta_cliente.json()
        cliente_id = cliente_criado["id"]

        resposta_analise = client.post("/analises/", json={"cliente_id": cliente_id})

        analise_criada = resposta_analise.json()

        resultados.append({
            "nome": cliente_criado["nome"],
            "cliente_id": cliente_id,
            "analise_id": analise_criada["id"],
            "score_credito": analise_criada["score_credito"]
        })

    print("\n=== RESULTADOS DO TESTE VIA ROTAS ===")
    for item in resultados:
        print(f"Cliente {item['nome']}: {item['score_credito']}")


if __name__ == "__main__":
    testar_rotas_com_csv()