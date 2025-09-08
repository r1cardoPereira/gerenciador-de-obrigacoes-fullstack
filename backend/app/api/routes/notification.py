from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.notification import NotificationCreate, NotificationRead
from app.service.notification import (
    create_notification,
    get_notification,
    get_notifications_by_document,
    delete_notification
)
from app.api.deps import get_db

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.post("/", response_model=NotificationRead)
def create(notification_in: NotificationCreate, db: Session = Depends(get_db)):
    return create_notification(db, notification_in)


@router.get("/{notification_id}", response_model=NotificationRead)
def read(notification_id: UUID, db: Session = Depends(get_db)):
    notification = get_notification(db, notification_id)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification


@router.get("/document/{document_id}", response_model=list[NotificationRead])
def read_by_document(document_id: UUID, db: Session = Depends(get_db)):
    return get_notifications_by_document(db, document_id)


@router.delete("/{notification_id}", response_model=bool)
def delete(notification_id: UUID, db: Session = Depends(get_db)):
    return delete_notification(db, notification_id)
