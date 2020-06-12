# Libraries to send a mail 
import smtplib, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Config.py file where the from_address, to_address, from_pass comes from
import config

# Basic mail format 
message = MIMEMultipart("alternative")
message["Subject"] = "Sample Mail" # Any subject
message["From"] = config.from_address
message["To"] = config.to_address

msg = "Test Message" # Any messsage 

msg_type = MIMEText(msg, "plain")
message.attach(msg_type)

# SMTP for Gmail (587 - Port for Gmail)
server = smtplib.SMTP("smtp.gmail.com", 587)
# Starting the server 
server.starttls()
server.login(config.from_address, config.from_pass)
# Started to send mail
server.sendmail(config.from_address, config.to_address, message.as_string())
# Mail Sent and quiting the server 
server.quit()