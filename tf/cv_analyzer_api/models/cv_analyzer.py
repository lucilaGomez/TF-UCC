from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from tf.database.session import Base
from ...user_api.models.user import Candidate

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