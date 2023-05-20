import sys
from os.path import abspath, dirname
import unittest


# Add the parent directory to the Python path
sys.path.append(dirname(dirname(abspath(__file__))))
from app import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        """
        Create a test client
        """
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_index_redirects_to_login(self):
        """
        Test that accessing the index route without a logged-in user redirects to the login page.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.headers['Location'])
        

    def test_account_redirects_to_login(self):
        """
        Test that accessing the account route without a logged-in user redirects to the login page.
        """
        response = self.client.get('/account/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.headers['Location'])

    def test_memory_redirects_to_login(self):
        """
        Test that accessing the memory route without a logged-in user redirects to the login page.
        """
        response = self.client.get('/memory/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.headers['Location'])

    def test_chat_redirects_to_login(self):
        """
        Test that accessing the chat route without a logged-in user redirects to the login page.
        """
        response = self.client.get('/chat/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.headers['Location'])

    def test_eliza_redirects_to_login(self):
        """
        Test that accessing the eliza route without a logged-in user redirects to the login page.
        """
        response = self.client.get('/eliza/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.headers['Location'])

    def test_login_page(self):
        """
        Test that the '/login/' page is valid and contains expected content.
        """
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'LOGIN', response.data)
        self.assertIn(b'name="username"', response.data)
        self.assertIn(b'name="password"', response.data)
        self.assertIn(b'type="submit"', response.data)

    def test_register_page(self):
        """
        Test that the '/register/' page is valid and contains expected content.
        """
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'REGISTER', response.data)
        self.assertIn(b'name="username"', response.data)
        self.assertIn(b'name="password"', response.data)
        self.assertIn(b'name="confirm_password"', response.data)
        self.assertIn(b'type="submit"', response.data)


if __name__ == '__main__':
    unittest.main()
