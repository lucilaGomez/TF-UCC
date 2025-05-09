from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List
from ..models.user import User, Candidate
from ..schemas.user import UserCreate, UserUpdate
from ..utils.security import hash_password, verify_password

# Crear un nuevo usuario
def create_user(db: Session, data: UserCreate) -> User:
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email ya registrado")

    new_user = User(
        email=data.email,
        password_hash=hash_password(data.password),
        user_type=data.user_type
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Crear registro en tabla Candidate si el usuario es tipo CANDIDATE
    if data.user_type == "CANDIDATE":
        create_candidate(db, new_user.email)

    return new_user

# Crear registro de Candidate vacío
def create_candidate(db: Session, user_email: str):
    new_candidate = Candidate(email=user_email, cv_file=None)
    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)

# Autenticación
def authenticate_user(db: Session, email: str, password: str) -> User:
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    return user

# Obtener todos los usuarios
def list_users(db: Session) -> List[User]:
    return db.query(User).all()

# Obtener usuario por email
def get_user_by_email_service(db: Session, email: str) -> User:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# Actualizar usuario
def update_user_service(db: Session, email: str, user_update: UserUpdate) -> User:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if user_update.email is not None:
        user.email = user_update.email
    if user_update.user_type is not None:
        user.user_type = user_update.user_type
    if user_update.password is not None:
        user.password_hash = hash_password(user_update.password)

    db.commit()
    db.refresh(user)
    return user

# Eliminar usuario
def delete_user_service(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(user)
    db.commit()
