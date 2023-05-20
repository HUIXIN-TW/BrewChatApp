from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
import pytz

# The user_loader decorator allows Flask-Login to load the current user and grab their id.
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# The UserMixin class provides default implementations for the methods that Flask-Login expects user objects to have.
# The db.Model class is the base class that SQLAlchemy uses to represent models.
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    date_of_birth = db.Column(db.Date)
    quote = db.Column(db.String(250))
    chats = db.relationship('Chat', backref='speaker', lazy='dynamic')

    # The __repr__ method tells Python how to print objects of this class, which is going to be useful for debugging.
    def __repr__(self):
        return '<User {}>'.format(self.username)

    # The password_hash field is a String field, which is limited to 128 characters.
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # The check_password method is a helper function that will return True if the password entered by the user
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# The Chat class represents individual chat messages. Each chat message links back to the user who sent it.
class Chat(db.Model):
    __tablename__ = 'robot_chats'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    response = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime(timezone=True), index=True, default=datetime.now(pytz.timezone('Australia/Perth')))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # The __repr__ method tells Python how to print objects of this class, which is going to be useful for debugging.
    def __repr__(self):
        return '<Chat {}>'.format(self.body)

class ChatPair(db.Model):
    __tablename__ = 'chat_pairs'

    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user2_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    chat_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<ChatPair {}>'.format(self.id)
