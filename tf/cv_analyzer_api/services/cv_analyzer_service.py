from sqlalchemy.orm import Session
from ..models.cv_analyzer import CVAnalyzed

from ..schemas.cv_analyzer import CVAnalyzedCreate
from fastapi import HTTPException, status

from IA.cv_analyzer_ia import analyze_cv_text, extract_text_from_pdf

def create_cv_analysis(db: Session, data: CVAnalyzedCreate) -> CVAnalyzed:
    existing_analysis = db.query(CVAnalyzed).filter(CVAnalyzed.email == data.email).first()
    if existing_analysis:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El CV ya ha sido analizado"
        )

    if not data.cv_file:
        raise HTTPException(status_code=400, detail="Se requiere el archivo del CV para analizar.")

    # Aplicar IA
    text = extract_text_from_pdf(data.cv_file)
    result = analyze_cv_text(text)

    # Crear entrada en la base de datos con el resultado del análisis
    new_analysis = CVAnalyzed(
        email=data.email,
        cv_file=data.cv_file,
        analysis_status="procesado",
        analysis_result=result["analysis_result"],
        skills=result["skills"],
        experience=result["experience"],
        education=result["education"],
        analysis_summary=result["analysis_summary"]
    )

    db.add(new_analysis)
    db.commit()
    db.refresh(new_analysis)
    return new_analysis

# ----- Obtener análisis por email -----
def get_cv_analysis_by_email(db: Session, email: str) -> CVAnalyzed:
    result = db.query(CVAnalyzed).filter(CVAnalyzed.email == email).first()
    if not result:
        raise HTTPException(status_code=404, detail= " Análisis no encontrado")
    return result
