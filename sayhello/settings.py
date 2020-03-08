import os
import sys

from sayhello import app

if sys.platform.startswith('win'):
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'db.sqlite')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', dev_db)
DEBUG_TB_INTERCEPT_REDIRECTS = False


