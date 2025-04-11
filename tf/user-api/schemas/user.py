from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from enum import Enum
from datetime import datetime

class TipoUsuario(str, Enum):
    ADMIN = "ADMIN"
    EMPRESA = "EMPRESA"
    CANDIDATO = "CANDIDATO"

class UsuarioBase(BaseModel):
    email: EmailStr
    tipo: TipoUsuario

class UsuarioCreate(UsuarioBase):
    password: str = Field(min_length=8)

class UsuarioResponse(UsuarioBase):
    id: UUID
    fecha_creacion: datetime

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
