import { useState } from "react";
import { TrendingUp, AlertCircle } from "lucide-react";
import CreditForm from "./components/CreditForm";
import ResultModal from "./components/ResultModal";
import type { PredictionResponse, FormDataType } from "./types";
import { api } from "./services/api";

const INITIAL_FORM: FormDataType = {
  nome: "",
  idade: "",
  profissao: "advogado",
  salario_anual: "",
  num_contas: "",
  num_cartoes: "",
  juros_emprestimo: "",
  num_emprestimos: "",
  dias_atraso: "",
  num_pagamentos_atrasados: "",
  num_verificacoes_credito: "",
  mix_credito: "Normal",
  divida_total: "",
  taxa_uso_credito: "",
  idade_historico_credito: "",
  investimento_mensal: "",
  comportamento_pagamento: "baixo_gasto_pagamento_medio",
  saldo_final_mes: "",
};

export default function App() {
  const [form, setForm] = useState<FormDataType>(INITIAL_FORM);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<PredictionResponse | null>(null);
  const [showResult, setShowResult] = useState(false);
  const [error, setError] = useState("");

  function handleChange(field: keyof FormDataType, value: string) {
    setForm((prev) => ({
      ...prev,
      [field]: value,
    }));
  }

  async function handleAnalyze() {
    if (!form.nome) {
      setError("Por favor, preencha o nome do cliente");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const data = await api.predict(form);
      setResult(data);
      setShowResult(true);
    } catch (err: any) {
      const message =
        err?.response?.data?.detail ||
        err?.response?.data?.message ||
        "Erro ao realizar análise de crédito. Tente novamente.";
      setError(message);
    } finally {
      setLoading(false);
    }
  }

  function handleReset() {
    setForm(INITIAL_FORM);
    setResult(null);
    setShowResult(false);
    setError("");
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-0 right-0 w-96 h-96 bg-blue-500 opacity-10 blur-3xl rounded-full"></div>
        <div className="absolute bottom-0 left-0 w-96 h-96 bg-slate-500 opacity-10 blur-3xl rounded-full"></div>
      </div>

      <div className="relative min-h-screen flex flex-col">
        <header className="border-b border-slate-700/50 backdrop-blur-sm bg-slate-800/30">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
            <div className="flex items-center gap-3">
              <div className="p-2 bg-blue-500/20 rounded-lg">
                <TrendingUp className="w-6 h-6 text-blue-400" />
              </div>
              <div>
                <h1 className="text-3xl font-bold text-white">Análise de Score de Crédito</h1>
                <p className="text-slate-400 text-sm mt-1">
                  Avaliação inteligente de perfil de crédito do cliente
                </p>
              </div>
            </div>
          </div>
        </header>

        <main className="flex-1 py-8 px-4">
          <div className="max-w-4xl mx-auto">
            {error && (
              <div className="mb-6 p-4 bg-red-500/10 border border-red-500/30 rounded-lg flex items-start gap-3">
                <AlertCircle className="w-5 h-5 text-red-400 flex-shrink-0 mt-0.5" />
                <p className="text-red-300">{error}</p>
              </div>
            )}

            <CreditForm
              form={form}
              onChange={handleChange}
              onAnalyze={handleAnalyze}
              onReset={handleReset}
              loading={loading}
            />
          </div>
        </main>

        <footer className="border-t border-slate-700/50 backdrop-blur-sm bg-slate-800/30">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <p className="text-slate-400 text-sm text-center">
              Sistema de Análise de Crédito © 2026 - Processamento seguro e confidencial
            </p>
          </div>
        </footer>
      </div>
      
    </div>
  );
}