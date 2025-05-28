from dotenv import load_dotenv
import os
from pydantic import BaseSettings

# Ruta absoluta del archivo .env en user_api
env_path = os.path.join(os.path.dirname(__file__), ".env")

# Cargar variables del .env para uso general (opcional pero recomendable)
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60  # Valor por defecto

    class Config:
        env_file = env_path
        env_file_encoding = 'utf-8'

# Crear instancia única para usar en toda la app
settings = Settings()

# Mensaje opcional para confirmar carga
print("Config loaded, DATABASE_URL:", settings.DATABASE_URL)
