from dataclasses import Field
from datetime import datetime
from typing_extensions import Literal
from pydantic import BaseModel


class AnalisePredictRequest(BaseModel):
    nome: str
    idade: float
    profissao: str
    salario_anual: float
    num_contas: float
    num_cartoes: float
    juros_emprestimo: float
    num_emprestimos: float
    dias_atraso: float
    num_pagamentos_atrasados: float
    num_verificacoes_credito: float
    mix_credito: str
    divida_total: float
    taxa_uso_credito: float
    idade_historico_credito: float
    investimento_mensal: float
    comportamento_pagamento: str
    saldo_final_mes: float


class PredictRequest(BaseModel):
    nome: str
    idade: float
    profissao: str
    salario_anual: float
    num_contas: float
    num_cartoes: float
    juros_emprestimo: float
    num_emprestimos: float
    dias_atraso: float
    num_pagamentos_atrasados: float
    num_verificacoes_credito: float
    mix_credito: str
    divida_total: float
    taxa_uso_credito: float
    idade_historico_credito: float
    investimento_mensal: float
    comportamento_pagamento: str
    saldo_final_mes: float


class PredictResponse(BaseModel):
    score: int | None = None
    classe: str | None = None
    message: str | None = None


class AnaliseCreditoCreate(BaseModel):
    cliente_id: str


class AnaliseCreditoResponse(BaseModel):
    id: str
    cliente_id: str
    score_credito: Literal["Good", "Poor", "Standard"]
    data_analise: datetime