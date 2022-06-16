"""CRUD operations."""
#functions that call the database


import schedule
import datetime
import time 
from model import db, User, JournalPrompt, JournalEntry, connect_to_db

def create_user(email, password, fname, lname):
    """Create and return a new user."""

    user = User(email = email, password = password, fname = fname, lname = lname)

    return user

def get_user_by_email(email):

    return User.query.filter_by(email = email).first()

def create_weekly_prompt(prompt, week):
    """Create and return a prompt"""
    
    weekly_prompt = JournalPrompt(prompt = prompt, week = week)

    return weekly_prompt

def get_prompt_by_week(week):
    """Create and return a prompt"""
    
    current_prompt = JournalPrompt.query.get(week)

    return current_prompt

    


if __name__ == '__main__':
    from server import app
    connect_to_db(app)