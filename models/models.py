import enum
from datetime import date
from sqlalchemy import Column, Integer, String, Boolean, Date, Numeric, ForeignKey, Enum
from sqlalchemy.orm import relationship
from core.database import Base  # Importa a Base declarativa configurada no core


class PerfilUsuario(str, enum.Enum):
    MEMBRO = "MEMBRO"
    BIBLIOTECARIO = "BIBLIOTECARIO"


class StatusEmprestimo(str, enum.Enum):
    ATIVO = "ATIVO"
    DEVOLVIDO = "DEVOLVIDO"
    ATRASADO = "ATRASADO"


# --- 1. USUÁRIO ---
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    perfil = Column(Enum(PerfilUsuario), default=PerfilUsuario.MEMBRO, nullable=False)
    ativo = Column(Boolean, default=True, nullable=False)

    # Relacionamentos
    emprestimos = relationship("Emprestimo", back_populates="usuario")


# --- 2. LIVRO (Catálogo) ---
class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    titulo = Column(String(150), nullable=False, index=True)
    autor = Column(String(100), nullable=False, index=True)
    isbn = Column(String(13), unique=True, index=True, nullable=False)
    categoria = Column(String(50), nullable=False)

    # Relacionamentos
    exemplares = relationship("Exemplar", back_populates="livro", cascade="all, delete-orphan")


# --- 3. EXEMPLAR (Acervo Físico) ---
class Exemplar(Base):
    __tablename__ = "exemplares"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    livro_id = Column(Integer, ForeignKey("livros.id"), nullable=False)
    disponivel = Column(Boolean, default=True, nullable=False)

    # Relacionamentos
    livro = relationship("Livro", back_populates="exemplares")
    emprestimos = relationship("Emprestimo", back_populates="exemplar")


# --- 4. EMPRÉSTIMO ---
class Emprestimo(Base):
    __tablename__ = "emprestimos"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    exemplar_id = Column(Integer, ForeignKey("exemplares.id"), nullable=False)
    data_emprestimo = Column(Date, default=date.today, nullable=False)
    data_devolucao_prevista = Column(Date, nullable=False)
    data_devolucao_real = Column(Date, nullable=True)
    status = Column(Enum(StatusEmprestimo), default=StatusEmprestimo.ATIVO, nullable=False)

    # Relacionamentos
    usuario = relationship("Usuario", back_populates="emprestimos")
    exemplar = relationship("Exemplar", back_populates="emprestimos")
    multa = relationship("Multa", back_populates="emprestimo", uselist=False)


# --- 5. MULTA ---
class Multa(Base):
    __tablename__ = "multas"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    emprestimo_id = Column(Integer, ForeignKey("emprestimos.id"), nullable=False, unique=True)
    valor = Column(Numeric(10, 2), nullable=False)
    paga = Column(Boolean, default=False, nullable=False)

    # Relacionamentos
    emprestimo = relationship("Emprestimo", back_populates="multa")