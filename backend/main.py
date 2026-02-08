from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine

import auth
import registrations
import events
import notifications
import event_registration

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # OK for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔑 REGISTER ROUTERS (THIS WAS MISSING)
app.include_router(auth.router)
app.include_router(registrations.router)
app.include_router(events.router)
app.include_router(notifications.router)
app.include_router(event_registration.router)

