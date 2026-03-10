from fastapi import FastAPI
from datetime import datetime
import pandas as pd

from app.database import clientes_collection, analises_collection
from app.ml_model import predict_credit_score
from app.routes.clientes import router as clientes_router
from app.routes.analises import router as analises_router

app = FastAPI(
    title="API de Análise de Crédito",
    version="1.0.0"
)


app.include_router(clientes_router)
app.include_router(analises_router)


def teste_importacao_csv():
    clientes_collection.delete_many({})
    analises_collection.delete_many({})

    df = pd.read_csv("data/novos_clientes.csv")

    resultados = []

    for _, row in df.iterrows():
        cliente_data = {
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
            "saldo_final_mes": float(row["saldo_final_mes"]),
            "criado_em": datetime.utcnow()
        }

        result_cliente = clientes_collection.insert_one(cliente_data)
        cliente_id = str(result_cliente.inserted_id)

        dados_modelo = cliente_data.copy()
        dados_modelo.pop("criado_em", None)
        dados_modelo.pop("nome", None)

        score_credito = predict_credit_score(dados_modelo)

        analise_data = {
            "cliente_id": cliente_id,
            "score_credito": score_credito,
            "data_analise": datetime.utcnow()
        }

        result_analise = analises_collection.insert_one(analise_data)

        resultados.append({
            "nome": cliente_data["nome"],
            "cliente_id": cliente_id,
            "analise_id": str(result_analise.inserted_id),
            "score_credito": score_credito
        })

    print("\n=== RESULTADOS DA IMPORTAÇÃO ===")
    for item in resultados:
        print(item)

    return resultados


if __name__ == "__main__":
    teste_importacao_csv()

# {'nome': 'John', 'score_credito': 'Poor'}
# {'nome': 'Jane', 'score_credito': 'Standard'}
# {'nome': 'Bob', 'score_credito': 'Standard'}
# {'nome': 'Alice', 'score_credito': 'Good'}
# {'nome': 'Nazario', 'score_credito': 'Poor'}
# {'nome': 'Carlos', 'score_credito': 'Good'}
# {'nome': 'Maria', 'score_credito': 'Standard'}
# {'nome': 'Ana', 'score_credito': 'Good'}

# Cliente John: Poor
# Cliente Jane: Standard
# Cliente Bob: Standard
# Cliente Alice: Good
# Cliente Nazario: Poor
# Cliente Carlos: Good
# Cliente Maria: Standard
# Cliente Ana: Good