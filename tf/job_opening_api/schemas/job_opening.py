from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JobOpeningBase(BaseModel):
    email: str
    company_email: str
    title: str
    description: Optional[str] = None
    requirements: Optional[str] = None
    location: Optional[str] = None
    salary: Optional[float] = None

class JobOpeningCreate(JobOpeningBase):
    pass

class JobOpeningResponse(JobOpeningBase):
    id_job_opening: int
    publication_date: datetime
    update_date: datetime

    class Config:
        orm_mode = True
