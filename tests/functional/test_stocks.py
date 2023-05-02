from app import StockModel


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
