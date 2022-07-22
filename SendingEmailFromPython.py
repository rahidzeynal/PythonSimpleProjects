import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os

# mail server parameters
smtpHost = "smtp.gmail.com"
smtpPort = 587
mailUname = 'senderemail@gmail.com'
mailPwd = 'GmailAppPassword'
fromEmail = 'senderemail@gmail.com'

# mail body, recepients, attachment files
mailSubject = 'Test mail from python, please ignore'
mailContext = "Hi, Hope you are fine."
recepientsMailList = ["receiveremail@gmail.com"]


def sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail, mailSubject, mailContext, recepientsMailList):
    # create message object
    msg = MIMEText(mailContext)
    msg['From'] = fromEmail
    msg['To'] = ','.join(recepientsMailList)
    msg['Subject'] = mailSubject
    
    # Send message object as email using smtplib
    s = smtplib.SMTP(smtpHost, smtpPort)
    s.starttls()
    s.login(mailUname, mailPwd)
    msgText = msg.as_string()
    sendErrs = s.sendmail(fromEmail, recepientsMailList, msgText)
    s.quit()

    # check if errors occured and handle them accordingly
    if not len(sendErrs.keys()) == 0:
        raise Exception("Errors occured while sending email", sendErrs)

sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail, 
            mailSubject, mailContext, recepientsMailList)
print("Execution complete...")

