from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from ..schemas.cv_analyzer import CVAnalyzedCreate, CVAnalyzedResponse
from ..services.cv_analyzer_service import create_cv_analysis, get_cv_analysis_by_email

from tf.database.session import get_db


router = APIRouter(
    prefix="/cv_analysis",
    tags=["CV Analysis"]
)

# ----- Crear un análisis de CV -----
@router.post("/", response_model=CVAnalyzedResponse, status_code=status.HTTP_201_CREATED)
def create_cv_analysis_route(cv_analysis: CVAnalyzedCreate, db: Session = Depends(get_db)):
    return create_cv_analysis(db, cv_analysis)

# ----- Obtener análisis de CV por email -----
@router.get("/user/{email}", response_model=CVAnalyzedResponse)
def get_cv_analysis_route(email: str, db: Session = Depends(get_db)):
    return get_cv_analysis_by_email(db, email)
