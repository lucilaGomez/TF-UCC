from fastapi import APIRouter, HTTPException, Depends, status
from user_api.schemas.user import UsuarioCreate, UsuarioResponse, LoginRequest, LoginResponse  # Importación absoluta
from user_api.services.user_service import crear_usuario, autenticar_usuario  # Importación absoluta
from user_api.database.session import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from user_api.auth.jwt import create_access_token

# Inicializamos el router
router = APIRouter()

# Endpoints de usuario

@router.post("/register", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    """
    Registra un nuevo usuario en la base de datos.
    """
    try:
        return crear_usuario(db, usuario)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/login", response_model=LoginResponse)
def login_usuario(usuario: LoginRequest, db: Session = Depends(get_db)):
    """
    Inicia sesión para un usuario y devuelve un token JWT.
    """
    usuario_db = autenticar_usuario(db, usuario.email, usuario.password)
    if not usuario_db:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    
    # Crear el token JWT
    token = create_access_token({"sub": str(usuario_db.id)})
    return {"access_token": token, "token_type": "bearer"}
