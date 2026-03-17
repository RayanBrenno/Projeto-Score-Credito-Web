from datetime import datetime
from bson import ObjectId
from fastapi import APIRouter, HTTPException
from app.database import clientes_collection, analises_collection
from app.ml_model import predict_credit_score
from app.utils import serialize_mongo_doc, is_valid_object_id
from app.schemas.analise import AnalisePredictRequest, AnaliseCreditoCreate

router = APIRouter(prefix="/analises", tags=["Análises de Crédito"])


@router.post("/")
def criar_analise(dados: AnaliseCreditoCreate):
    if not is_valid_object_id(dados.cliente_id):
        raise HTTPException(status_code=400, detail="cliente_id inválido")

    cliente = clientes_collection.find_one({"_id": ObjectId(dados.cliente_id)})
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    cliente_para_modelo = dict(cliente)
    cliente_para_modelo.pop("_id", None)
    cliente_para_modelo.pop("criado_em", None)
    cliente_para_modelo.pop("nome", None)

    try:
        score_credito = predict_credit_score(cliente_para_modelo)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao prever score: {str(e)}")

    nova_analise = {
        "cliente_id": dados.cliente_id,
        "score_credito": score_credito,
        "data_analise": datetime.utcnow()
    }

    result = analises_collection.insert_one(nova_analise)
    analise_salva = analises_collection.find_one({"_id": result.inserted_id})

    return serialize_mongo_doc(analise_salva)


@router.get("/")
def listar_analises():
    analises = list(analises_collection.find().sort("data_analise", -1))
    return [serialize_mongo_doc(analise) for analise in analises]


@router.get("/{analise_id}")
def buscar_analise(analise_id: str):
    if not is_valid_object_id(analise_id):
        raise HTTPException(status_code=400, detail="ID inválido")

    analise = analises_collection.find_one({"_id": ObjectId(analise_id)})
    if not analise:
        raise HTTPException(status_code=404, detail="Análise não encontrada")

    return serialize_mongo_doc(analise)

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