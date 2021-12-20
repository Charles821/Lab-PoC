import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
SECRET_KEY = 'supersecretkey'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

DEBUG = True

MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USERNAME = 'callatelaboca821@gmail.com'
MAIL_PASSWORD = "qmfcajuirsvnmyiz"
MAIL_USE_TLS = False
MAIL_USE_SSL = True