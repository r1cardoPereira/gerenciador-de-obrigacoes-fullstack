from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.document import DocumentCreate, DocumentUpdate, DocumentRead
from app.service.document import (
    create_document,
    get_document,
    get_documents_by_company,
    update_document,
    delete_document
)
from app.api.deps import get_db
router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/", response_model=DocumentRead)
def create(document_in: DocumentCreate, db: Session = Depends(get_db)):
    return create_document(db, document_in)


@router.get("/{document_id}", response_model=DocumentRead)
def read(document_id: UUID, db: Session = Depends(get_db)):
    document = get_document(db, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document


@router.get("/company/{company_id}", response_model=list[DocumentRead])
def read_by_company(company_id: UUID, db: Session = Depends(get_db)):
    return get_documents_by_company(db, company_id)


@router.put("/{document_id}", response_model=DocumentRead)
def update(document_id: UUID, document_in: DocumentUpdate, db: Session = Depends(get_db)):
    document = update_document(db, document_id, document_in)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document


@router.delete("/{document_id}", response_model=bool)
def delete(document_id: UUID, db: Session = Depends(get_db)):
    return delete_document(db, document_id)
