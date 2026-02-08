from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    title: str
    description: str
    date: datetime
    venue: str

class EventOut(EventCreate):
    id: int
    approved: bool
