import sys
from os.path import abspath, dirname
import unittest
from datetime import datetime
from flask_login import login_user, logout_user, current_user
from flask_testing import TestCase

# Add the parent directory to the Python path
sys.path.append(dirname(dirname(abspath(__file__))))
from flask import current_app, session
from app import app
from app.models import User


class AppTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        # Set up the application context
        self.app_context = app.app_context()
        self.app_context.push()

        # Create a mock user and log them in
        date_of_birth = datetime.strptime('2000-01-01', '%Y-%m-%d').date()
        self.user = User(id=1, username='testuser', password_hash='password1234', date_of_birth=date_of_birth, quote='test quote')
        login_user(self.user)

        # Set up the necessary session data
        with self.client.session_transaction() as sess:
            sess['random_user_name'] = 'Friend'
            sess['chat_pair_id'] = 1

    def tearDown(self):
        # Log out the user after each test
        logout_user()

        # Remove the application context
        self.app_context.pop()

    def test_index_page(self):
        """
        Test that the '/' page is valid and contains expected content.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to BrewChat', response.data)
        self.assertIn(b'About BrewChat', response.data)
        self.assertIn(b'Contact us - Support and Feedback', response.data)
        self.assertEqual(current_user, self.user)

    def test_login_page(self):
        """
        Test that the '/login/' page is valid and contains expected content.
        """
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/', response.headers['Location'])


    def test_register_page(self):
        """
        Test that the '/register/' page is valid and contains expected content.
        """
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/', response.headers['Location'])

    
    def test_account_page(self):
        """
        Test that the '/account/' page is valid and contains expected content.
        """
        response = self.client.get('/account/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Account', response.data)
        self.assertIn(b'id="quoteButton"', response.data)
        self.assertIn(b'onclick="likeQuote()"', response.data)
        self.assertIn(b'id="quoteButton"', response.data)
        self.assertIn(b'onclick="likeQuote()"', response.data)
        self.assertIn(b'<h1 id="type-effect">Account details</h1>', response.data)
        self.assertIn(b'<form action="/account" method="post">', response.data)
        self.assertIn(b'<td>Username</td>', response.data)
        self.assertIn(b'<td>Date of Birth</td>', response.data)
        self.assertIn(b'<td>Favorite Quote</td>', response.data)
        self.assertIn(b'<button class="btn save-btn" id="save-btn" onclick="Save()" type="submit">', response.data)
        self.assertIn(b'<button class="btn" id="edit-btn">Edit</button>', response.data)
        self.assertEqual(current_user, self.user)

    
    def test_memory_page(self):
        """
        Test that the '/memory/' page is valid and contains expected content.
        """
        response = self.client.get('/memory/')
        content = response.data.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Message history', response.data)
        self.assertIn(b'<form id="search-form">', response.data)
        self.assertIn(b'<div id="search-results"></div>', response.data)
        self.assertIn(b'name="message"', response.data)
        self.assertIn(b'<button id="mark-button" onclick="mark()" class="chat-button" type="submit">', response.data)
        self.assertEqual(current_user, self.user)

    def test_eliza_page(self):
        """
        Test that the '/eliza/' page is valid and contains expected content.
        """
        response = self.client.get('/eliza/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Eliza', response.data)
        self.assertIn(b'<form id="chat-form">', response.data)
        self.assertIn(b'name="message"', response.data)
        self.assertIn(b'<button class="chat-button" type="submit">Send</button>', response.data)
        self.assertEqual(current_user, self.user)


    def test_chat_page(self):
        """
        Test that the '/chat/' page is valid and contains expected content.
        """    
        response = self.client.get('/chat/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Chat', response.data)
        self.assertIn(b'<button id="randomUserButton" class="btn">Show friend</button>', response.data)
        self.assertIn(b'id="text"', response.data)
        self.assertIn(b'Enter your message here', response.data)
        self.assertIn(b'<form id="text-form">', response.data)
        self.assertIn(b'<button type="submit" class="chat-button">Send</button>', response.data)
        self.assertEqual(current_user, self.user)


if __name__ == '__main__':
    unittest.main()