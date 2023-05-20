import sys
import time
import unittest
from os.path import abspath, dirname
from werkzeug.security import generate_password_hash, check_password_hash
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Add the parent directory to the Python path
sys.path.append(dirname(dirname(abspath(__file__))))

from app import db, app
from app.models import User, Chat, ChatPair

class SystemTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        print("=== === === setUpClass === === ===")
        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome('./chromedriver')
        cls.driver.implicitly_wait(60)
        cls.driver.maximize_window()
        if not cls.driver:
            cls.skipTest("Web browser not available")

    @classmethod
    def tearDownClass(cls):
        print("=== === === tearDownClass === === ===")
        try:
            if cls.driver:
                cls.driver.close()
        except Exception as e:
            print(f"An error occurred during WebDriver closure: {e}")

    def setUp(self):
        print("=== === === setUp === === ===")
        with app.app_context():
            db.create_all()

    def tearDown(self):
        print("=== === === tearDown === === ===")
        # Ensure logout is performed
        self.driver.get("http://127.0.0.1:5000/logout/")
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_first_visiting(self):
        """
        End-User Test Case 1 - First Time to Use BrewChat
        1. User visits the register page
        2. User inputs username, password
        3. User clicks the register button
        4. Assert that the page redirects to the login page
        5. User inputs username, password in login page
        6. User clicks the login button
        7. Assert that the page redirects to the index page
        """

        # Navigate to the register page
        self.driver.get("http://127.0.0.1:5000/register/")
        username = "Selenium_2"
        password = "Password1234"

        # Find the registration elements and fill in the details
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        confirm_password_field = self.driver.find_element(By.NAME, "confirm_password")

        register_button = self.driver.find_element(By.XPATH, "//button[text()='Register']")
        username_field.send_keys(username)
        password_field.send_keys(password)
        confirm_password_field.send_keys(password)

        # Submit the registration form
        register_button.click()

        # Wait until the registration process completes or any other specific condition is met
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be("http://127.0.0.1:5000/login/")) 

        # Assert that the page redirects to the login page
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:5000/login/")

        # Find the login elements and fill in the credentials
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.XPATH, "//button[text()='Log In']")
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the login form
        login_button.click()

        # Wait until the login process completes
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be("http://127.0.0.1:5000/index"))

        # Assert that the page redirects to the login page
        assert self.driver.current_url == "http://127.0.0.1:5000/index"

        with app.app_context():
            # Retrieve the user from the database based on the username
            user = User.query.filter_by(username=username).first()

        # Perform any additional checks or assertions based on the user data retrieved from the database
        assert user is not None  # Ensure the user exists in the database
        assert user.check_password(password)  # Validate the password using the User model's check_password method

    def test_existing_user_login(self):
        """
        End-User Test Case 2 - Login
        1. User visits the login page
        2. User inputs username, password
        3. User clicks the login button
        4. Assert that the page redirects to the index page
        """
        # Mock a user in the database
        existing_user = "Selenium_ABC"
        existing_password = "Password1234"
        with app.app_context():
            user_input_username = existing_user
            user_input_password = existing_password
            user = User(username=user_input_username, password_hash=generate_password_hash(user_input_password))
            db.session.add(user)
            db.session.commit() 

        # Navigate to the login page
        self.driver.get("http://127.0.0.1:5000/login/")

        # Find the login elements and fill in the credentials
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.XPATH, "//button[text()='Log In']")
        username_field.send_keys(existing_user)
        password_field.send_keys(existing_password)

        # Submit the login form
        login_button.click()

        # Wait until the login process completes
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be("http://127.0.0.1:5000/index"))

        # Assert that the page redirects to the index page
        assert self.driver.current_url == "http://127.0.0.1:5000/index"

        with app.app_context():
            # Retrieve the user from the database based on the username
            user = User.query.filter_by(username=existing_user).first()

        # Perform any additional checks or assertions based on the user data retrieved from the database
        assert user is not None  # Ensure the user exists in the database
        assert user.check_password(existing_password)  # Validate the password using the User model's check_password method


if __name__ == "__main__":
    unittest.main()
