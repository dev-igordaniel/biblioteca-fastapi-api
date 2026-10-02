from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Gerencia e valida as configurações globais e variáveis de ambiente da aplicação.
    Os valores definidos aqui atuam como fallback caso não estejam presentes no .env.
    """
    
    # --- Configurações de Conexão com o Banco de Dados ---
    # String de conexão com o MySQL utilizando o driver PyMySQL
    DATABASE_URL: str = "mysql+pymysql://usuario:senha@localhost:3306/biblioteca_db"

    # --- Configurações de Segurança e Tokens JWT ---
    # Chave secreta para assinatura dos tokens JWT (substituir em produção)
    SECRET_KEY: str = "sua_chave_secreta_jwt_muito_segura_aqui_123456"
    
    # Algoritmo de criptografia do token JWT
    ALGORITHM: str = "HS256"
    
    # Tempo de expiração do token de acesso em minutos
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        # Define o arquivo fonte de onde as variáveis de ambiente serão lidas
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instância única exportada para acesso fácil em toda a aplicação
settings = Settings()