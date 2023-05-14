from app import db
from app import login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# The user_loader decorator allows Flask-Login to load the current user and grab their id.
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# The UserMixin class provides default implementations for the methods that Flask-Login expects user objects to have.
# The db.Model class is the base class that SQLAlchemy uses to represent models.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
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
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    response = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # foreign key link with users database

    # The __repr__ method tells Python how to print objects of this class, which is going to be useful for debugging.
    def __repr__(self):
        return '<Chat {}>'.format(self.body)