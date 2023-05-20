import pytest
from app import app
from app.models import User
from flask_login import login_user, logout_user, current_user
from datetime import datetime, date


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False # Disable CSRF tokens in the Forms
    app.config['LOGIN_DISABLED'] = True  # Disable login requirement for testing

    with app.test_client() as client:
        yield client


def test_index_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    # Access the protected route with the logged-in user
    response = client.get('/')
    # Assert that the response is valid
    assert response.status_code == 200
    assert b'Welcome to BrewChat' in response.data
    assert b'About BrewChat' in response.data
    assert b'Contact us - Support and Feedback' in response.data


def test_login_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login/' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get('/login/')
    assert response.status_code == 200
    assert b'LOGIN' in response.data
    assert b'<input autocomplete="off" autofocus class="input-group" name="username" placeholder="Username" type="text" required>' in response.data
    assert b'<input class="input-group" name="password" placeholder="Password" type="password" required>' in response.data
    assert b'<button class="btn" type="submit">Log In</button>' in response.data


def test_register_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register/' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get('/register/')
    assert response.status_code == 200
    assert b'REGISTER' in response.data
    assert b'<input autocomplete="off" autofocus class="input-group" name="username" placeholder="Username" type="text" required>' in response.data
    assert b'<input class="input-group" name="password" placeholder="Password" type="password" required>' in response.data
    assert b'<input class="input-group" name="confirm_password" placeholder="Password Again" type="password" required>' in response.data
    assert b'<button class="btn" type="submit">Register</button>' in response.data


def test_memory_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/memory/' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get('/memory/')
    assert response.status_code == 200
    assert b'Message History' in response.data
    assert b'<form id="search-form">' in response.data
    assert b'<input  class="chat-box" type="text" name="query" placeholder="Search...">' in response.data
    assert b'<button type="submit" class="show-button" >Show memory</button>' in response.data
    assert b'<div id="search-results"></div>' in response.data
    assert b'<input id="keyword" class="chat-box" type="text" name="message" placeholder="Mark your message...">' in response.data
    assert b'<button id="mark-button" onclick="mark()" class="chat-button" type="submit">Mark</button>' in response.data


def test_eliza_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/eliza/' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get('/eliza/')
    assert response.status_code == 200
    assert b'Eliza' in response.data
    assert b'<form id="chat-form">' in response.data
    assert b'<input id="message" class="chat-box" type="text" name="message" placeholder="Type your message...">' in response.data
    assert b'<button onclick="sendMessage()" class="chat-button" type="submit">Send</button>' in response.data
    

def test_account_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/account/' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get('/account/')
    print(response.data)
    assert b'<button id="quoteButton" onclick="loadRandomQuote()">New Quote</button>' in response.data
    assert b'<button id="likequoteButton" onclick="likeQuote()">Like</button>' in response.data
    assert b'<h1>Account details</h1>' in response.data
    assert b'<form action="/account" method="post">' in response.data
    assert b'<td>Username</td>' in response.data
    assert b'<td>Date of Birth</td>' in response.data
    assert b'<td>Favorite Quote</td>' in response.data
    assert b'<button class="btn save-btn" id="save-btn" onclick="Save()"  type="submit">Save</button>' in response.data
    assert b'<button class="btn" id="edit-btn">Edit</button>' in response.data


# def test_post_eliza_page(client, logged_in_user):
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/eliza/' page is posted (POST)
#     THEN check that the response is valid
#     """
#     data = {'body': 'TSLA', 'response': '100', 'speaker': '100'}
    
#     with client: 
#         response = test_client.post('/eliza/', data=data, follow_redirects=True)
#         assert response.status_code == 200


# def test_post_account_page(client, logged_in_user):
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/account/' page is posted (POST)
#     THEN check that the response is valid
#     """
#     dob=datetime.strptime('2000-01-01', '%Y-%m-%d').date()
#     quote='test quote'
#     current_datetime=datetime.now().date()
#     with client:
#         response = test_client.post('/account/', dob=dob, quote=quote, current_datetime=current_datetime, follow_redirects=True)
#         assert response.status_code == 302
        
#         assert b'test quote' in response.data
#         assert b'2000-01-01' in response.data
#         assert current_datetime in response.data



# @pytest.fixture
# def client():
#     with app.test_client() as client:
#         with app.app_context():
#             db.create_all() 
#         yield client
#         with app.app_context():
#             db.drop_all()


# @pytest.fixture
# def logged_in_user(client):
#     # Create a user and log them in
#     user = User(username='testuser', password_hash='password123', date_of_birth=date(2000, 1, 1), quote='test quote')
#     with app.app_context():
#         db.session.add(user)
#         db.session.commit()
#         login_user(user)

#     # Return the logged-in user
#     yield user

#     # Log the user out
#     with app.test_request_context():
#         logout_user()


# @pytest.fixture(scope='module')
# def client():
#     app.config['TESTING'] = True
#     app.config['WTF_CSRF_ENABLED'] = False
#     app.config['LOGIN_DISABLED'] = True
#     client = app.test_client()

#     # Create a virtual user for testing
#     with app.app_context():
#         user = User.query.get(1)  # Replace with your own user query
#         login_user(user)
#         load_user(1)

#     yield client

    # logout_user()

#     @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     app.config['WTF_CSRF_ENABLED'] = False
#     app.config['LOGIN_DISABLED'] = True  # Disable login requirement for testing
#     client = app.test_client()

#     with app.app_context():
#         with app.test_request_context():
#             db.create_all()  # Create any necessary database tables

#             # Create a test user
#             user = User(id=1, name='Test User')
#             db.session.add(user)
#             db.session.commit()

#             yield client
#             db.session.remove()
#             db.drop_all()
    # # Create a user with a date_of_birth
    # user = User(name='John Doe', date_of_birth='1990-01-01')
    # db.session.add(user)
    # db.session.commit()

    # # Log in the user
    # login_user(user)

    # with app.test_request_context():
    #     # Create a user object
    #     test_current_user = User(id='1', username='testuser', quote='test quote', date_of_birth=date(2000, 1, 1), password_hash='password123')
                
    #     # Log in the test user and set the current_user
    #     login_user(test_current_user)
    #     logout_user()