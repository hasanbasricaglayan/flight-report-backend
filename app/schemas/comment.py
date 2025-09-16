from pydantic import BaseModel, ConfigDict
from datetime import datetime

class CommentCreate(BaseModel):
    text: str

class CommentUpdate(BaseModel):
    text: str

class CommentOut(BaseModel):
    model_config = ConfigDict(from_attributes = True)

    id: int
    report_id: int
    user_id: int
    text: str
    created_at: datetime
