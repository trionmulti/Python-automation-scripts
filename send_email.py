import smtplib
import ssl
from email.message import EmailMessage

# --- CONFIGURATION ---

# 1. Email Credentials
#    (Get an "App Password" from Google, see instructions below)
SENDER_EMAIL = "your.email@gmail.com"
SENDER_PASSWORD = "your-16-digit-app-password"

# 2. Recipient
RECEIVER_EMAIL = "recipient.email@example.com"

# 3. Email Content
EMAIL_SUBJECT = "Hello from Python!"
EMAIL_BODY = """
This is an automated email sent from a Python script.
Have a great day!
"""

# 4. SMTP Server (for Gmail)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # For SSL

# ---------------------


def main():
    """
    Connects to the SMTP server and sends the email.
    """
    print("Preparing to send email...")

    # 1. Create the EmailMessage object
    msg = EmailMessage()
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg.set_content(EMAIL_BODY)

    # 2. Create a secure SSL context
    #    This ensures your connection is encrypted
    context = ssl.create_default_context()

    try:
        # 3. Connect to the server and log in
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            print("Connecting to email server...")
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            print("Login successful.")
            
            # 4. Send the email
            server.send_message(msg)
            print(f"\nEmail successfully sent to: {RECEIVER_EMAIL}")

    except smtplib.SMTPAuthenticationError:
        print("\nError: Authentication failed.")
        print("Please check your SENDER_EMAIL and SENDER_PASSWORD.")
        print("Did you use a 16-digit 'App Password'?")
    except smtplib.SMTPServerDisconnected:
         print("\nError: Server disconnected unexpectedly.")
    except Exception as e:
        # Catch other potential errors (e.g., connection timed out)
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
