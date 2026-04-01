## 📌 Visão Geral

Este projeto consiste em uma aplicação web completa para análise de crédito, integrando frontend moderno, backend robusto e um modelo de Machine Learning para classificação de risco financeiro.

A aplicação permite que usuários realizem cadastro, autenticação e submetam informações financeiras para receber uma avaliação automatizada de score de crédito. Todo o fluxo foi desenvolvido com foco em simplicidade, desempenho e organização de código, simulando um cenário real de sistemas utilizados em instituições financeiras.

---

## 🎯 Objetivo

O principal objetivo do projeto é desenvolver um sistema inteligente capaz de auxiliar na tomada de decisão de crédito, utilizando dados financeiros do usuário para gerar uma classificação de risco de forma automatizada.

Além disso, o projeto busca:

* Aplicar conceitos de desenvolvimento fullstack (React + FastAPI)
* Integrar autenticação segura com JWT
* Utilizar Machine Learning para análise preditiva
* Simular um sistema real de avaliação de crédito
* Servir como base para evolução em um produto SaaS

---

## 🧠 Funcionalidades

* 🔐 Autenticação de usuários (Login / Register)
* 👤 Gerenciamento de sessão (JWT)
* 📊 Análise de crédito via IA
* 📈 Classificação de score (baixo, médio, alto risco)
* 🧾 Formulário completo de dados financeiros
* 🖥️ Interface moderna com React + Tailwind

---

## 🛠️ Tecnologias utilizadas

### Frontend

* React (Vite)
* TypeScript
* TailwindCSS
* React Router

### Backend

* FastAPI
* Python
* JWT (Autenticação)
* MongoDB
* Pydantic

### Machine Learning

* Scikit-learn
* Pandas
* Joblib

---

## ⚙️ Como rodar o projeto

> O projeto já está disponível online no link acima.  
[text](https://projeto-score-credito-web.vercel.app/)

> Caso queira executar localmente, siga os passos abaixo.

### 🔙 Backend (FastAPI)

```bash

cd backend

python -m venv .venv

source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows

pip install -r requirements.txt

python scripts/train_model.py

uvicorn app.main:app --reload
```

Servidor disponível em:

```
http://127.0.0.1:8000
```

---

### 🔜 Frontend (React)

```bash
cd credi-score-frontend

npm install
npm run dev
```

App disponível em:

```
http://localhost:5173
```

---

## 🔄 Fluxo de funcionamento

1. O usuário acessa a aplicação através do navegador (localhost).

2. Ao entrar no sistema, ele pode escolher entre:

   * Fazer login (caso já tenha conta)
   * Realizar cadastro (caso ainda não tenha)

3. Se optar por cadastro:

   * Preenche nome, email e senha
   * O sistema registra o usuário
   * O usuário já é autenticado automaticamente

4. Se optar por login:

   * Informa email e senha
   * O sistema valida as credenciais
   * Em caso de sucesso, o usuário é autenticado

5. Após autenticado:

   * O usuário é redirecionado para o dashboard

6. No dashboard:

   * O usuário preenche os dados financeiros necessários para análise

7. O sistema:

   * Envia os dados para o backend
   * O modelo de Machine Learning processa as informações

8. O resultado da análise é retornado:

   * Classificação de crédito (ex: bom, médio, ruim)
   * Exibição na interface para o usuário

9. O usuário pode:

   * Fazer novas análises
   * Ou realizar logout

10. Ao realizar logout:

    * A sessão é encerrada
    * O usuário retorna para a tela de login