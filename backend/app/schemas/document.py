from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime, date



class DocumentBase(BaseModel):
    nome: str
    tipo: Optional[str] = None
    data_vencimento: date
    arquivo_url: Optional[str] = None
    observacoes: Optional[str] = None

class DocumentCreate(DocumentBase):
    empresa_id: UUID
class DocumentUpdate(DocumentBase):
    pass

class DocumentRead(DocumentBase):
    id: UUID
    empresa_id: UUID
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        orm_mode = True
