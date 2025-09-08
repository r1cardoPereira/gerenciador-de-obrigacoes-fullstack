import uuid
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlmodel import Column, Field, Relationship, SQLModel
from .admin import User

class ReminderSettings(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    usuario_id: uuid.UUID = Field(foreign_key="user.id")
    dias_antes: list[str] = Field(sa_column=Column(ARRAY(String)))  # ARRAY
    canais: list[str] = Field(sa_column=Column(ARRAY(String)))      # ARRAY
    usuario: User = Relationship(back_populates="configuracoes_alerta")