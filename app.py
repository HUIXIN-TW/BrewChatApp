import secrets

from flask import (Flask, redirect, render_template, request, session,
                   url_for)
from markupsafe import escape

from pydantic import BaseModel, ValidationError, validator

app = Flask(__name__)

app.secret_key = secrets.token_bytes(32)


class StockModel(BaseModel):
    ticker: str
    number_of_shares: int
    price: float

    @validator('ticker')
    def stock_ticker_check(cls, v):
        if not v.isalpha() or len(v) > 5:
            raise ValidationError(
                'ticker must be 1-5 characters long and only contain letters')
        return v.upper()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about/")  # trailing slash
def about():
    return render_template('about.html', class_name='CITS5505')


@app.route("/example/", methods=['GET', 'POST'])
def example():
    return "<h3>Example</h3>"


@app.route("/hello/<name>/")
def hello(name):
    # escape is used to prevent XSS attacks
    return f"<h5>Hello, {escape(name)}!</h5>"


@app.route("/blog/<int:postID>/")
def show_blog(postID):
    return f"Blog Number: #{escape(postID)}"


@app.route('/add_stock/', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        for k, v in request.form.items():
            print(f'{k}: {v}')
        try:
            stock_data = StockModel(
                ticker=request.form['ticker'],
                number_of_shares=request.form['numberOfShares'],
                price=request.form['price']
            )
            print(stock_data)

            # save information in the session object
            session['ticker'] = stock_data.ticker
            session['numberOfShares'] = stock_data.number_of_shares
            session['price'] = stock_data.price

            return redirect(url_for('list_stock'))  # call list_stock function

        except ValidationError as e:
            print(e)

    return render_template('add_stock.html')


@ app.route('/stocks/')
def list_stock():
    return render_template('stocks.html')


@app.route('/button')
def button():
    return render_template("button.html", title="Button!")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
