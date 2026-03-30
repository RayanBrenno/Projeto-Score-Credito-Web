#!/bin/bash

echo "🚀 Subindo aplicação..."

# =========================
# BACKEND
# =========================
echo "🧠 Iniciando backend..."

cd backend || exit
source .venv/bin/activate

uvicorn app.main:app --reload &

cd ..

# =========================
# FRONTEND
# =========================
echo "💻 Iniciando frontend..."

cd credit-score-frontend || exit

npm run dev &

cd ..

echo "✅ Aplicação iniciada!"

wait