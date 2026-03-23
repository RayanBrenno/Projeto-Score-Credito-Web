from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.database import analises_collection
from app.ml_model import predict_credit_score
from app.schemas.analise import AnalisePredictRequest

router = APIRouter(prefix="/analises", tags=["Análises de Crédito"])


#  using
@router.post("/predict")
def prever_direto(dados: AnalisePredictRequest):
    dados_dict = dados.dict()

    dados_modelo = dict(dados_dict)
    dados_modelo.pop("nome", None)

    try:
        score_credito = predict_credit_score(dados_modelo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao prever score: {str(e)}")

    nova_analise = {
        "nome": dados_dict.get("nome"),
        "dados_formulario": dados_dict,
        "score_credito": score_credito,
        "data_analise": datetime.utcnow()
    }

    result = analises_collection.insert_one(nova_analise)
    analise_salva = analises_collection.find_one({"_id": result.inserted_id})

    return {
        "id": str(analise_salva["_id"]),
        "classe": score_credito,
        "message": "Análise realizada e salva com sucesso"
    }