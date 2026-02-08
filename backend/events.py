from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
from event_schemas import EventCreate

from dependencies import get_current_user
from email_utils import send_email


router = APIRouter(tags=["Events"])


# 🔓 Public – anyone can view approved events
@router.get("/events")
def get_approved_events(db: Session = Depends(get_db)):
    return db.query(models.Event).filter(models.Event.approved == True).all()


# 🔐 Logged-in users can create events
@router.post("/events")
def create_event(
    event: EventCreate,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    new_event = models.Event(
        title=event.title,
        description=event.description,
        location=event.location,
        date=event.date,
        approved=False
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event


# 🔐 Admin-only – approve event
@router.post("/events/{event_id}/approve")
def approve_event(
    event_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only")

    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    event.approved = True

    # 🔔 Notification
    notification = models.Notification(
        message=f"Event '{event.title}' has been approved"
    )

    db.add(notification)
    db.commit()

    return {"message": "Event approved successfully"}


# 🔐 Student – register for event
@router.post("/events/{event_id}/register")
def register_for_event(
    event_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = user["user_id"]

    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event or not event.approved:
        raise HTTPException(status_code=404, detail="Event not available")

    existing = db.query(models.EventRegistration).filter(
        models.EventRegistration.user_id == user_id,
        models.EventRegistration.event_id == event_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Already registered")

    registration = models.EventRegistration(
        user_id=user_id,
        event_id=event_id
    )

    db.add(registration)
    db.commit()

    return {"message": "Registered successfully"}

@router.post("/events/{event_id}/register")
async def register_for_event(
    event_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = user["user_id"]

    event = db.query(models.Event).filter(
        models.Event.id == event_id,
        models.Event.approved == True
    ).first()

    if not event:
        raise HTTPException(status_code=404, detail="Event not available")

    existing = db.query(models.EventRegistration).filter_by(
        user_id=user_id,
        event_id=event_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Already registered")

    registration = models.EventRegistration(
        user_id=user_id,
        event_id=event_id
    )

    db.add(registration)
    db.commit()

    # 📧 EMAIL CONFIRMATION
    user_db = db.query(models.User).filter(models.User.id == user_id).first()

    await send_email(
        subject="Event Registration Confirmed 🎉",
        recipients=[user_db.email],
        body=f"""
        <h2>Registration Successful!</h2>
        <p>You are registered for:</p>
        <b>{event.title}</b><br/>
        📅 {event.date}<br/>
        📍 {event.venue}
        """
    )

    return {"message": "Registered successfully"}
