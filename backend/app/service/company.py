from sqlalchemy.orm import Session
from uuid import UUID
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


def create_company(db: Session, company_in: CompanyCreate, usuario_id: UUID) -> Company:
    company = Company(**company_in.dict(), usuario_id=str(usuario_id))
    db.add(company)
    db.commit()
    db.refresh(company)
    return company


def get_company(db: Session, company_id: UUID) -> Company | None:
    return db.query(Company).filter(Company.id == str(company_id)).first()


def get_companies_by_user(db: Session, usuario_id: UUID) -> list[Company]:
    return db.query(Company).filter(Company.usuario_id == str(usuario_id)).all()


def update_company(db: Session, company_id: UUID, company_in: CompanyUpdate) -> Company | None:
    company = get_company(db, company_id)
    if not company:
        return None
    for field, value in company_in.dict(exclude_unset=True).items():
        setattr(company, field, value)
    db.commit()
    db.refresh(company)
    return company


def delete_company(db: Session, company_id: UUID) -> bool:
    company = get_company(db, company_id)
    if not company:
        return False
    db.delete(company)
    db.commit()
    return True
