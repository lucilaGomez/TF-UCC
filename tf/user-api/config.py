from dotenv import load_dotenv
import os
from pydantic import BaseSettings

# Ruta absoluta del .env en user-api
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)  # Esto carga el .env manualmente

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = env_path  # Se puede dejar también para referencia

settings = Settings()
