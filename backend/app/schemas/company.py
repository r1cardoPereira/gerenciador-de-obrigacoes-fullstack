from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class CompanyBase(BaseModel):
    nome: str
    cnpj: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(CompanyBase):
    pass

class CompanyRead(CompanyBase):
    id: UUID
    usuario_id: UUID
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        orm_mode = True
