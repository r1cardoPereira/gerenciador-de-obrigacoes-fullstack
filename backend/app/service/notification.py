from sqlalchemy.orm import Session
from uuid import UUID
from app.models.notification import Notification
from app.schemas.notification import NotificationCreate


def create_notification(db: Session, notification_in: NotificationCreate) -> Notification:
    notification = Notification(**notification_in.dict())
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return notification


def get_notification(db: Session, notification_id: UUID) -> Notification | None:
    return db.query(Notification).filter(Notification.id == str(notification_id)).first()


def get_notifications_by_document(db: Session, document_id: UUID) -> list[Notification]:
    return db.query(Notification).filter(Notification.documento_id == str(document_id)).all()


def delete_notification(db: Session, notification_id: UUID) -> bool:
    notification = get_notification(db, notification_id)
    if not notification:
        return False
    db.delete(notification)
    db.commit()
    return True
