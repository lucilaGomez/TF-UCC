from fastapi import FastAPI
from .routes import user_routes
from database.session import Base, engine
import models.user  # Import necesario para registrar modelos
from user_api.routes import user_routes


app = FastAPI(title="API de Usuarios")

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la API de Usuarios"}
