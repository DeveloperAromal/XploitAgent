import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(receiver_email, subject, report_file_path, app_email, app_password):

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
        # Connect to SMTP server (example: Gmail SMTP)
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure connection
            server.login(app_email, app_password)
            server.send_message(message)

        print(f"Email sent to {receiver_email} successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")
        
    receiver_email=""
    subject=""
    report_file_path=".reporting.report_maker.py"
    app_email="geethaniya42@gmail.com"
    app_password="twpe heeh hamp adva"
    

