"""CRUD operations."""
#functions that call the database

from multiprocessing.context import ForkContext
from nturl2path import url2pathname
from flask import Blueprint
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
    # Do I even need this one? I have a seed.py for prompts
    
    weekly_prompt = JournalPrompt(prompt = prompt, week = week)

    return weekly_prompt

def ret_all_prompts():
    """Return all prompts that user has access to"""

    # WBN
    # if entry with prompt put check in front of url
    # if not then no check 

def get_prompt_by_week(week):
    """Create and return a prompt"""
   
    current_prompt = JournalPrompt.query.get(week)
    
    return current_prompt

def save_new_entry(user_id, week, user_entry, entry_date, visibility):

    entry = JournalEntry (user_id = user_id, week = week, user_entry = user_entry, entry_date = entry_date, visibility = visibility) 
    # entry = JournalEntry (user_entry = user_entry, entry_date = entry_date, entry_modified = entry_modified, modified_date = modified_date, visibility = visibility) 

    return entry

def get_entry_by_prompt():
    pass



if __name__ == '__main__':
    from server import app
    connect_to_db(app)