import secrets
import logging
from logging.handlers import RotatingFileHandler
from markupsafe import escape

from pydantic import BaseModel, ValidationError, validator

from flask import (Flask, redirect, render_template, request, session,
                   url_for, flash)


app = Flask(__name__)

# set the secret key.
app.secret_key = secrets.token_bytes(32)

# logging configuration
file_handler = RotatingFileHandler(
    filename='logs/app.log', maxBytes=10240, backupCount=10)
formatter = logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

# log application startup
app.logger.info('App startup')


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route("/account/")
def account():
    return render_template('account.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
