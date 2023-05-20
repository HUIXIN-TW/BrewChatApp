from app import app, db, chatbot, socketio
from datetime import datetime, date
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (Flask, redirect, render_template, request, session,
                   url_for, flash, jsonify)
from flask_login import current_user, login_user, logout_user, login_required
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from app.models import User, Chat, ChatPair, UserChat
from .handleStranger import generate_chat_pairs, get_today_chat_pair


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
##@login_required
def index():
    return render_template('index.html')


@app.route('/eliza/', methods=['GET', 'POST'])
@login_required
def eliza():
    current_datetime = datetime.now().date()
    if request.method == 'POST':
        message = request.form['message'].lower()
        response = chatbot.get_response(message)
        # Create a new Chat instance with the user input and chatbot response, and add it to the database.
        chat = Chat(body=message, response=response, speaker=current_user)
        db.session.add(chat)
        db.session.commit()
        return jsonify({'response': response})
    return render_template('eliza.html', current_datetime = current_datetime)


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
        session['tmpName'] = request.form['username']
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
        # Additional password validation: the password minimum length should be 6.
        if len(password) < 6:
            flash('Password should be at least 6 characters long.', category='danger')
            return redirect(url_for('register'))
        # Additional password validation: requiring both letters and digits
        if not any(char.isalpha() for char in password) or not any(char.isdigit() for char in password):
            flash('Password should contain both letters and digits', category='danger')
            return redirect(url_for('register'))

        # If the user does not exist, then the application will create a new user and add them to the database
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        session.clear()
        flash('Congratulations, you are now a registered user!', category='success')
        return redirect(url_for('login'))
    else:
        return render_template('register.html')


@app.route("/account/", methods=['GET', 'POST'])
@login_required
def account():
    if request.method == 'POST':
        try:
        # Get the updated values from the form
            dob_str = request.form['dob']
            favorite_quote = request.form['favorite_quote']
            
            # Convert dob_str to a date object
            dob = datetime.strptime(dob_str, '%Y-%m-%d').date()

            # Update the user's date of birth and favorite quote
            current_user.date_of_birth = dob
            current_user.quote = favorite_quote
            db.session.commit()
            flash('Account details updated successfully!', 'success')
        except Exception as e:
            # Handle the case when updating the account details fails
            db.session.rollback()
            flash('Failed to update account details.', 'error')
        return redirect(url_for('account'))
    
    # Get the current date
    current_datetime = datetime.now().date()
    
    # Get the current values from the database
    dob = current_user.date_of_birth
    quote = current_user.quote
    return render_template('account.html', dob=dob, quote=quote, current_datetime=current_datetime)


@app.route('/like_quote', methods=['POST'])
@login_required
def like_quote():
    # Get the quote from the request
    quote_data = request.get_json()
    quote = quote_data.get('quote')

    # Store the liked quote in the database
    current_user.quote = quote
    
    try:
        # Attempt to commit the changes to the database
        db.session.commit()
        # flash('Quote added successfully!', 'success')
        response = jsonify({'success': True})
    except Exception as e:
        # Handle the case when adding the quote fails
        db.session.rollback()
        # flash('Failed to add the quote.', 'error')
        response = jsonify({'success': False})

    return response


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


@app.route('/chat/')
@login_required
def chat():
    if session.get('random_user_name') is None:
        get_random_user()

    username = current_user.username
    # Check if the chat pair already exists for today
    if session.get('chat_pair_id') is None:
        session['chat_pair_id'] = get_today_chat_pair().id
    print(f'==== chat_pair_session: {session.get("chat_pair_id")} ====')

    room = session.get("chat_pair_id")
    print(f'==== room: {room} ====')

    return render_template('chat.html', username=username, room=room)


@app.route('/get_random_user')
@login_required
def get_random_user():
    print("==== get_random_user ====")
    random_user = generate_chat_pairs(current_user)
    if random_user:
        print(f'==== random_user: {random_user} ====')
        session['random_user_name'] = random_user.username
        return jsonify({'random_user_name': random_user.username})
    else:
        return jsonify({'random_user_name': None})


@socketio.on('join', namespace='/chat/')
def join(message):
    room = session.get("chat_pair_id")
    join_room(room)
    emit('status', {'msg': current_user.username + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat/')
def text(message):
    room = session.get("chat_pair_id")
    emit('message', {'msg': current_user.username + ':' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat/')
def left():
    room = session.get("chat_pair_id")
    leave_room(room)
    emit('status', {'msg': current_user.username + ' has left the room.'}, room=room)