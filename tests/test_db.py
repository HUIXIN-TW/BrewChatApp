import sys
import os
from os.path import abspath, dirname
import unittest
from datetime import datetime, date

# Add the parent directory to the Python path
sys.path.append(dirname(dirname(abspath(__file__))))

from app import db, app
from app.models import User, Chat, ChatPair


class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Set up the application context
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Clean up the database after testing
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_repr(self):
        # Create a user
        with app.app_context():
            user = User(username='testuser')
            db.session.add(user)
            db.session.commit()

            # Retrieve the user from the database and verify the __repr__ method
            retrieved_user = User.query.get(user.id)
            self.assertEqual(retrieved_user.__repr__(), '<User testuser>')

    def test_user_model(self):
        # Create a user and add it to the database
        with app.app_context():
            user = User(username='testuser')
            user.set_password('password1234')
            user.date_of_birth = datetime.strptime('1990-01-01', '%Y-%m-%d').date()
            user.quote = 'Test quote'
            db.session.add(user)
            db.session.commit()

            # Retrieve the user from the database and verify its properties
            retrieved_user = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(retrieved_user)
            self.assertEqual(retrieved_user.username, 'testuser')
            self.assertTrue(retrieved_user.check_password('password1234'))
            self.assertEqual(retrieved_user.date_of_birth, datetime.strptime('1990-01-01', '%Y-%m-%d').date())
            self.assertEqual(retrieved_user.quote, 'Test quote')

    def test_chat_model(self):
        # Create a chat and associate it with a user
        with app.app_context():
            user = User(username='testuser')
            chat = Chat(body='Hello', response='Hi there!', speaker=user)
            db.session.add(user)
            db.session.add(chat)
            db.session.commit()

            # Retrieve the chat from the database and verify its properties
            retrieved_chat = Chat.query.filter_by(body='Hello').first()
            self.assertIsNotNone(retrieved_chat)
            self.assertEqual(retrieved_chat.body, 'Hello')
            self.assertEqual(retrieved_chat.response, 'Hi there!')
            self.assertEqual(retrieved_chat.user_id, user.id)

    def test_chat_pair_model(self):
        # Create two users and a chat pair
        with app.app_context():
            user1 = User(username='user1')
            user2 = User(username='user2')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()

            chat_pair = ChatPair(user1_id=user1.id, user2_id=user2.id, chat_date=date(2023, 5, 20))
            db.session.add(chat_pair)
            db.session.commit()

            # Retrieve the chat pair from the database and verify its properties
            retrieved_chat_pair = ChatPair.query.filter_by(id=chat_pair.id).first()
            self.assertIsNotNone(retrieved_chat_pair)
            self.assertEqual(retrieved_chat_pair.user1_id, user1.id)
            self.assertEqual(retrieved_chat_pair.user2_id, user2.id)
            self.assertEqual(retrieved_chat_pair.chat_date, date(2023, 5, 20))

    def test_chat_relationships(self):
        # Create a user and multiple chats
        with app.app_context():
            user = User(username='testuser')
            chat1 = Chat(body='Hello', response='Hi there!', speaker=user)
            chat2 = Chat(body='How are you?', response='I am good!', speaker=user)
            db.session.add(user)
            db.session.add(chat1)
            db.session.add(chat2)
            db.session.commit()
        # Retrieve the user from the database and verify the chat relationships
            retrieved_user = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(retrieved_user)
            self.assertEqual(len(retrieved_user.chats.all()), 2)
            self.assertIn(chat1, retrieved_user.chats)
            self.assertIn(chat2, retrieved_user.chats)


if __name__ == '__main__':
    unittest.main()
