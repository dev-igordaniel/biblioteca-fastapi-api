from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from core.config import settings

# --- Configuração de Argumentos do Engine ---
# O SQLite precisa do 'check_same_thread': False para funcionar corretamente com o FastAPI
connect_args = {"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}



# --- Engine de Conexão ---
# Instancia o mecanismo que gerencia as conexões com o banco de dados MySQL
engine = create_engine(
    settings.DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True  # Verifica se a conexão está ativa antes de executar queries
)

# --- Fábrica de Sessões ---
# Cria sessões locais para cada requisição na API
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# --- Classe Base Declarativa ---
# Mapeador base do qual todos os Models do SQLAlchemy irão herdar
Base = declarative_base()


# --- Injeção de Dependência ---
def get_db():
    """
    Prover uma sessão do banco de dados por requisição no FastAPI 
    e garante seu fechamento automático ao finalizar.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()