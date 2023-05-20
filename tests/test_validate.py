import sys
import os
from os.path import abspath, dirname
import unittest
from datetime import datetime, date
from flask import current_app
from flask_login import login_user, logout_user, current_user

# Add the parent directory to the Python path
sys.path.append(dirname(dirname(abspath(__file__))))

from app import db, app
from app.models import User, Chat, ChatPair


class TestAppRoutes(unittest.TestCase):
    def setUp(self):
        # Set up a test client and create a test database
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        # Clean up the test database
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_valid_login(self):
        # Test a valid login with correct credentials
        with self.app:
            # Create a test user
            username = 'testuser'
            password = 'testpassword123'
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            # Perform login with correct credentials
            response = self.app.post('/login/', data={'username': username, 'password': password}, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Welcome to BrewChat', response.data)
            self.assertIn(b'About BrewChat', response.data)
            self.assertIn(b'Contact us - Support and Feedback', response.data)
            self.assertTrue(current_user.is_authenticated)
            self.assertEqual(current_user.username, username)


    def test_invalid_login_wrong_password(self):
        with self.app:
            # Create a test user
            username = 'testuser'
            password = 'testpassword123'
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            wrong_password = 'pass_word_1234'

            # Perform login with correct credentials
            response = self.app.post('/login/', data={'username': username, 'password': wrong_password}, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Invalid username or password. Please try again.', response.data)
            self.assertFalse(current_user.is_authenticated)

    def test_invalid_login_nonexisting_user(self):
        # Test an invalid login with incorrect credentials
        with self.app:
            # Perform login with incorrect credentials
            response = self.app.post('/login/', data={'username': 'wronguser', 'password': 'wrongpassword'}, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Invalid username or password. Please try again.', response.data)
            self.assertFalse(current_user.is_authenticated)


if __name__ == '__main__':
    unittest.main()
