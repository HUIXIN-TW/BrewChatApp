from flask import Flask
from config import Config
from logging.handlers import RotatingFileHandler
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# Flask initialization
app = Flask(__name__)


# Flask configuration
app.config.from_object(Config)


# Flask-SQLAlchemy and Flask-Migrate initialization
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# avoid circular imports
from app import routes, models


# login manager initialization
login = LoginManager(app)


# log errors to file
file_handler = RotatingFileHandler(
    filename='logs/app.log', maxBytes=10240, backupCount=10)
formatter = logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


# log startup
app.logger.info('App startup')


if __name__ == '__main__':
    app.run(debug=True, port=5000)