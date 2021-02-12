from api.middlewares.application import ApplicationManager
from api.controllers.email import EmailView


app = ApplicationManager().app

app.add_url_rule('/send_mail', 'send_mail', EmailView.send_mail, methods=['POST'])