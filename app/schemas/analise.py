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