from flask import request, Response
from api.model.Email import Email

class EmailView(object):
  
  @staticmethod
  def send_mail():
    
    payload = request.get_json()
    
    try:
      email = Email(payload['destination'])
      send = email.send_mail(payload['content'], payload['subject'])
    except Exception as e:
      return Response(e, status=400)
    
    return Response(send, status=200)
    