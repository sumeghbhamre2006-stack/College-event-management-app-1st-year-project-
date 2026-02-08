# College-event-management-app-1st-year-project-
FY B.Tech personal project
# 🎓 College Event Management System

A full-stack web application that helps colleges manage events efficiently.  
Students can register for events, admins can approve events and view registrations, and users receive email confirmations on successful registration.

---

## ✨ Features

### 👤 User Authentication
- User registration and login
- JWT-based authentication
- Secure password hashing

### 📅 Event Management
- Create events (admin/host)
- Approve events (admin)
- View approved events (students)

### 📝 Event Registration
- Students can register for events
- Duplicate registration prevention
- View “My Registered Events”

### 📧 Email Notifications
- Automatic email confirmation after event registration
- Gmail SMTP integration using App Passwords

### 📊 Admin Dashboard
- View registered students for each event
- Monitor event participation

---

## 🛠 Tech Stack

### Backend
- **FastAPI**
- **SQLAlchemy**
- **JWT Authentication**
- **SQLite**
- **SMTP (Gmail)**

### Frontend
- **HTML**
- **CSS**
- **JavaScript**

---

## 📂 Project Structure

College-event-management-app/
│
├── backend/
│ ├── auth.py
│ ├── database.py
│ ├── dependencies.py
│ ├── email_utils.py
│ ├── event_registration.py
│ ├── event_schemas.py
│ ├── events.py
│ ├── jwt_utils.py
│ ├── main.py
│ ├── models.py
│ ├── notifications.py
│ ├── registrations.py
│ ├── user_schemas.py
│ └── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── login.html
│ ├── student_register.html
│ ├── student_dashboard.html
│ ├── admin_dashboard.html
│ ├── host_event.html
│ └── styles.css
│
├── .gitignore
└── README.md

##  How to Run the Project

## Backend Setup

bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload

Backend will run at:http://127.0.0.1:8000

 Frontend Setup

Open any HTML file from the frontend/ folder directly in a browser
(example: login.html).

 Email Configuration

Email confirmation is sent when a user registers for an event.

To enable email:

Use a Gmail account

Enable 2-Step Verification

Create a Gmail App Password

Update email_utils.py:

SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"

 Security Practices

Passwords are hashed using bcrypt

JWT tokens are used for protected routes

Sensitive files are excluded using .gitignore

 API Highlights

POST /auth/register – Register user

POST /auth/login – Login user

GET /events – View approved events

POST /events/{event_id}/register – Register for event

GET /users/{user_id}/registrations – View registered events

GET /events/{event_id}/registrations – Admin view

 Academic Relevance

This project demonstrates:

Full-stack development

REST API design

Authentication & authorization

Database relationships

Real-world email integration

Secure version control practices

 Author

Sumegh Bhamre
1st Year Engineering Student

 Future Enhancements

Event reminder emails

Role-based admin control

Deployment on cloud (Render / Railway)

Mobile-friendly UI
