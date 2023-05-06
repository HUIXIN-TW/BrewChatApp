from app import app
import pytest
from pydantic import ValidationError


def test_index_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b'<h1>Welcome Stocks Homepage</h1>' in response.data
        assert b'The followings are' in response.data
        assert b'my stocks' in response.data


def test_about_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/about/' page is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        response = test_client.get('/about/')
        assert response.status_code == 200
        assert b'<h1>About Page</h1>' in response.data
        assert b'Here is for class' in response.data
        assert b'Class name:' in response.data


def test_get_add_stock_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/add_stock/' page is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        response = test_client.get('/add_stock/')
        assert response.status_code == 200
        assert b'<h2>Add A Stock</h2>' in response.data
        assert b'<form method="post">' in response.data
        assert b'<input type="submit" value="submit" />' in response.data
        assert b'Stock Ticker <em>(required)</em>:' in response.data
        assert b'Number Of Shares <em>(required)</em>:' in response.data
        assert b'Price <em>(required)</em>:' in response.data


def test_post_add_stock_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/add_stock/' page is posted (POST)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        response = test_client.post('/add_stock/', data={
            'ticker': 'TSLA',
            'numberOfShares': '100',
            'price': '105.54'
        }, follow_redirects=True)
        assert response.status_code == 200

        assert b'<h1>List of Stocks</h1>' in response.data

        assert b'Ticker' in response.data
        assert b'Number of Shares' in response.data
        assert b'Price' in response.data

        assert b'TSLA' in response.data
        assert b'100' in response.data
        assert b'105.54' in response.data
