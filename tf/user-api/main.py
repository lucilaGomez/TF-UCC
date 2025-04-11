from fastapi import FastAPI
from dotenv import load_dotenv
from pathlib import Path

from .routes import user_routes
from .database.session import Base, engine
from .models import user  # Import necesario para registrar modelos

# Ruta al archivo .env dentro de la carpeta user-api
dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

# Inicialización de la app
app = FastAPI(title="API de Usuarios")

# Crear tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

# Incluir rutas de usuario
app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la API de Usuarios"}
