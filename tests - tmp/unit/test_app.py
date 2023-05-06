from app import StockModel
import pytest
from pydantic import ValidationError


def test_validate_stock_data():
    """ 
        GIVEN a helper class to validate the form data
        WHEN the validate_stock_data is called
        THEN check the return value
    """
    stock_data = StockModel(
        ticker='TLSA',
        number_of_shares='100',
        price='105.54'
    )

    assert stock_data.ticker == 'TLSA'
    assert stock_data.number_of_shares == 100
    assert stock_data.price == 105.54


def test_validate_stock_data_invalid_ticker():
    """
    GIVEN a helper class to validate the form data
    WHEN the validate_stock_data is called with invalid ticker
    THEN check it raises a validation error
    """
    with pytest.raises(ValidationError):
        StockModel(
            ticker='TLSA1',
            number_of_shares='100',
            price='105.54'
        )


def test_validate_stock_data_invalid_number_of_shares():
    """
    GIVEN a helper class to validate the form data
    WHEN the validate_stock_data is called with invalid number of shares
    THEN check it raises a validation error
    """
    with pytest.raises(ValidationError):
        StockModel(
            ticker='TLSA',
            number_of_shares='100.5',
            price='105.54'
        )


def test_validate_stock_data_invalid_price():
    """
    GIVEN a helper class to validate the form data
    WHEN the validate_stock_data is called with invalid price
    THEN check it raises a validation error
    """
    with pytest.raises(ValidationError):
        StockModel(
            ticker='TLSA',
            number_of_shares='100',
            price='105.54.1'
        )


def test_validate_stock_data_missing_input():
    """
    GIVEN a helper class to validate the form data
    WHEN the validate_stock_data is called with missing input
    THEN check it raises a validation error
    """
    with pytest.raises(ValidationError):
        StockModel()


def test_validate_stock_data_missing_price():
    """
    GIVEN a helper class to validate the form data
    WHEN the validate_stock_data is called with missing price
    THEN check it raises a validation error
    """
    with pytest.raises(ValidationError):
        StockModel(
            ticker='TLSA',
            number_of_shares='100',
        )
