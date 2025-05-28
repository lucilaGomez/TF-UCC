from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..schemas.search import SearchCreate, SearchResponse
from ..services.search_service import create_search, get_all_searches
from tf.database.session import get_db

router = APIRouter(
    prefix="/searches",
    tags=["Searches"]
)

@router.post("/", response_model=SearchResponse, status_code=status.HTTP_201_CREATED)
def create_search_route(search: SearchCreate, db: Session = Depends(get_db)):
    return create_search(db, search)

@router.get("/", response_model=list[SearchResponse])
def get_all_searches_route(db: Session = Depends(get_db)):
    return get_all_searches(db)
