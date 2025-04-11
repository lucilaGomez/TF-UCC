from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

# Importaciones relativas que apuntan correctamente dentro del paquete user-api
from ..schemas.user import UsuarioCreate, UsuarioResponse, LoginRequest, LoginResponse
from ..services.user_service import crear_usuario, autenticar_usuario
from ..database.session import get_db
from ..auth.jwt import create_access_token

# Inicializamos el router de FastAPI para agrupar endpoints relacionados con "usuarios"
router = APIRouter()

# Endpoint para registro de usuarios
@router.post("/register", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    """
    Registra un nuevo usuario en la base de datos.
    
    - Recibe un esquema `UsuarioCreate` con los datos del nuevo usuario.
    - Usa la dependencia `get_db()` para obtener la sesión de base de datos.
    - Llama a la función `crear_usuario` del servicio para guardar el usuario.
    - Devuelve un esquema `UsuarioResponse` con los datos del usuario registrado.
    """
    try:
        return crear_usuario(db, usuario)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

# Endpoint para login de usuarios
@router.post("/login", response_model=LoginResponse)
def login_usuario(usuario: LoginRequest, db: Session = Depends(get_db)):
    """
    Inicia sesión para un usuario y devuelve un token JWT.
    
    - Recibe un esquema `LoginRequest` con email y password.
    - Usa `autenticar_usuario` para validar las credenciales.
    - Si son válidas, crea y retorna un JWT con `create_access_token`.
    - Si no lo son, devuelve un error 401 (no autorizado).
    """
    usuario_db = autenticar_usuario(db, usuario.email, usuario.password)
    if not usuario_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )
    
    token = create_access_token({"sub": str(usuario_db.id)})
    return {"access_token": token, "token_type": "bearer"}
