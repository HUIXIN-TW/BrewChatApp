from datetime import date
from random import choice
from flask import session
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db, chatbot, socketio
from app.models import User, ChatPair


def generate_chat_pairs(users):
    # Check if the chat pair already exists for today
    existing_chat_pair = get_today_chat_pair()

    if existing_chat_pair:
        session['chat_pair_id'] = existing_chat_pair.id
        if existing_chat_pair.user1_id == current_user.id:
            random_user = User.query.filter_by(id=existing_chat_pair.user2_id).first()
        # If the chat pair already exists, then return the random user
        else:
            random_user = User.query.filter_by(id=existing_chat_pair.user1_id).first()
        return random_user


    # Retrieve all paired users
    paired_users = ChatPair.query.all()
    # Retrieve all user IDs from paired users
    paired_user_ids = [pair.user1_id for pair in paired_users] + [pair.user2_id for pair in paired_users]
    # Retrieve all users except the current user and paired users
    users = User.query.filter(User.id != current_user.id, ~User.id.in_(paired_user_ids)).all()
   
    if users:
        # Select a random user from the list
        random_user = choice(users)        
        try:
            # Generate and store a random user name for the current user
            chat_pair = ChatPair(user1_id=current_user.id, user2_id=random_user.id, chat_date=date.today())
            db.session.add(chat_pair)
            db.session.commit()
            session['chat_pair_id'] = chat_pair.id
            return random_user
        except Exception as e:
            # Handle the case when adding the quote fails
            db.session.rollback()
            print("Failed to generate chat pairs or no more users left")
            return None
    return None

def get_today_chat_pair():
    chat_pair = ChatPair.query.filter(
        ((ChatPair.user1_id == current_user.id)) |
        ((ChatPair.user2_id == current_user.id)),
        ChatPair.chat_date == date.today()
    ).first()
    print(f'==== chat_pair: {chat_pair} ====')
    return chat_pair