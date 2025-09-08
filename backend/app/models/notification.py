import uuid
from sqlmodel import Field, Relationship, SQLModel
from .document import Document


class Notification(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    documento_id: uuid.UUID = Field(foreign_key="document.id")
    tipo: str  # email, whatsapp
    data_envio: str | None = None
    status: str  # enviado, falhou

    documento: Document = Relationship(back_populates="notificacoes")




