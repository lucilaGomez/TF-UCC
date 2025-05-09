from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from ..schemas.job_opening import JobOpeningCreate, JobOpeningResponse
from ..services.job_opening_service import create_job_opening, get_all_job_offers
from ..database.session import get_db

router = APIRouter(prefix="/job_openings", tags=["Job Openings"])

@router.post("/", response_model=JobOpeningResponse, status_code=status.HTTP_201_CREATED)
def create_job_opening_route(job_opening: JobOpeningCreate, db: Session = Depends(get_db)):
    return create_job_opening (db, job_opening)

@router.get("/", response_model=List[JobOpeningResponse])
def get_job_opening_route(db: Session = Depends(get_db)):
    return get_all_job_openings(db)
