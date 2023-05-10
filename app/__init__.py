from flask import Flask
from config import Config
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


# login manager initialization
login = LoginManager(app)
login.login_view = 'login'


# avoid circular imports
from app import routes, models


if __name__ == '__main__':
    app.run(debug=True, port=5000)