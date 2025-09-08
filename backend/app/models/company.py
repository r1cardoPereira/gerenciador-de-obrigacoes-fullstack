import uuid
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from .document import Document

class Company(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    nome: str
    cnpj: str | None = Field(default=None, unique=True)
    usuario_id: uuid.UUID = Field(foreign_key="user.id")
    criado_em: datetime = Field(default_factory=datetime.utcnow)
    atualizado_em: datetime = Field(default_factory=datetime.utcnow)
    documentos: list[Document] = Relationship(back_populates="empresa")