from sqlalchemy.orm import Session
from ..models.job_offer import JobOffer
from ..schemas.job_offer import JobOfferCreate
from fastapi import HTTPException, status

def create_job_opening(db: Session, job_opening_data: JobOfferCreate) -> JobOffer:
    new_job_offer = JobOffer(
        email=job_opening_data.email,
        company_email=job_opening_data.company_email,
        title=job_opening_data.title,
        description=job_opening_data.description,
        requirements=job_opening_data.requirements,
        location=job_opening_data.location,
        salary=job_opening_data.salary
    )

    db.add(new_job_offer)
    db.commit()
    db.refresh(new_job_offer)

    return new_job_offer

def get_all_job_openings(db: Session):
    return db.query(JobOffer).order_by(JobOffer.publication_date.desc()).all()

