from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Event, EventRegistration, User
from dependencies import get_current_user
from email_utils import send_email

router = APIRouter(prefix="/events", tags=["Event Registration"])


@router.post("/{event_id}/register")
def register_for_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    event = db.query(Event).filter(Event.id == event_id, Event.approved == True).first()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    existing = db.query(EventRegistration).filter(
        EventRegistration.user_id == current_user.id,
        EventRegistration.event_id == event_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Already registered")

    registration = EventRegistration(
        user_id=current_user.id,
        event_id=event_id
    )

    db.add(registration)
    db.commit()

    # 📧 SEND EMAIL
    subject = f"Registration Confirmed: {event.title}"
    content = f"""
Hi {current_user.username},

You have successfully registered for the event:

📌 Event: {event.title}
📅 Date: {event.date}
📍 Location: {event.location}

Thank you for registering!
UNI Events Team
"""

    send_email(current_user.email, subject, content)

    return {"message": "Registered successfully"}
