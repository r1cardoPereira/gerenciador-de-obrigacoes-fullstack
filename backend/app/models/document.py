import uuid
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from .company import Company


class Document(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    empresa_id: uuid.UUID = Field(foreign_key="company.id")
    nome: str
    tipo: str | None = None
    data_vencimento: datetime
    arquivo_url: str | None = None
    observacoes: str | None = None
    criado_em: datetime = Field(default_factory=datetime.utcnow)
    atualizado_em: datetime = Field(default_factory=datetime.utcnow)

    empresa: Company = Relationship(back_populates="documentos")
