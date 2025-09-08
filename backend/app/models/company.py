from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime
from app.core.db import Base
from .document import Document

class Company(Base):
    __tablename__ = "companies"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    nome = Column(String, nullable=False)
    cnpj = Column(String, unique=True)
    usuario_id = Column(String, ForeignKey("users.id"), nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)
    atualizado_em = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    documentos = relationship("Document", back_populates="empresa", lazy="selectin")
