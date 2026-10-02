#para rodar nosso codigo executar no terminal: uvicorn main:app --reload
from fastapi import FastAPI;
app = FastAPI();

from routers.auth_routes import auth_router;
from routers.rest_routes import rest_router;

app.include_router(auth_router);
app.include_router(rest_router);


