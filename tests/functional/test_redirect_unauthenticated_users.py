import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_protected_route(client):
    """
    GIVEN a Flask application configured for testing
    WHEN a protected route is accessed without a logged-in user
    THEN check that it redirects to the login page
    """
    # Access the protected route without a logged-in user
    response_index = client.get('/')
    response_account = client.get('/account/')
    response_memory = client.get('/memory/')
    response_chat = client.get('/chat/')
    response_eliza = client.get('/eliza/')
    
    # Assert that the response redirects to the login page
    assert response_index.status_code == 302
    assert response_account.status_code == 302
    assert response_memory.status_code == 302
    assert response_chat.status_code == 302
    assert response_eliza.status_code == 302

    assert '/login/' in response_index.location
    assert '/login/' in response_account.location
    assert '/login/' in response_memory.location
    assert '/login/' in response_chat.location
    assert '/login/' in response_eliza.location

