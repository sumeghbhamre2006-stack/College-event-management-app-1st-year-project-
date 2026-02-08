import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = "yourgmail@gmail.com"      # 👈 your gmail
SENDER_PASSWORD = "your_app_password"     # 👈 16-char app password


def send_email(to_email: str, subject: str, content: str):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(content)

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"📧 Email sent to {to_email}")
    except Exception as e:
        print("❌ Email sending failed:", e)
