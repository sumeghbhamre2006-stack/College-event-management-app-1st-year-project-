from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/notifications")
def get_notifications(db: Session = Depends(get_db)):
    return db.query(models.Notification).all()
