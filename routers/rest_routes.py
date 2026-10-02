from fastapi import APIRouter

rest_router = APIRouter()



@rest_router.get("/livros",tags=["Livros e Acervo"])
async def get_livros():
    """
    Lista todos os livros cadastrados.
    Suporta filtros por categoria e busca por título/autor.
    Acesse por Membros e Bibliotecários
    """
    return {"message": "Rota de listagem de livros (GET) - Em desenvolvimento."}

@rest_router.get("/livros/isbn/{isbn}",tags=["Livros e Acervo"])
async def get_livro_by_isbn(isbn: str):
    """
    Busca e retorna os detalhes de um livro específico através do seu ISBN único.
    """
    return {"message": f"Rota de busca de livro por ISBN {isbn} (GET) - Em desenvolvimento."}

@rest_router.post("/livros",tags=["Livros e Acervo"])
async def create_livro():
    """
    Cadastra um novo livro no catálogo (título, autor, ISBN, categoria). Apenas Bibliotecários.
    """
    return {"message": "Rota de cadastro de livro (POST) - Em desenvolvimento."}

@rest_router.delete("/livros/{id}",tags=["Livros e Acervo"])
async def delete_livro(id: int):
    """
    Remove um livro do catálogo. Só permite se não houver empréstimos ativos associados a ele.
    Apaga o acervo em cascata. Apenas Bibliotecários.
    """
    return {"message": f"Rota de exclusão de livro com ID {id} (DELETE) - Em desenvolvimento."}

@rest_router.post("/acervo/exemplares",tags=["Livros e Acervo"])
async def create_exemplar():
    """
    Adiciona exemplares no acervo de um livro já existente no catálogo.
    Apenas Bibliotecários.
    """
    return {"message": "Rota de cadastro de exemplar (POST) - Em desenvolvimento."}

@rest_router.delete("/acervo/exemplares",tags=["Livros e Acervo"])
async def delete_exemplar():
    """
    Remove exemplares do acervo, desde que não estejam vinculados a um empréstimo ativo.
    Apenas Bibliotecários.
    """
    return {"message": "Rota de exclusão de exemplar (DELETE) - Em desenvolvimento."}





@rest_router.post("/emprestimos",tags=["Emprestimos"])
async def create_emprestimo():
    """
    Efetua o empréstimo de um livro.
    Valida: limite de 3 empréstimos ativos, ausência de multas pendentes,
    disponibilidade no acervo e se o usuário já não possui o mesmo livro alugado.
    """
    return {"message": "Rota de criação de empréstimo (POST) - Em desenvolvimento."}

@rest_router.post("/emprestimos/{id}/devolucao",tags=["Emprestimos"])
async def devolver_emprestimo(id: int):
    """
    Registra a devolução do livro, incrementa o acervo e calcula se houve atraso (prazo padrão: 14 dias).
    Se atrasado, gera automaticamente uma multa de R$ 1,00 por dia.
    """
    return {"message": f"Rota de devolução de empréstimo com ID {id} (POST) - Em desenvolvimento."}

@rest_router.get("/emprestimos/meus",tags=["Emprestimos"])
async def get_meus_emprestimos():
    """
    Lista os empréstimos ativos e passados pertencentes ao Membro autenticado.
    """
    return {"message": "Rota de listagem de empréstimos do usuário (GET) - Em desenvolvimento."}

@rest_router.get("/emprestimos",tags=["Emprestimos"])
async def get_emprestimos():
    """
    Lista todos os empréstimos globais. Permite filtrar por status (ex: ?status=atrasado).
    Apenas Bibliotecários.
    """
    return {"message": "Rota de listagem de todos os empréstimos (GET) - Em desenvolvimento."}





@rest_router.get("/multas/minhas", tags=["Multas"])
async def get_minhas_multas():
    """
    Lista as multas (pendentes e quitadas) do Membro logado.
    """
    return {"message": "Rota de listagem de multas do usuário (GET) - Em desenvolvimento."}

@rest_router.get("/multas", tags=["Multas"])
async def get_multas():
    """
    Lista todas as multas registradas no sistema. Apenas Bibliotecários.
    """
    return {"message": "Rota de listagem de todas as multas (GET) - Em desenvolvimento."}

@rest_router.patch("/multas/{id}/quitar", tags=["Multas"])
async def quitar_multa(id: int):
    """
    Altera o status da multa para quitada/paga, liberando o usuário para novos empréstimos. Apenas Bibliotecários.
    """
    return {"message": f"Rota de quitação de multa com ID {id} (PATCH) - Em desenvolvimento."}