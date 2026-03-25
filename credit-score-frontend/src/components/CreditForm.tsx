import type { FormDataType } from "../types";
import FormSection from "./FormSection";
import FormField from "./FormField";
import FormSelect from "./FormSelect";
import { Loader2 } from "lucide-react";

interface CreditFormProps {
  form: FormDataType;
  onChange: (field: keyof FormDataType, value: string) => void;
  onAnalyze: () => void;
  onReset: () => void;
  loading: boolean;
}

const MIX_OPTIONS = ["Ruim", "Normal", "Bom"];
const PAYMENT_OPTIONS = [
  { value: "baixo_gasto_pagamento_baixo", label: "Baixo Gasto - Pagamento Baixo" },
  { value: "baixo_gasto_pagamento_medio", label: "Baixo Gasto - Pagamento Médio" },
  { value: "baixo_gasto_pagamento_alto", label: "Baixo Gasto - Pagamento Alto" },
  { value: "alto_gasto_pagamento_baixo", label: "Alto Gasto - Pagamento Baixo" },
  { value: "alto_gasto_pagamento_medio", label: "Alto Gasto - Pagamento Médio" },
  { value: "alto_gasto_pagamento_alto", label: "Alto Gasto - Pagamento Alto" },
];
const JOB_OPTIONS = [
  { value: "advogado", label: "Advogado" },
  { value: "arquiteto", label: "Arquiteto" },
  { value: "cientista", label: "Cientista" },
  { value: "contador", label: "Contador" },
  { value: "desenvolvedor", label: "Desenvolvedor" },
  { value: "empresario", label: "Empresário" },
  { value: "engenheiro", label: "Engenheiro" },
  { value: "escritor", label: "Escritor" },
  { value: "gerente", label: "Gerente" },
  { value: "gerente_midia", label: "Gerente de Mídia" },
  { value: "jornalista", label: "Jornalista" },
  { value: "mecanico", label: "Mecânico" },
  { value: "medico", label: "Médico" },
  { value: "musico", label: "Músico" },
  { value: "professor", label: "Professor" }
];

// Componente principal do formulário de análise de crédito, dividido em seções para organizar os campos de entrada, com botões para analisar e limpar o formulário, e um estado de carregamento para indicar quando a análise está em andamento
export default function CreditForm({
  form,
  onChange,
  onAnalyze,
  onReset,
  loading,
}: CreditFormProps) {
  return (
    <div className="bg-slate-800/50 backdrop-blur border border-slate-700/50 rounded-2xl p-8">

      {/* Seção de informações pessoais, com campos para nome, idade, profissão e salário anual, permitindo ao usuário fornecer dados básicos sobre si mesmo que são relevantes para a análise de crédito */}
      <FormSection title="Informações Pessoais" subtitle="Dados básicos do cliente">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <FormField
            label="Nome"
            value={form.nome}
            onChange={(value) => onChange("nome", value)}
            placeholder="João da Silva"
            fullWidth={false}
          />
          <FormField
            label="Idade"
            type="number"
            value={form.idade}
            onChange={(value) => onChange("idade", value)}
            placeholder="30"
          />
          <FormSelect
            label="Profissão"
            value={form.profissao}
            onChange={(value) => onChange("profissao", value)}
            options={JOB_OPTIONS}
          />
          <FormField
            label="Salário Anual (R$)"
            type="number"
            value={form.salario_anual}
            onChange={(value) => onChange("salario_anual", value)}
            placeholder="60000"
          />
        </div>
      </FormSection>

      {/* Seção de contas e cartões, com campos para número de contas bancárias e número de cartões de crédito */}
      <FormSection title="Contas e Cartões" subtitle="Informações sobre contas bancárias">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <FormField
            label="Número de Contas"
            type="number"
            value={form.num_contas}
            onChange={(value) => onChange("num_contas", value)}
            placeholder="2"
          />
          <FormField
            label="Número de Cartões"
            type="number"
            value={form.num_cartoes}
            onChange={(value) => onChange("num_cartoes", value)}
            placeholder="3"
          />
        </div>
      </FormSection>

      {/* Seção de empréstimos, com campos para juros do empréstimo e número de empréstimos, permitindo ao usuário inserir informações sobre suas dívidas e obrigações financeiras */}
      <FormSection title="Empréstimos" subtitle="Dados sobre empréstimos e juros">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <FormField
            label="Juros do Empréstimo (%)"
            type="number"
            step="0.01"
            value={form.juros_emprestimo}
            onChange={(value) => onChange("juros_emprestimo", value)}
            placeholder="5.5"
          />
          <FormField
            label="Número de Empréstimos"
            type="number"
            value={form.num_emprestimos}
            onChange={(value) => onChange("num_emprestimos", value)}
            placeholder="1"
          />
        </div>
      </FormSection>

      {/* Seção de histórico de pagamentos, com campos para dias de atraso, número de pagamentos atrasados e número de verificações de crédito, permitindo ao usuário fornecer informações sobre seu comportamento de pagamento e histórico financeiro */}
      <FormSection title="Histórico de Pagamentos" subtitle="Informações sobre atrasos e verificações">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <FormField
            label="Dias de Atraso"
            type="number"
            value={form.dias_atraso}
            onChange={(value) => onChange("dias_atraso", value)}
            placeholder="0"
          />
          <FormField
            label="Número de Pagamentos Atrasados"
            type="number"
            value={form.num_pagamentos_atrasados}
            onChange={(value) => onChange("num_pagamentos_atrasados", value)}
            placeholder="0"
          />
          <FormField
            label="Número de Verificações de Crédito"
            type="number"
            value={form.num_verificacoes_credito}
            onChange={(value) => onChange("num_verificacoes_credito", value)}
            placeholder="2"
          />
        </div>
      </FormSection>

      {/* Seção de perfil de crédito, com campos para mix de crédito, dívida total, taxa de uso de crédito e idade do histórico de crédito, permitindo ao usuário fornecer informações sobre sua situação financeira atual e uso de crédito */}
      <FormSection title="Perfil de Crédito" subtitle="Análise de dívida e uso de crédito">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <FormSelect
            label="Mix de Crédito"
            value={form.mix_credito}
            onChange={(value) => onChange("mix_credito", value)}
            options={MIX_OPTIONS}
          />
          <FormField
            label="Dívida Total (R$)"
            type="number"
            value={form.divida_total}
            onChange={(value) => onChange("divida_total", value)}
            placeholder="15000"
          />
          <FormField
            label="Taxa de Uso de Crédito (%)"
            type="number"
            step="0.01"
            value={form.taxa_uso_credito}
            onChange={(value) => onChange("taxa_uso_credito", value)}
            placeholder="45.5"
          />
          <FormField
            label="Idade do Histórico de Crédito (dias)"
            type="number"
            value={form.idade_historico_credito}
            onChange={(value) => onChange("idade_historico_credito", value)}
            placeholder="5"
          />
        </div>
      </FormSection>

      {/* Seção de comportamento financeiro, com um campo para comportamento de pagamento, permitindo ao usuário fornecer informações sobre seus padrões de gasto e pagamento, o que pode ser um indicador importante para a análise de crédito */}
      <FormSection title="Comportamento Financeiro" subtitle="Padrões de gasto e pagamento">
        <FormSelect
          label="Comportamento de Pagamento"
          value={form.comportamento_pagamento}
          onChange={(value) => onChange("comportamento_pagamento", value)}
          options={PAYMENT_OPTIONS.map((opt) => ({ value: opt.value, label: opt.label }))}
        />
      </FormSection>

      {/* Seção de investimentos e saldo, com campos para investimento mensal e saldo final do mês, permitindo ao usuário fornecer informações sobre sua capacidade de poupança e investimento, o que pode ser um indicador importante para a análise de crédito */}
      <FormSection title="Investimentos e Saldo" subtitle="Capacidade de poupança e investimento">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <FormField
            label="Investimento Mensal (R$)"
            type="number"
            value={form.investimento_mensal}
            onChange={(value) => onChange("investimento_mensal", value)}
            placeholder="500"
          />
          <FormField
            label="Saldo Final do Mês (R$)"
            type="number"
            value={form.saldo_final_mes}
            onChange={(value) => onChange("saldo_final_mes", value)}
            placeholder="2000"
          />
        </div>
      </FormSection> 

      {/* Botões para analisar o score de crédito e limpar o formulário, com um estado de carregamento para indicar quando a análise está em andamento, desabilitando os botões durante a análise para evitar múltiplas submissões */}
      <div className="flex gap-4 mt-8">
        <button
          onClick={onAnalyze}
          disabled={loading}
          className="flex-1 flex items-center justify-center gap-2 bg-blue-600 hover:bg-blue-700 disabled:bg-slate-700 disabled:cursor-not-allowed text-white font-semibold py-3 px-6 rounded-lg transition-all duration-200"
        >
          {loading && <Loader2 className="w-5 h-5 animate-spin" />}
          {loading ? "Analisando..." : "Analisar Score de Crédito"}
        </button>
        <button
          onClick={onReset}
          disabled={loading}
          className="px-6 bg-slate-700 hover:bg-slate-600 disabled:bg-slate-700 disabled:cursor-not-allowed text-white font-semibold py-3 rounded-lg transition-all duration-200"
        >
          Limpar
        </button>
      </div>
    </div>
  );
}