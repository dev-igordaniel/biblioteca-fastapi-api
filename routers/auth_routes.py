from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["Autenticação"])

@auth_router.post("/cadastrar")
async def create_user():
    """
    Cadastra um novo usuário no sistema (Membro ou Bibliotecário).
    Valida se o CPF e e-mail já não estão em uso no banco, gera o hash da senha usando bcrypt e salva os dados na tabela Usuario.
    """
    return {"message": "Rota de cadastro de usuário (POST) - Em desenvolvimento."}

@auth_router.post("/login")
async def login_user():
    """
    Autentica o usuário.
    Recebe e-mail e senha no formato de formulário (OAuth2 Form Data),
    valida com o banco de dados e, se estiver correto,
    retorna um Token JWT assinado contendo a identidade e o perfil do usuário.
    """
    return {"message": "Rota de login de usuário (POST) - Em desenvolvimento."}

@auth_router.get("/me")
async def get_user_profile():
    """
    Retorna os dados cadastrais (nome, e-mail, perfil) do usuário que fez a requisição.
    Exige envio do Token JWT no cabeçalho para identificar o usuário logado.
    """
    return {"message": "Rota de perfil do usuário (GET) - Em desenvolvimento."}

@auth_router.put("/me/senha")
async def update_user_password():
    """
    Permite que o usuário autenticado altere sua própria senha.
    Exige a confirmação da senha atual e a nova senha para atualizar o hash criptografado no banco.
    """
    return {"message": "Rota de atualização de senha do usuário (PUT) - Em desenvolvimento."}