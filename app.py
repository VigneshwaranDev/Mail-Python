import smtplib, time, config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

message = MIMEMultipart("alternative")
message["Subject"] = "Sample Mail"
message["From"] = config.from_address
message["To"] = config.to_address

msg = "Test Message"

msg_type = MIMEText(msg, "plain")
message.attach(msg_type)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(config.from_address, config.from_pass)
server.sendmail(config.from_address, config.to_address, message.as_string())
server.quit()