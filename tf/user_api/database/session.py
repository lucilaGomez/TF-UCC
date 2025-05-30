from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from tf.user_api import config

DATABASE_URL = config.settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
