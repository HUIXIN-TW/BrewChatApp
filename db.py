import os
import sqlite3


# database connection
def connect_db():
    db_path = 'users.db'
    create_db = not os.path.exists(db_path)
    conn = sqlite3.connect(db_path)
    if create_db:
        create_usersdb(conn)
        populate_samples(conn)
    return conn


# create database
def create_usersdb(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)
    conn.commit()


# populate sample data
def populate_samples(conn):
    sample_users = [
        ('alice', '123456'),
        ('bob', 'password'),
        ('charlie', 'qwerty'),
        ('david', 'asdfgh'),
        ('eve', 'zxcvbn'),
        ('frank', '111111'),
        ('grace', '222222'),
        ('heidi', '333333'),
        ('ivan', '444444'),
        ('justin', '555555'),
        ('mallory', '666666'),
        ('olivia', '777777'),
        ('peggy', '888888'),
        ('steve', '999999'),
        ('trudy', '000000')
    ]
    with conn:
        conn.executemany(
            'INSERT INTO users (username, password) VALUES (?, ?)', sample_users)


# automatically create the users table if the database does not exist
connect_db()
