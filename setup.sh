#!/bin/bash

echo "🚀 Iniciando setup do projeto..."

# =========================
# BACKEND
# =========================
echo "📦 Configurando backend..."

cd backend || exit

if [ ! -d ".venv" ]; then
  echo "🔧 Criando ambiente virtual..."
  python3 -m venv .venv
fi

source .venv/bin/activate

echo "⬇️ Instalando dependências do backend..."
pip install --upgrade pip
pip install -r ./requeriments.txt

# =========================
# TREINAR MODELO SE NÃO EXISTIR
# =========================
if [ ! -f "models/modelo_score_credito.joblib" ]; then
  echo "🧠 Modelo não encontrado. Gerando dataset tratado..."
  python scripts/build_training_dataset.py

  echo "🤖 Treinando modelo..."
  python scripts/train_model.py
else
  echo "✅ Modelo já existe. Pulando etapa de treinamento."
fi

cd ..

# =========================
# FRONTEND
# =========================
echo "📦 Configurando frontend..."

cd credit-score-frontend || exit
echo "⬇️ Instalando dependências do frontend..."
npm install

cd ..

echo "✅ Setup finalizado com sucesso!"
