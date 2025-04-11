from sqlalchemy.orm import Session
from uuid import UUID
from fastapi import HTTPException, status

# Importaciones relativas al paquete user-api
from ..models.user import Usuario, TipoUsuario
from ..schemas.user import UsuarioCreate
from ..utils.security import hash_password, verify_password

def crear_usuario(db: Session, datos: UsuarioCreate) -> Usuario:
    """
    Crea un nuevo usuario si el email no está registrado.
    """
    existente = db.query(Usuario).filter(Usuario.email == datos.email).first()
    if existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El email ya está registrado"
        )

    nuevo_usuario = Usuario(
        email=datos.email,
        password_hash=hash_password(datos.password),  # Contraseña encriptada
        tipo=datos.tipo
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def autenticar_usuario(db: Session, email: str, password: str) -> Usuario:
    """
    Verifica si el usuario existe y si la contraseña es correcta.
    """
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario or not verify_password(password, usuario.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )
    return usuario

def obtener_usuario_por_id(db: Session, usuario_id: UUID) -> Usuario:
    """
    Devuelve un usuario por ID o lanza 404 si no existe.
    """
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return usuario
