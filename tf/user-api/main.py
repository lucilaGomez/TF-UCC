from fastapi import FastAPI
from dotenv import load_dotenv
from pathlib import Path
import sys

# Imports del propio user-api
from .routes import user_routes
from .database.session import Base, engine
from .models import user  # Import necesario para registrar modelos de usuario

# Agregar paths de APIs externas
base_path = Path(__file__).resolve().parents[1]
sys.path.append(str(base_path / "CV_Analyzer-api"))
sys.path.append(str(base_path / "Job_Opening-api"))
sys.path.append(str(base_path / "search-api"))

# Routers externos
from routes.cv_analyzer_routes import router as cv_analyzer_router
from routes.job_opening_routes import router as job_opening_router
from routes.search_routes import router as search_router  # si lo tenés implementado

# Configuración del entorno
dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

# Inicialización de la app
app = FastAPI(title="Plataforma Inteligente de Trabajo")

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir todos los routers
app.include_router(user_routes.router)             # /users/
app.include_router(cv_analyzer_router)             # /cv_analysis/
app.include_router(job_opening_router)             # /job_offers/
app.include_router(search_router)                  # /search/

# Endpoint base de prueba
@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la Plataforma Inteligente de Trabajo"}
