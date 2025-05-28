from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

# Correcta importación de la instancia settings
from tf.user_api.config import settings  # Importamos settings directamente

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# 🔐 Clave secreta y configuración desde config.py
SECRET_KEY = settings.SECRET_KEY  # Usamos la instancia settings para acceder a SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES  # Usamos settings también aquí

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Crea un token JWT firmado con SECRET_KEY.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> dict:
    """
    Verifica y decodifica un token JWT.
    """
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"}
        )

def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Extrae el payload del usuario a partir del token JWT.
    """
    return verify_token(token)
