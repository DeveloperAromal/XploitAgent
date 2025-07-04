import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def Send_email(receiver_email, subject, report_file_path, app_email, app_password):
    """
    Send an email with a report as the body.

    Parameters:
        receiver_email (str): The recipient's email address.
        subject (str): The subject line of the email.
        report_file_path (str): Path to the file containing the report text.
        app_email (str): Your app's email address (SMTP account).
        app_password (str): The app email password (or app password if using Gmail).
    """

    # Read report content from file
    with open(report_file_path, 'r', encoding='utf-8') as file:
        report_body = file.read()

    # Create the email message
    message = MIMEMultipart()
    message['From'] = app_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(report_body, 'plain'))

    try:
        # Connect to SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(app_email, app_password)
            server.send_message(message)

        print(f"Email sent to {receiver_email} successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")

# ===========================
# 🔥 Here you type the actual values
# ===========================

receiver_email = "sajuniya111@gmail.com"
subject = "Weekly Project Report"
report_file_path = "reporting/report_maker.py"  # The file must exist with your content

# Your app's email credentials
app_email = "geethaniya42@gmail.com"
app_password = "twpe heeh hamp adva"  # Ideally store in env or config

# Send the email
Send_email(receiver_email, subject, report_file_path, app_email, app_password)


