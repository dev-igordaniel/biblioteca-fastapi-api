# ⚙️ Módulo Core (`/core`)

Este módulo é responsável por concentrar a infraestrutura base e as configurações globais da aplicação. Ele fornece a abstração necessária para a conexão com o banco de dados MySQL e o gerenciamento de variáveis de ambiente e parâmetros de segurança.

---

## 📁 Estrutura de Arquivos

| Arquivo | Função |
| :--- | :--- |
| **`config.py`** | Mapeia e valida as variáveis de ambiente a partir do arquivo `.env` utilizando a classe `BaseSettings` do Pydantic. Centraliza a URL do banco de dados, chaves do JWT e algoritmo de criptografia. |
| **`database.py`** | Inicializa o mecanismo de conexão do SQLAlchemy (`engine`), define a fábrica de sessões (`SessionLocal`), instancia a classe `Base` (herdada por todos os modelos) e exporta a função `get_db()` para injeção de dependência no FastAPI. |

---

## ⚙️ Uso e Injeção de Dependência

A função `get_db()` exposta por este módulo gerencia o ciclo de vida das conexões com o banco de dados em cada requisição:

1. **Abertura:** Instancia uma nova sessão do SQLAlchemy quando uma rota é acionada.
2. **Execução:** Prova a sessão para repositories/services através de injeção de dependência (`Depends(get_db)`).
3. **Fechamento:** Garante o encerramento da conexão ao término da requisição, prevenindo vazamentos de conexões (*connection leaks*).