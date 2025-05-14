from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from ..schemas.job_offer import JobOfferCreate, JobOfferResponse
from ..services.job_offer_service import create_job_offer, get_all_job_offers
from ..database.session import get_db

router = APIRouter()

@router.post("/job_offers/", response_model=JobOfferResponse, status_code=status.HTTP_201_CREATED)
def create_job_offer_route(job_offer: JobOfferCreate, db: Session = Depends(get_db)):
    return create_job_offer(db, job_offer)

@router.get("/job_offers/", response_model=List[JobOfferResponse])
def get_job_offers_route(db: Session = Depends(get_db)):
    return get_all_job_offers(db)
