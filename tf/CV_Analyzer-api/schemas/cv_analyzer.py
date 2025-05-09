from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ----- Base Schema -----
class CVAnalyzedBase(BaseModel):
    email: str
    cv_file: Optional[str]
    analysis_status: Optional[str]
    analysis_result: Optional[str]
    skills: Optional[str]
    experience: Optional[str]
    education: Optional[str]
    analysis_summary: Optional[str]

# ----- Esquema para creación -----
class CVAnalyzedCreate(BaseModel):
    email: str
    cv_file: Optional[str]
    analysis_status: Optional[str]
    analysis_result: Optional[str]
    skills: Optional[str]
    experience: Optional[str]
    education: Optional[str]
    analysis_summary: Optional[str]

# ----- Esquema para respuesta -----
class CVAnalyzedResponse(CVAnalyzedBase):
    analysis_date: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
