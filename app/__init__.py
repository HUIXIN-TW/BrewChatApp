from flask import Flask
from config import Config
from .chatbot import ElizaChatbot
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


# print(dir(eliza))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']

# ['Chat', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
# 'demo', 'eliza_chat', 'eliza_chatbot', 'pairs', 'reflections']

# eliza demo
# eliza.demo()

# eliza initialization
# chatbot = eliza.Chat(eliza.pairs, eliza.reflections)
# chatbot.converse()

# chatbot initialization
chatbot = ElizaChatbot()


# avoid circular imports
from app import routes, models


if __name__ == '__main__':
    app.run(debug=True, port=5000)