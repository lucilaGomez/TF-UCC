import enum
from datetime import datetime
from sqlalchemy import Column, String, Enum as SqlEnum, DateTime, Integer, Float, Text, ForeignKey
from sqlalchemy.orm import relationship

from tf.database.session import Base
from tf.job_opening_api.models.job_offer import JobOffer

# ----- Enum para tipos de usuario -----
class UserType(str, enum.Enum):
    ADMIN = "ADMIN"
    COMPANY = "COMPANY"
    CANDIDATE = "CANDIDATE"

# ----- Modelos SQLAlchemy -----

class User(Base):
    __tablename__ = "user"

    email = Column(String, primary_key=True, index=True)
    password_hash = Column(String, nullable=False)
    user_type = Column(SqlEnum(UserType), nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Person(Base):
    __tablename__ = "person"

    email = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    birth_date = Column(DateTime)
    address = Column(String)

    candidate = relationship("Candidate", back_populates="person")

class Candidate(Base):
    __tablename__ = "candidate"

    email = Column(String, ForeignKey("person.email"), primary_key=True)
    cv_file = Column(String)

    person = relationship("Person", back_populates="candidate")
    cv_analyzed = relationship("CVAnalyzed", uselist=False, back_populates="candidate")
    applications = relationship("Application", back_populates="candidate")

class Company(Base):
    __tablename__ = "company"

    company_email = Column(String, primary_key=True, index=True)
    company_name = Column(String)
    description = Column(Text)
    address = Column(String)

    recruiters = relationship("Recruiter", back_populates="company")

class Recruiter(Base):
    __tablename__ = "recruiter"

    email = Column(String, primary_key=True)
    company_email = Column(String, ForeignKey("company.company_email"))

    company = relationship("Company", back_populates="recruiters")

class Application(Base):
    __tablename__ = "application"

    id_application = Column(Integer, primary_key=True, index=True)
    email = Column(String, ForeignKey("candidate.email"))
    job_offer_id = Column(Integer, ForeignKey("job_offer.id"))

    match_score = Column(Float)
    status = Column(String)
    application_date = Column(DateTime, default=datetime.utcnow)

    candidate = relationship("Candidate", back_populates="applications")
    job_offer = relationship("JobOffer", back_populates="applications")
