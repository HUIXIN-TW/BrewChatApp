import os
import secrets


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Flask-SECRET-KEY configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_bytes(32)
    # Flask-SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
