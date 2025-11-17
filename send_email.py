import smtplib
import ssl
from email.message import EmailMessage

SENDER_EMAIL = "your.email@gmail.com"
SENDER_PASSWORD = "your-16-digit-app-password"
RECEIVER_EMAIL = "recipient.email@example.com"
EMAIL_SUBJECT = "Hello from Python!"
EMAIL_BODY = "This is an automated email sent from a Python script."
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def main():
    print("Preparing to send email...")
    msg = EmailMessage()
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg.set_content(EMAIL_BODY)
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            print(f"Email sent to: {RECEIVER_EMAIL}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
