from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    text: str

class CommentUpdate(BaseModel):
    text: str

class CommentOut(BaseModel):
    id: int
    report_id: int
    user_id: int
    text: str
    created_at: datetime

    class Config:
        orm_mode = True
