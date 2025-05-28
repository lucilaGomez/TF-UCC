from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import EmailStr

from tf.database.session import get_db
from ..schemas.user import PersonUpdateSchema, CompanyUpdateSchema
from ..models.user import Person, Company

router = APIRouter()

@router.put("/person/{email}", response_model=PersonUpdateSchema)
def update_person(email: EmailStr, person_update: PersonUpdateSchema, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.email == email).first()
    if not person:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    
    for key, value in person_update.dict(exclude_unset=True).items():
        setattr(person, key, value)
    
    db.commit()
    db.refresh(person)
    return person

@router.put("/company/{company_email}", response_model=CompanyUpdateSchema)
def update_company(company_email: EmailStr, company_update: CompanyUpdateSchema, db: Session = Depends(get_db)):
    company = db.query(Company).filter(Company.company_email == company_email).first()
    if not company:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")

    for key, value in company_update.dict(exclude_unset=True).items():
        setattr(company, key, value)
    
    db.commit()
    db.refresh(company)
    return company
