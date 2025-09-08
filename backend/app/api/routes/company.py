from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.company import CompanyCreate, CompanyUpdate, CompanyRead
from app.service.company import (
    create_company,
    get_company,
    get_companies_by_user,
    update_company,
    delete_company
)
from app.api.deps import get_db

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.post("/user/{usuario_id}", response_model=CompanyRead)
def create(usuario_id: UUID, company_in: CompanyCreate, db: Session = Depends(get_db)):
    return create_company(db, company_in, usuario_id)


@router.get("/{company_id}", response_model=CompanyRead)
def read(company_id: UUID, db: Session = Depends(get_db)):
    company = get_company(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.get("/user/{usuario_id}", response_model=list[CompanyRead])
def read_by_user(usuario_id: UUID, db: Session = Depends(get_db)):
    return get_companies_by_user(db, usuario_id)


@router.put("/{company_id}", response_model=CompanyRead)
def update(company_id: UUID, company_in: CompanyUpdate, db: Session = Depends(get_db)):
    company = update_company(db, company_id, company_in)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.delete("/{company_id}", response_model=bool)
def delete(company_id: UUID, db: Session = Depends(get_db)):
    return delete_company(db, company_id)
