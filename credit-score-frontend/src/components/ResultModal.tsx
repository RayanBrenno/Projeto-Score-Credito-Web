import type { PredictionResponse, CreditClass } from "../types";
import { X, CheckCircle, AlertCircle, TrendingDown } from "lucide-react";

interface ResultModalProps {
  result: PredictionResponse | null;
  isOpen: boolean;
  onClose: () => void;
}

function getClassificationColor(classe?: CreditClass) {
  switch (classe) {
    case "Good":
      return "bg-green-500/20 border-green-500/50 text-green-300";
    case "Standard":
      return "bg-blue-500/20 border-blue-500/50 text-blue-300";
    case "Poor":
      return "bg-red-500/20 border-red-500/50 text-red-300";
    default:
      return "bg-slate-500/20 border-slate-500/50 text-slate-300";
  }
}

function getClassificationLabel(classe?: CreditClass) {
  switch (classe) {
    case "Good":
      return "Excelente";
    case "Standard":
      return "Padrão";
    case "Poor":
      return "Baixo";
    default:
      return "Indefinido";
  }
}

function getClassificationIcon(classe?: CreditClass) {
  switch (classe) {
    case "Good":
      return <CheckCircle className="w-10 h-10 text-green-400" />;
    case "Standard":
      return <TrendingDown className="w-10 h-10 text-blue-400" />;
    case "Poor":
      return <AlertCircle className="w-10 h-10 text-red-400" />;
    default:
      return <AlertCircle className="w-10 h-10 text-slate-400" />;
  }
}

export default function ResultModal({ result, isOpen, onClose }: ResultModalProps) {
  if (!isOpen || !result) return null;

  const classe = result.classe;
  const classColor = getClassificationColor(classe);
  const classLabel = getClassificationLabel(classe);

  return (
    <div className="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 rounded-2xl shadow-2xl max-w-md w-full">

        <div className="flex items-center justify-between p-6 border-b border-slate-700">
          <h2 className="text-2xl font-bold text-white">
            Resultado da Análise
          </h2>

          <button
            onClick={onClose}
            className="text-slate-400 hover:text-white transition-colors"
          >
            <X className="w-6 h-6" />
          </button>
        </div>

        <div className="p-6 space-y-6">

          <div className="bg-slate-700/30 rounded-xl p-6 text-center border border-slate-700">
            <div className="flex justify-center mb-4">
              {getClassificationIcon(classe)}
            </div>

            <div className="text-3xl font-bold text-white">
              {classLabel}
            </div>

            <p className="text-slate-400 text-sm mt-2">
              Classificação de Crédito
            </p>
          </div>

          <div className={`rounded-xl p-4 border ${classColor}`}>
            <p className="text-sm font-medium">Classificação</p>
            <p className="text-xl font-bold">{classe}</p>
          </div>

          {result.message && (
            <div className="bg-slate-700/30 rounded-xl p-4 border border-slate-700">
              <p className="text-slate-300 text-sm">
                {result.message}
              </p>
            </div>
          )}

          <button
            onClick={onClose}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-lg transition-all"
          >
            Fechar
          </button>

        </div>
      </div>
    </div>
  );
}