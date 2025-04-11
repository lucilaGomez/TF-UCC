import uuid
import enum
from datetime import datetime
from sqlalchemy import Column, String, Enum as SqlEnum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

# Base para todos los modelos
Base = declarative_base()

# Enum de tipos de usuario — DEBE coincidir con el schema
class TipoUsuario(str, enum.Enum):
    ADMIN = "ADMIN"
    EMPRESA = "EMPRESA"
    CANDIDATO = "CANDIDATO"

# Modelo de la tabla 'usuarios'
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    tipo = Column(SqlEnum(TipoUsuario), nullable=False)

    # Agregado para que coincida con el schema
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

