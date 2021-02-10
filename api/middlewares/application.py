from flask import Flask


class ApplicationManager(object):

  def __init__(self, app=Flask(__name__)):
    self._app = app

  def get_app(self):
    self._app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3307/junior_db'
    self._app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return self._app
