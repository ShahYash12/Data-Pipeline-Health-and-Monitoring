import smtplib
from email.message import EmailMessage

def send_email(subject, body, to_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = "your_alerts@company.com"
    msg['To'] = to_email

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("user", "pass")
        server.send_message(msg)
