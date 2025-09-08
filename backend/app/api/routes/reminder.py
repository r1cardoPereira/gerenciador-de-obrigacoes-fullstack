from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.reminder import ReminderSettingsCreate, ReminderSettingsRead
from app.service.reminder import (
    create_reminder_settings,
    get_reminder_settings_by_user,
    update_reminder_settings,
    delete_reminder_settings
)
from app.api.deps import get_db

router = APIRouter(prefix="/reminders", tags=["Reminder Settings"])


@router.post("/", response_model=ReminderSettingsRead)
def create(reminder_in: ReminderSettingsCreate, db: Session = Depends(get_db)):
    return create_reminder_settings(db, reminder_in)


@router.get("/user/{usuario_id}", response_model=ReminderSettingsRead)
def read(usuario_id: UUID, db: Session = Depends(get_db)):
    reminder = get_reminder_settings_by_user(db, usuario_id)
    if not reminder:
        raise HTTPException(status_code=404, detail="Reminder settings not found")
    return reminder


@router.put("/user/{usuario_id}", response_model=ReminderSettingsRead)
def update(usuario_id: UUID, reminder_in: ReminderSettingsCreate, db: Session = Depends(get_db)):
    reminder = update_reminder_settings(db, usuario_id, reminder_in)
    if not reminder:
        raise HTTPException(status_code=404, detail="Reminder settings not found")
    return reminder


@router.delete("/user/{usuario_id}", response_model=bool)
def delete(usuario_id: UUID, db: Session = Depends(get_db)):
    return delete_reminder_settings(db, usuario_id)
