from fastapi import FastAPI
from dotenv import load_dotenv
from pathlib import Path
import sys

# === PATHS para imports locales ===
base_path = Path(__file__).resolve().parent
sys.path.append(str(base_path / "cv_analyzer_api"))
sys.path.append(str(base_path / "job_opening_api"))
sys.path.append(str(base_path / "search_api"))
sys.path.append(str(base_path / "user_api"))

# === DOTENV ===
dotenv_path = base_path / ".env"
load_dotenv(dotenv_path=dotenv_path)

# === Inicializar app ===
app = FastAPI(title="Plataforma Inteligente de Trabajo")

# === Importar modelos para registrar relaciones ===
import tf.user_api.models.user           # Application, Candidate, etc.
import tf.job_opening_api.models.job_offer  # JobOffer

# === Base de datos ===
from sqlalchemy import text
from tf.database.session import Base, engine

# 🔥 SOLO PARA DESARROLLO: eliminar todas las tablas con CASCADE
with engine.connect() as conn:
    conn.execute(text("DROP SCHEMA public CASCADE"))
    conn.execute(text("CREATE SCHEMA public"))

# Crear nuevamente todas las tablas
Base.metadata.create_all(bind=engine)


# === Routers ===
from tf.cv_analyzer_api.routes.cv_analyzer_routes import router as cv_analyzer_router
from tf.job_opening_api.routes.job_opening_routes import router as job_opening_router
from tf.search_api.routes.search_routes import router as search_router
from tf.user_api.routes.user_routes import router as user_router
from tf.user_api.routes import profile_routes

# === Montar routers ===
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(cv_analyzer_router, prefix="/cv_analysis", tags=["CV Analyzer"])
app.include_router(job_opening_router, prefix="/job_offers", tags=["Job Offers"])
app.include_router(search_router, prefix="/search", tags=["Search"])
app.include_router(profile_routes.router, prefix="/profile", tags=["Profile"])
