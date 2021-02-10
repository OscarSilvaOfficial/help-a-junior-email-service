from email.mime.multipart import MIMEMultipart
from api.configs.enviroment import EMAIL_PASS
from email.mime.text import MIMEText
import smtplib


class Email(object):
  
  def __init__(self, receiver_address: str, mail_server='smtp.gmail.com', smtp_port=25):
    self.sender_address = 'oscarkaka222@gmail.com'
    self.sender_passwd = EMAIL_PASS
    self.receiver_address = receiver_address
    self.message = MIMEMultipart()
    self.mail_server = smtplib.SMTP(mail_server, smtp_port)
    
  def _create_massage(self, mail_content, subject):
    self.message['From'] = self.sender_address
    self.message['To'] = self.receiver_address
    self.message['Subject'] = subject
    self.message.attach(MIMEText(mail_content, 'plain'))
    
    return self.message
  
  def _define_auth(self):
    self.mail_server.connect("smtp.gmail.com", 587)
    try:
      self.mail_server.starttls()
    except Exception as e:
      print(e)
    
    try:
      self.mail_server.ehlo()
    except Exception as e:
      print(e)
      
    self.mail_server.login(self.sender_address, self.sender_passwd)
    
    return self.mail_server

  def send_mail(self, mail_content: str, subject: str):
    
    try:
      message = self._create_massage(mail_content, subject)
    except Exception as e:
      raise(e)
    
    try:
      mail_server = self._define_auth()
    except Exception as e:
      raise(e)
    
    try:
      text = message.as_string()
      mail_server.sendmail(self.sender_address, self.receiver_address, text)
    except Exception as e:
      raise(e)
    finally:
      mail_server.quit()
    return 'Email enviado'
  

""" import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = '''Hello,
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You
'''
#The mail addresses and password
sender_address = 'oscarkaka222@gmail.com'
sender_pass = 'pass'
receiver_address = 'junior-devq@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit() """