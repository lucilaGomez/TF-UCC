from sqlalchemy.orm import Session
from ..models.search import Search
from ..schemas.search import SearchCreate

def create_search(db: Session, search_data: SearchCreate) -> Search:
    new_search = Search(
        query=search_data.query,
        user_email=search_data.user_email
    )
    db.add(new_search)
    db.commit()
    db.refresh(new_search)
    return new_search

def get_all_searches(db: Session):
    return db.query(Search).order_by(Search.created_at.desc()).all()
