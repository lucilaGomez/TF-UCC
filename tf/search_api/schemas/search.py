from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SearchBase(BaseModel):
    query: str
    user_email: Optional[str] = None

class SearchCreate(SearchBase):
    pass

class SearchResponse(SearchBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
