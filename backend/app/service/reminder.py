from sqlalchemy.orm import Session
from uuid import UUID
from app.models.reminder import ReminderSettings
from app.schemas.reminder import ReminderSettingsCreate


def create_reminder_settings(db: Session, reminder_in: ReminderSettingsCreate) -> ReminderSettings:
    reminder = ReminderSettings(**reminder_in.dict())
    db.add(reminder)
    db.commit()
    db.refresh(reminder)
    return reminder


def get_reminder_settings_by_user(db: Session, usuario_id: UUID) -> ReminderSettings | None:
    return db.query(ReminderSettings).filter(ReminderSettings.usuario_id == str(usuario_id)).first()


def update_reminder_settings(db: Session, usuario_id: UUID, reminder_in: ReminderSettingsCreate) -> ReminderSettings | None:
    reminder = get_reminder_settings_by_user(db, usuario_id)
    if not reminder:
        return None
    for field, value in reminder_in.dict(exclude_unset=True).items():
        setattr(reminder, field, value)
    db.commit()
    db.refresh(reminder)
    return reminder


def delete_reminder_settings(db: Session, usuario_id: UUID) -> bool:
    reminder = get_reminder_settings_by_user(db, usuario_id)
    if not reminder:
        return False
    db.delete(reminder)
    db.commit()
    return True
