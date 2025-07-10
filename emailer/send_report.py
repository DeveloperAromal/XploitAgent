import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def Send_email(receiver_email, subject, html_content, app_email, app_password):
    """
    Sends an HTML email with optional plain text fallback.

    Parameters:
        receiver_email (str): Recipient's email address
        subject (str): Subject line of the email
        html_content (str): Full HTML content to embed
        app_email (str): Sender's email address
        app_password (str): Sender's app password (Gmail/SMTP)
    """
    # Optional: define a fallback plain text version
    plain_text = "This email requires HTML support to view properly."

    message = MIMEMultipart("alternative")
    message["From"] = app_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(plain_text, "plain"))
    message.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(app_email, app_password)
            server.send_message(message)
        print(f"✅ Email sent to {receiver_email} successfully!")

    except Exception as e:
        print(f"❌ Error sending email: {e}")
