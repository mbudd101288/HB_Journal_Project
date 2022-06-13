"""CRUD operations."""
#functions that call the database


import schedule
import time 
from model import db, User, JournalPrompt, JournalEntry, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def get_user_by_email(email):

    return User.query.filter_by(email=email).first()

def show_prompt():
    """Display prompt on user page scheduled weekly"""

    


if __name__ == '__main__':
    from server import app
    connect_to_db(app)