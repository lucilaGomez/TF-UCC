from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, status
from sqlalchemy.orm import Session
import shutil
import os
import uuid

from tf.user_api.models.user import Candidate
from tf.database.session import get_db

router = APIRouter()

UPLOAD_DIR = "uploaded_cvs"  # carpeta donde se guardan los archivos

# Crear la carpeta si no existe
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@router.post("/cv/upload/{candidate_email}", status_code=status.HTTP_200_OK)
async def upload_cv(
    candidate_email: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    # Validar que el candidato existe
    candidate = db.query(Candidate).filter(Candidate.email == candidate_email).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")

    # Crear un nombre único para el archivo
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # Guardar el archivo en disco
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Actualizar ruta en la DB
    candidate.cv_file = file_path
    db.commit()
    db.refresh(candidate)

    return {"filename": unique_filename, "detail": "Archivo subido correctamente"}
