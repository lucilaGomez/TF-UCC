from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, status
from dotenv import load_dotenv
import os

# Cargar variables desde el archivo .env
load_dotenv()

# 🔐 Clave secreta y configuración
SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Crea un token JWT firmado con SECRET_KEY.

    Args:
        data (dict): Payload que se incluirá en el token (por ejemplo: {"sub": "usuario@email.com"})
        expires_delta (timedelta, optional): Tiempo de expiración personalizado. Si no se provee, se usa el valor por defecto.

    Returns:
        str: Token JWT firmado
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> dict:
    """
    Verifica la validez de un token JWT y devuelve su payload si es válido.

    Args:
        token (str): Token JWT a verificar.

    Raises:
        HTTPException: Si el token es inválido o ha expirado.

    Returns:
        dict: Payload decodificado del token.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"}
        )
