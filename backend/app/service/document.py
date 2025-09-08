from sqlalchemy.orm import Session
from uuid import UUID
from app.models.document import Document
from app.schemas.document import DocumentCreate, DocumentUpdate


def create_document(db: Session, document_in: DocumentCreate) -> Document:
    doc = Document(**document_in.dict())
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc


def get_document(db: Session, document_id: UUID) -> Document | None:
    return db.query(Document).filter(Document.id == str(document_id)).first()


def get_documents_by_company(db: Session, company_id: UUID) -> list[Document]:
    return db.query(Document).filter(Document.empresa_id == str(company_id)).all()


def update_document(db: Session, document_id: UUID, document_in: DocumentUpdate) -> Document | None:
    doc = get_document(db, document_id)
    if not doc:
        return None
    for field, value in document_in.dict(exclude_unset=True).items():
        setattr(doc, field, value)
    db.commit()
    db.refresh(doc)
    return doc


def delete_document(db: Session, document_id: UUID) -> bool:
    doc = get_document(db, document_id)
    if not doc:
        return False
    db.delete(doc)
    db.commit()
    return True


def get_all_documents(db: Session) -> list[Document]:
    return db.query(Document).all()