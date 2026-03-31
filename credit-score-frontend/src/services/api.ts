import axios from "axios";
import type { FormDataType, PredictionResponse } from "../types";

// const API_URL = "http://localhost:8000"
const API_URL = import.meta.env.VITE_API_URL;

// Função auxiliar para converter strings numéricas com formatação brasileira (ex: "1.234,56") para números do JavaScript (ex: 1234.56)
function toNumber(value: string): number {
  if (!value) return 0;
  return Number(String(value).replace(/\./g, "").replace(",", "."));
}

// Objeto de API para lidar com as chamadas ao backend, incluindo a função de previsão que envia os dados do formulário para o endpoint de previsão e retorna a resposta do modelo
export const api = {
  async predict(form: FormDataType): Promise<PredictionResponse> {
    const payload = {
      nome: form.nome,
      idade: toNumber(form.idade),
      profissao: form.profissao,
      salario_anual: toNumber(form.salario_anual),
      num_contas: toNumber(form.num_contas),
      num_cartoes: toNumber(form.num_cartoes),
      juros_emprestimo: toNumber(form.juros_emprestimo),
      num_emprestimos: toNumber(form.num_emprestimos),
      dias_atraso: toNumber(form.dias_atraso),
      num_pagamentos_atrasados: toNumber(form.num_pagamentos_atrasados),
      num_verificacoes_credito: toNumber(form.num_verificacoes_credito),
      mix_credito: form.mix_credito,
      divida_total: toNumber(form.divida_total),
      taxa_uso_credito: toNumber(form.taxa_uso_credito),
      idade_historico_credito: toNumber(form.idade_historico_credito),
      investimento_mensal: toNumber(form.investimento_mensal),
      comportamento_pagamento: form.comportamento_pagamento,
      saldo_final_mes: toNumber(form.saldo_final_mes),
    };

    const response = await axios.post<PredictionResponse>(
      `${API_URL}/analises/predict`,
      payload
    );

    return response.data;
  },
};
