import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    
    def __init__(self):
        self.message = f"Subject:Cheap Flight ALERT!! \n"
        self.html_message = ""
        self.my_email = "dawid.python.study@gmail.com"
        self.password = "uyja fkuy zero vlmu"
        self.send_to = ["dawid7c@gmail.com", "aga.kowalikk94@gmail.com "]

    def send_message(self):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email, to_addrs=self.send_to, msg=self.message.encode('utf-8'))

    def reset_message(self):
        self.message = f"Subject:Cheap Flight ALERT!! \n"
    
    def send_html_message(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = "Cheap Flight ALERT!!"
        message["From"] = "dawid.python.study@gmail.com"
        message["To"] = "dawid7c@gmail.com"
        message.attach(MIMEText(self.html_message, "html"))
        
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email, to_addrs=self.send_to, msg=message.as_string())