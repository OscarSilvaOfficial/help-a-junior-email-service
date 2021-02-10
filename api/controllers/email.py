from flask import jsonify, request, Response
from api.middlewares.application import ApplicationManager
from api.model.Email import Email


app = ApplicationManager().get_app()

class EmailView(object):
  def send_mail():
    email = Email('dondi8181@gmail.com')
    return email.send_mail('Fofaaaaaaaaaa', 'Cabecalho fofinho')
    