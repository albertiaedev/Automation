import smtplib

#some mail services require you to enable the security options for smtp

SENDER_EMAIL = ''
SENDER_PASSWORD = ''

#for this example we'll use gmail, which requires you to enable security settings for smtp

#Enable Security Settings in Gmail: Account Settings > Security > Less Secure App Access > ON

def send_email(receiver, subject, body):
    message = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver, message)
