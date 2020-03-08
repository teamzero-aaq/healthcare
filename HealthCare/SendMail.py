import smtplib
import ssl
from email.mime.text import MIMEText


def sendmail(receiver, title, msgbody, link):
    port = 465  # 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "shifakarol77@gmail.com"
    password = "Shifa@007"
    toaddrs = receiver

    msg = MIMEText("Click to chat " + link)
    msg['Subject'] = title
    msg['To'] = sender_email

    print(msg.as_string())
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, toaddrs, msg.as_string())


def sendmail1(receiver, title, msgbody):
    port = 465  # 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "shifakarol77@gmail.com"
    password = "Shifa@007"
    toaddrs = receiver

    msg = MIMEText(msgbody)
    msg['Subject'] = title
    msg['To'] = sender_email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, toaddrs, msg.as_string())
