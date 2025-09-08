import uuid
from sqlmodel import Field, Relationship, SQLModel
from .admin import User


class ReminderSettings(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    usuario_id: uuid.UUID = Field(foreign_key="user.id")
    dias_antes: list[str]  # ["30", "15", "7"]
    canais: list[str]      # ["email", "whatsapp"]

    usuario: User = Relationship(back_populates="configuracoes_alerta")


