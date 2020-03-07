import smtplib
import ssl


def sendmail(receiver, title, msgbody):
    port = 465  # 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "shifakarol77@gmail.com"
    password = "Shifa@007"
    toaddrs = receiver
    message = "Subject:" + title + "\n" + msgbody
    print(message)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, toaddrs, message)
