from ctypes import ARRAY
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime
from app.core.db import Base
from .admin import User


class ReminderSettings(Base):
    __tablename__ = "reminder_settings"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    usuario_id = Column(String, ForeignKey("user.id"), nullable=False)
    dias_antes = Column(ARRAY(String))  # ["30", "15", "7"]
    canais = Column(ARRAY(String))      # ["email", "whatsapp"]

    usuario = relationship("User", back_populates="configuracoes_alerta")
