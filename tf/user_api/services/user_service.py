from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List
from ..models.user import User, Person, Candidate
from ..schemas.user import RegisterUserSchema, UserCreate, UserUpdate
from ..utils.security import hash_password, verify_password

def create_user(db: Session, data: RegisterUserSchema) -> User:
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email ya registrado")

    new_user = User(
        email=data.email,
        password_hash=hash_password(data.password),
        user_type=data.user_type
    )
    db.add(new_user)

    new_person = Person(
        email=data.email,
        first_name=data.first_name,
        last_name=data.last_name,
        gender=data.gender,
        birth_date=data.birth_date,
        address=data.address
    )
    db.add(new_person)

    if data.user_type == "CANDIDATE":
        new_candidate = Candidate(email=data.email)
        db.add(new_candidate)

    db.commit()
    db.refresh(new_user)
    return new_user

# def create_candidate(db: Session, user_email: str):
#     new_candidate = Candidate(email=user_email, cv_file=None)
#     db.add(new_candidate)
#     db.commit()
#     db.refresh(new_candidate)

def authenticate_user(db: Session, email: str, password: str) -> User:
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    return user

def list_users(db: Session) -> List[User]:
    return db.query(User).all()

def get_user_by_email_service(db: Session, email: str) -> User:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

def update_user_service(db: Session, email: str, user_update: UserUpdate) -> User:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Opcional: evitar cambiar email si rompe integridad referencial
    if user_update.email is not None:
        raise HTTPException(status_code=400, detail="No se permite cambiar el email")

    if user_update.password is not None:
        user.password_hash = hash_password(user_update.password)

    db.commit()
    db.refresh(user)
    return user

def delete_user_service(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(user)
    db.commit()
