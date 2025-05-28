from sqlalchemy import Column, Integer, String, DateTime, Text, Float
from sqlalchemy.orm import relationship
from datetime import datetime

from tf.database.session import Base


class JobOffer(Base):
    __tablename__ = "job_offer"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    company_email = Column(String)
    title = Column(String)
    description = Column(String)
    requirements = Column(String)
    location = Column(String)
    salary = Column(Float)
    publication_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    applications = relationship("Application", back_populates="job_offer")

print("✅ JobOffer cargado")
