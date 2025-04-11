from datetime import datetime, timedelta
from jose import JWTError, jwt
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env si existe
load_dotenv()

# Clave secreta para firmar el JWT
SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Crea un token JWT codificado con una carga útil (payload).
    
    - `data`: información a incluir en el token (por ejemplo, {"sub": "usuario_id"})
    - `expires_delta`: tiempo de expiración personalizado (opcional)
    """
    to_encode = data.copy()

    # Establecer tiempo de expiración
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    # Codificar el token con clave secreta y algoritmo HS256
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    """
    Verifica y decodifica un token JWT.
    
    - Devuelve el payload decodificado si es válido.
    - Lanza excepción si el token es inválido o expirado.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise ValueError("Token inválido o expirado")
