from app import app
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (Flask, redirect, render_template, request, session,
                   url_for, flash)
from flask_login import current_user, login_user, logout_user
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', [username])
        user = cursor.fetchone()  # returns the first row found
        if user and check_password_hash(user[2], password):
            # store the user's id in session
            session['id'] = user[0]
            # store the user's username in session
            session['username'] = username
            return redirect('/account/')
        else:
            error = 'Invalid username or password'
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')


@app.route('/logout/')
def logout():
    logout_user()
    return redirect('/login/')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', [username])
        user = cursor.fetchone()
        # if a user is found, we want to redirect back to signup page so user can try again
        if user:
            error = 'Username already exists'
            return render_template('login.html', error=error)
        else:
            # create the new user
            hashed_password = generate_password_hash(password, method='sha256')
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', [
                           username, hashed_password])
            conn.commit()
            # log the user in
            session['username'] = username
            session['id'] = cursor.lastrowid
            return redirect('/account/')
    else:
        return render_template('register.html')


@app.route("/account/")
def account():
    return render_template('account.html')
