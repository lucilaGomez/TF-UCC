from sqlalchemy.orm import Session
from models.user import Usuario, TipoUsuario
from schemas.user import UsuarioCreate
from utils.security import hash_password, verify_password
from uuid import UUID
from fastapi import HTTPException, status

def crear_usuario(db: Session, datos: UsuarioCreate) -> Usuario:
    existente = db.query(Usuario).filter(Usuario.email == datos.email).first()
    if existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El email ya está registrado")

    nuevo_usuario = Usuario(
        email=datos.email,
        password_hash=hash_password(datos.password),
        tipo=datos.tipo
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def autenticar_usuario(db: Session, email: str, password: str) -> Usuario:
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario or not verify_password(password, usuario.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    return usuario

def obtener_usuario_por_id(db: Session, usuario_id: UUID) -> Usuario:
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario
