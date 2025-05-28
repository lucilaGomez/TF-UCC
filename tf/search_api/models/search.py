from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from tf.database.session import Base

class Search(Base):
    __tablename__ = "searches"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(String, nullable=False)
    user_email = Column(String, nullable=True)  # Si querés registrar qué usuario hizo la búsqueda (opcional)
    created_at = Column(DateTime, default=datetime.utcnow)
