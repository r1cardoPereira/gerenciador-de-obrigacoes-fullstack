from sqlalchemy import Column, String, DateTime, ForeignKey, Text, Date
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime
from app.core.db import Base
from .company import Company

class Document(Base):
    __tablename__ = "documents"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    empresa_id = Column(String, ForeignKey("companies.id"), nullable=False)
    nome = Column(String, nullable=False)
    tipo = Column(String)
    data_vencimento = Column(Date, nullable=False)
    arquivo_url = Column(String)
    observacoes = Column(Text)
    criado_em = Column(DateTime, default=datetime.utcnow)
    atualizado_em = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    empresa = relationship("Company", back_populates="documentos", lazy="selectin")
