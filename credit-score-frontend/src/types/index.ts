export type CreditClass = "Good" | "Standard" | "Poor";

export interface PredictionResponse {
  classe?: CreditClass;
  message?: string;
}

export interface FormDataType {
  nome: string;
  idade: string;
  profissao: string;
  salario_anual: string;
  num_contas: string;
  num_cartoes: string;
  juros_emprestimo: string;
  num_emprestimos: string;
  dias_atraso: string;
  num_pagamentos_atrasados: string;
  num_verificacoes_credito: string;
  mix_credito: string;
  divida_total: string;
  taxa_uso_credito: string;
  idade_historico_credito: string;
  investimento_mensal: string;
  comportamento_pagamento: string;
  saldo_final_mes: string;
}
