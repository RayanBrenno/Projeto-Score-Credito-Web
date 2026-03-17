import datetime
from pydantic import BaseModel, Field


class ClienteCreate(BaseModel):
    nome: str
    idade: int = Field(..., ge=0)
    profissao: str
    salario_anual: float
    num_contas: int = Field(..., ge=0)
    num_cartoes: int = Field(..., ge=0)
    juros_emprestimo: float
    num_emprestimos: int = Field(..., ge=0)
    dias_atraso: int = Field(..., ge=0)
    num_pagamentos_atrasados: int = Field(..., ge=0)
    num_verificacoes_credito: int = Field(..., ge=0)
    mix_credito: str
    divida_total: float
    taxa_uso_credito: float
    idade_historico_credito: float
    investimento_mensal: float
    comportamento_pagamento: str
    saldo_final_mes: float


class ClienteResponse(ClienteCreate):
    id: str
    criado_em: datetime