from email.mime.multipart import MIMEMultipart
from api.configs.enviroment import EMAIL_PASS, EMAIL_ACCOUNT
from email.mime.text import MIMEText
import smtplib, logging


class Email(object):
  
  def __init__(self, receiver_address: str, mail_server='smtp.gmail.com', smtp_port=25):
    self.__sender_address = EMAIL_ACCOUNT
    self.__sender_passwd = EMAIL_PASS
    self.__receiver_address = receiver_address
    self.__message = MIMEMultipart()
    self.__mail_server = smtplib.SMTP(mail_server, smtp_port)
    
  def __create_massage(self, mail_content, subject):
    self.__message['From'] = self.__sender_address
    self.__message['To'] = self.__receiver_address
    self.__message['Subject'] = subject
    self.__message.attach(MIMEText(mail_content, 'plain'))
    
    return self.__message
  
  def __define_auth(self):
    self.__mail_server.connect("smtp.gmail.com", 587)
    try:
      self.__mail_server.starttls()
    except Exception as e:
      raise e
    
    try:
      self.__mail_server.ehlo()
    except Exception as e:
      raise e
      
    self.__mail_server.login(self.__sender_address, self.__sender_passwd)
    
    return self.__mail_server

  def send_mail(self, mail_content: str, subject: str):
    
    try:
      message = self.__create_massage(mail_content, subject)
    except Exception as e:
      logging.error(e)
      return 'Erro ao criar mensagem'
    
    try:
      mail_server = self.__define_auth()
    except Exception as e:
      logging.error(e)
      return 'Erro ao fazer autenticação com os servidores'
    
    try:
      text = message.as_string()
      mail_server.sendmail(self.__sender_address, self.__receiver_address, text)
    except Exception as e:
      logging.error(e)
      return 'Erro ao enviar mensagem'
    finally:
      mail_server.quit()
      
    return 'Email enviado'