#!/usr/bin/env python2.7
__author__='axe.xu'
from email.mime.text import MIMEText
import smtplib,sys

[SMTP_SERVER,SENDER,PASSWORD,RECIPIENT,SUBJECT,MESSAGE] = sys.argv[1:7]

msg = MIMEText('<html><body>'+ MESSAGE +'</body></html>','html','utf-8')
msg['From'] = SENDER
msg['To'] = RECIPIENT
msg['Subject'] = SUBJECT

server = smtplib.SMTP(SMTP_SERVER, 25)
server.login(SENDER, PASSWORD)
server.sendmail(SENDER,RECIPIENT,msg.as_string())
server.quit()
