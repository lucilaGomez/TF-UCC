from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JobOfferBase(BaseModel):
    email: str
    company_email: str
    title: str
    description: Optional[str] = None
    requirements: Optional[str] = None
    location: Optional[str] = None
    salary: Optional[float] = None

class JobOfferCreate(JobOfferBase):
    pass

class JobOfferResponse(JobOfferBase):
    id: int
    published_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
