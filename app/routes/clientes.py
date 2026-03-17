from datetime import datetime
from bson import ObjectId
from fastapi import APIRouter, HTTPException
from app.database import clientes_collection
from app.utils import serialize_mongo_doc, is_valid_object_id
from app.schemas.cliente import ClienteCreate

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.post("/")
def criar_cliente(dados: ClienteCreate):
    novo_cliente = {
        **dados.model_dump(),
        "criado_em": datetime.utcnow()
    }

    result = clientes_collection.insert_one(novo_cliente)
    cliente_salvo = clientes_collection.find_one({"_id": result.inserted_id})

    return serialize_mongo_doc(cliente_salvo)


@router.get("/")
def listar_clientes():
    clientes = list(clientes_collection.find().sort("criado_em", -1))
    return [serialize_mongo_doc(cliente) for cliente in clientes]


@router.get("/{cliente_id}")
def buscar_cliente(cliente_id: str):
    if not is_valid_object_id(cliente_id):
        raise HTTPException(status_code=400, detail="ID inválido")

    cliente = clientes_collection.find_one({"_id": ObjectId(cliente_id)})
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return serialize_mongo_doc(cliente)
