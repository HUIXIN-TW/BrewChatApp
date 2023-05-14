from app import app, db, chatbot

from werkzeug.security import generate_password_hash, check_password_hash
from flask import (Flask, redirect, render_template, request, session,
                   url_for, flash, jsonify)
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Chat

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        message = request.form['message']
        response = chatbot.get_response(message)
        # Create a new Chat instance with the user input and chatbot response, and add it to the database.
        chat = Chat(body=message, response=response, speaker=current_user)
        db.session.add(chat)
        db.session.commit()
        return jsonify({'response': response})
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # If the user is already logged in, then there is no need to show them the login page; 
    # instead, the application should redirect them to the main page.
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # query the database to see if the user exists
        user = User.query.filter_by(username=username).first()
        # If the user does not exist or if the password is wrong, then the application will flash a message
        if user is None or not user.check_password(password):
            flash(message='Invalid username or password. Please try again.', category='danger')
            return redirect(url_for('login'))

        # If the user does exist and the password is correct, then the user is considered logged in
        # login_user function from Flask-Login will keep track of the user.
        login_user(user, remember=True)

        # print(current_user.id, current_user.username, current_user.email, current_user.password_hash)
        
        # If the user navigates to /index, for example, the @login_required decorator will intercept the 
        # request and respond with a redirect to /login, but it will add a query string argument to this 
        # URL, making the complete redirect URL /login?next=/index. The next query string argument is set 
        # to the original URL, so the application can use that to redirect back after login.
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    else:
        return render_template('login.html')


@app.route('/logout/')
def logout():
    # The logout_user function will remove the user ID from the session.
    logout_user()
    return redirect('/login/')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    # If the user is already logged in, then there is no need to show them the register page;
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        # check if the password and confirm password are the same
        if password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('register'))
        # check if the username already exists
        user = User.query.filter_by(username=username).first()
        # If the user does exist, then the application will flash a message
        if user:
            flash('Username already exists. Please choose a different username.', category='danger')
            return redirect(url_for('register'))

        # If the user does not exist, then the application will create a new user and add them to the database
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', category='success')
        return redirect(url_for('login'))
    else:
        return render_template('register.html')


@app.route("/account/")
@login_required
def account():
    return render_template('account.html')


# @app.route('/chatbot/', methods=['GET', 'POST'])
# @login_required
# def chatbot_response():
#     if request.method == 'POST':
#         message = request.form['message']
#         response = chatbot.get_response(message)
#         # Create a new Chat instance with the user input and chatbot response, and add it to the database.
#         chat = Chat(body=message, response=response, speaker=current_user)
#         db.session.add(chat)
#         db.session.commit()
#         return jsonify({'response': response})
#     return render_template('chatbot.html')

@app.route('/memory/', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        # check if 'query' parameter exists in form data
        if 'query' in request.form:
            query = request.form['query']
            # process the search query and return the results
            results = Chat.query.filter(Chat.user_id == current_user.id, Chat.body.ilike(f"%{query}%")).order_by(Chat.timestamp.asc()).all()
            if results:
                return jsonify({'results': [{'body': r.body, 'response': r.response, 'timestamp': r.timestamp} for r in results]})
            else:
                return jsonify({'error': 'No results found'})
        else:
            # 'query' parameter is missing from form data
            return jsonify({'error': 'Missing query parameter'})
    return render_template('memory.html')
