from sqlalchemy.orm import Session
from ..models.job_offer import JobOpening
from ..schemas.job_offer import JobOpeningCreate
from fastapi import HTTPException, status

def create_job_opening(db: Session, job_opening_data: JobOpeningCreate) -> JobOpening:

    # Evitamos restricción innecesaria por título duplicado

    new_job_opening = JobOpening(
        email=job_opening_data.email,
        company_email=job_opening_data.company_email,
        title=job_opening_data.title,
        description=job_opening_data.description,
        requirements=job_opening_data.requirements,
        location=job_opening_data.location,
        salary=job_opening_data.salary
        
        # publication_date y update_date se completan automáticamente
    )

    db.add(new_job_opening)
    db.commit()
    db.refresh(new_job_opening)

    return new_job_opening

def get_all_job_openings(db: Session):
    return db.query(JobOpening).order_by(JobOpening.publication_date.desc()).all()

