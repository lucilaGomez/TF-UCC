from fastapi import FastAPI
from dotenv import load_dotenv
from pathlib import Path
import sys

# Agregar paths de APIs externas (antes de importar)
base_path = Path(__file__).resolve().parents[1]
sys.path.append(str(base_path / "cv_analyzer_api"))
sys.path.append(str(base_path / "job_opening_api"))
sys.path.append(str(base_path / "search_api"))

# Import del propio user-api
from .routes import user_routes
from tf.database.session import Base, engine
from .models import user  # Import necesario para registrar modelos de usuario

# Routers externos
from tf.cv_analyzer_api.routes.cv_analyzer_routes import router as cv_analyzer_router
from tf.job_opening_api.routes.job_opening_routes import router as job_opening_router
from tf.search_api.routes.search_routes import router as search_router

# Configuración del entorno
dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

# Inicialización de la app
app = FastAPI(title="Plataforma Inteligente de Trabajo")

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir todos los routers
app.include_router(user_routes.router)
app.include_router(cv_analyzer_router)
app.include_router(job_opening_router)
app.include_router(search_router)

# Endpoint base de prueba
@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la Plataforma Inteligente de Trabajo"}
