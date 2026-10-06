from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Gerencia e valida as configurações globais e variáveis de ambiente da aplicação.
    """
    
    # --- Configuração de Conexão SQLite ---
    DATABASE_URL: str = "sqlite:///./biblioteca.db"

    # --- Configurações de Segurança e Tokens JWT ---
    SECRET_KEY: str = "sua_chave_secreta_jwt_muito_segura_aqui_123456"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instância única exportada para acesso fácil em toda a aplicação
settings = Settings()






