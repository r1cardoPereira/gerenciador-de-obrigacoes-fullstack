from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime
from app.core.db import Base
from .document import Document



class Notification(Base):
    __tablename__ = "notifications"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    documento_id = Column(String, ForeignKey("documents.id"), nullable=False)
    tipo = Column(String)  # email, whatsapp
    data_envio = Column(DateTime, default=datetime.utcnow)
    status = Column(String)  # enviado, falhou

    documento = relationship("Document", back_populates="notificacoes")
