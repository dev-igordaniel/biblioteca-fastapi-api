# 📚 Library Management API (FastAPI)

API RESTful de alta performance projetada para o gerenciamento completo de acervos bibliográficos, controle de empréstimos, devoluções, controle de acesso e cálculo automatizado de multas.

O projeto utiliza uma **arquitetura modular** inspirada em padrões de separação de responsabilidades (Controller, Service, Repository, DTO), oferecendo escalabilidade, facilidade de manutenção e documentação interativa automatizada.

---

## 🛠️️ Tecnologias Utilizadas

- **Linguagem:** Python 3.11+
- **Framework Web:** FastAPI
- **Servidor ASGI:** Uvicorn
- **ORM:** SQLAlchemy
- **Validação de Dados & DTOs:** Pydantic
- **Banco de Dados:** MySQL
- **Autenticação & Segurança:** Passlib (`bcrypt`), PyJWT (OAuth2 Bearer Token)

---

## 🏛️ Arquitetura do Projeto

A aplicação está organizada em camadas bem definidas para isolar a lógica de apresentação, negócios e acesso a dados:

```text
├── core/           # Configurações de banco de dados, variáveis de ambiente e segurança
├── models/         # Entidades ORM do SQLAlchemy (mapeamento do banco de dados)
├── schemas/        # Schemas do Pydantic (data transfer objects / validações)
├── repositories/   # Camada de persistência e consultas ao banco (CRUD)
├── services/       # Regras de negócio e validações do domínio
└── routers/        # Endpoints REST expostos pela API (FastAPI APIRouter)