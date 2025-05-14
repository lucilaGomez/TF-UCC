from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from pydantic import EmailStr

from ..schemas.user import (
    UserCreate,
    UserResponse,
    LoginRequest,
    LoginResponse,
    UserListResponse,
    UserUpdate,
)
from ..services.user_service import (
    create_user,
    authenticate_user,
    list_users,
    get_user_by_email_service,
    update_user_service,
    delete_user_service
)
from ..database.session import get_db
from ..auth.jwt import create_access_token, get_current_user

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    user_db = create_user(db, user)
    return user_db

@router.post("/login", response_model=LoginResponse)
def login_user(user: LoginRequest, db: Session = Depends(get_db)):
    user_db = authenticate_user(db, user.email, user.password)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/users/", response_model=UserListResponse)
def get_users(db: Session = Depends(get_db)):
    users = list_users(db)
    return {"users": users}

@router.get("/users/{email}", response_model=UserResponse)
def get_user_by_email(email: EmailStr, db: Session = Depends(get_db)):
    user = get_user_by_email_service(db, email)
    return user

@router.put("/users/{email}", response_model=UserResponse)
def update_user(email: EmailStr, user_update: UserUpdate, db: Session = Depends(get_db)):
    return update_user_service(db, email, user_update)

@router.delete("/users/{email}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(email: EmailStr, db: Session = Depends(get_db)):
    delete_user_service(db, email)
    return {"detail": "Usuario eliminado correctamente"}

@router.get("/me", response_model=UserResponse)
def get_logged_in_user(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(user).filter(user.email == current_user["sub"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user