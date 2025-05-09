from sqlalchemy import Column, String, Integer, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from user_api.database.session import Base
from datetime import datetime, timezone

class JobOpening(Base):
    __tablename__ = "job_opening"

    id_job_opening = Column(Integer, primary_key=True, index=True)
    email = Column(String, ForeignKey("reclutador.email"), nullable=False)
    company_email = Column(String, ForeignKey("empresa.email"), nullable=False)

    title = Column(String)
    description = Column(Text)
    requirements = Column(Text)
    location = Column(String)
    salary = Column(Float)

    publication_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    update_date = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    applications = relationship("Application", back_populates="job_opening")

    
