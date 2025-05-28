from pydantic import BaseModel, EmailStr, Field
from enum import Enum
from datetime import datetime, date
from typing import List, Optional

# ----- UserType Enum -----
class UserType(str, Enum):
    ADMIN = "ADMIN"
    COMPANY = "COMPANY"
    CANDIDATE = "CANDIDATE"

# ----- User Schemas -----
class UserBase(BaseModel):
    email: EmailStr
    user_type: UserType

class UserCreate(UserBase):
    password: str = Field(min_length=8)

class UserResponse(UserBase):
    creation_date: datetime
    update_date: datetime

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserListResponse(BaseModel):
    users: List[UserResponse]

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    user_type: Optional[UserType] = None
    password: Optional[str] = Field(default=None, min_length=8)

# ----- Person Schemas -----
class PersonBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    gender: Optional[str]
    birth_date: datetime
    address: Optional[str]

class PersonResponse(PersonBase):
    class Config:
        orm_mode = True

# ----- Candidate Schemas -----
class CandidateBase(BaseModel):
    email: EmailStr
    cv_file: Optional[str]

class CandidateResponse(CandidateBase):
    person: Optional[PersonResponse]
    class Config:
        orm_mode = True

# ----- Recruiter Schemas -----
class RecruiterBase(BaseModel):
    email: EmailStr
    company_email: EmailStr

class RecruiterResponse(RecruiterBase):
    class Config:
        orm_mode = True

# ----- Company Schemas -----
class CompanyBase(BaseModel):
    company_email: EmailStr
    company_name: str
    description: Optional[str] = None
    address: Optional[str] = None

class CompanyResponse(CompanyBase):
    recruiters: List[RecruiterResponse] = []
    class Config:
        orm_mode = True

class RegisterUserSchema(UserCreate):
    first_name: str
    last_name: str
    gender: Optional[str] = None
    birth_date: date
    address: Optional[str] = None

    class Config:
        orm_mode = True
        
# ----- Person Update Schema -----
class PersonUpdateSchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    birth_date: Optional[date]
    address: Optional[str]

    class Config:
        orm_mode = True

# ----- Company Update Schema -----
class CompanyUpdateSchema(BaseModel):
    company_name: Optional[str]
    description: Optional[str]
    address: Optional[str]

    class Config:
        orm_mode = True

class CandidateProfileResponse(BaseModel):
    email: EmailStr
    cv_file: Optional[str]
    person: Optional[PersonResponse]  
    
    # Usamos el schema que ya tenés para persona
    # análisis podría ir aquí cuando esté listo

    class Config:
        orm_mode = True