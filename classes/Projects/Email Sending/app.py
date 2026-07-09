# import required modules 
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Srerver configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "rajkumar.gariki7@gmail.com"
passkey = "okmxljbgmfypepgh"

def singleEmailSend(to_email:str, subject:str, body:str):
    msg = MIMEMultipart()
    msg['To'] = to_email
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))

    try:
        # start server
        server = SMTP(smtp_server,smtp_port)
        # start server
        server.starttls()
        # Login to server
        server.login(sender_email,passkey)
        # send email
        server.sendmail(from_addr=sender_email,to_addrs=to_email,msg=msg.as_string())
        server.quit()
        return f"Successfully email send to {to_email}"
    except Exception as e:
        return f"Failed to send email because :{e}"
to_email = input("Enter email address : ")
subject = input("Enter subject : ")
body = input("Enter email body : ")
# calling singleEmailSend
print(singleEmailSend(to_email,subject,body))
