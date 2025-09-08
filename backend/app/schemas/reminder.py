from pydantic import BaseModel
from typing import List
from uuid import UUID

class ReminderSettingsBase(BaseModel):
    dias_antes: List[str]
    canais: List[str]

class ReminderSettingsCreate(ReminderSettingsBase):
    usuario_id: UUID

class ReminderSettingsRead(ReminderSettingsBase):
    id: UUID
    usuario_id: UUID

    class Config:
        orm_mode = True
