from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from user_api.database.session import Base
from datetime import datetime, timezone

# ----- Candidate Model -----
class Candidate(Base):
    __tablename__ = "candidate"

    email = Column(String, primary_key=True)
    cv_file = Column(String)

    # Relación uno a uno con CVAnalyzed
    cv_analyzed = relationship("CVAnalyzed", back_populates="candidate", uselist=False)


# ----- CVAnalyzed Model -----
class CVAnalyzed(Base):

    __tablename__ = "CV_Analyzed"

    email = Column(String, ForeignKey("candidate.email"), primary_key=True)
    cv_file = Column(String)
    analysis_status = Column(String)
    skills = Column(Text)
    experience = Column(Text)
    education = Column(Text)
    analysis_summary = Column(Text)
    analysis_result = Column(Text)

    analysis_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    candidate = relationship("Candidate", back_populates="cv_analyzed")