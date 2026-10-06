# Para rodar o código execute no terminal: uvicorn main:app --reload
from fastapi import FastAPI
from routers.auth_routes import auth_router
from routers.rest_routes import rest_router

app = FastAPI(
    title="Sistema de Biblioteca API",
    description="API para gerenciamento de acervo, usuários, empréstimos e multas.",
    version="1.0.0"
)

# Registro dos roteadores
app.include_router(auth_router)
app.include_router(rest_router)


@app.get("/", tags=["Status"])
async def root():
    return {"message": "API do Sistema de Biblioteca rodando com sucesso!"}