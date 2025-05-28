from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..schemas.job_offer import JobOfferCreate, JobOfferResponse
from ..services.job_opening_service import create_job_opening, get_all_job_openings
from tf.database.session import get_db

router = APIRouter(
    prefix="/job_offers",
    tags=["Job Offers"]
)

@router.post("/", response_model=JobOfferResponse, status_code=status.HTTP_201_CREATED)
def create_job_opening_route(job_offer: JobOfferCreate, db: Session = Depends(get_db)):
    return create_job_opening(db, job_offer)

@router.get("/", response_model=list[JobOfferResponse])
def get_all_job_offerings_route(db: Session = Depends(get_db)):
    return get_all_job_openings(db)


