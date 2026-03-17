from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.analises import router as analises_router

app = FastAPI(
    title="API de Análise de Crédito",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analises_router)