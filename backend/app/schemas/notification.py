from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class NotificationBase(BaseModel):
    tipo: str
    status: str

class NotificationCreate(NotificationBase):
    documento_id: UUID

class NotificationRead(NotificationBase):
    id: UUID
    data_envio: datetime
    documento_id: UUID

    class Config:
        orm_mode = True
