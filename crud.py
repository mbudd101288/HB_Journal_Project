"""CRUD operations."""
#functions that call the database

from multiprocessing.context import ForkContext
from nturl2path import url2pathname
from flask import Blueprint, jsonify, session
import schedule
from datetime import datetime
import time
from model import db, User, JournalPrompt, JournalEntry, connect_to_db


def create_user(email, password, fname, lname, sign_up, profile_pic):
    """Create and return a new user."""

    user = User(email = email, password = password, fname = fname, lname = lname, sign_up = sign_up, profile_pic = profile_pic)

    return user

def get_user_by_email(email):

    return User.query.filter_by(email = email).first()

def get_user_by_id(id):

    return User.query.get(id)

def create_weekly_prompt(prompt, week, book, bonus_text):
    """Create and return a prompt"""
    # Do I even need this one? I have a seed.py for prompts
    
    weekly_prompt = JournalPrompt(prompt = prompt, week = week, book = book, bonus_text = bonus_text)

    return weekly_prompt

def get_all_prompts():
    
    
    prompts = JournalPrompt.query.all()
    json = []
    for prompt in prompts:
        prompt_dict = {
            "week": prompt.week,
            "prompt": prompt.prompt,
            "book": prompt.book,
            "bonus_text":prompt.bonus_text
        }
        json.append(prompt_dict)
    return json

    # WBN
    # if entry with prompt put check in front of url
    # if not then no check 

def prompts_available_to_user(user_id):
    """Return all prompts that user has access to"""
    
    user = User.query.get(user_id)

    current_week = session['week']
    sign_up_week = datetime.strftime(user.sign_up, ("%U"))

    available_prompts= JournalPrompt.query.filter((JournalPrompt.week >= sign_up_week) & (JournalPrompt.week <= current_week)).all()

    return available_prompts

def prompts_available_to_user_json(user_id):
    """Return all prompts that user has access to"""
    
    user = User.query.get(user_id)
    
    current_week = session['week']
    sign_up_week = datetime.strftime(user.sign_up, ("%U"))

    available_prompts= JournalPrompt.query.filter((JournalPrompt.week >= sign_up_week) & (JournalPrompt.week <= current_week)).all()
    json = []
    for prompt in available_prompts:
        prompt_dict = {
            "week": prompt.week,
            "prompt": prompt.prompt,
            "book": prompt.book,
            "bonus_text":prompt.bonus_text
        }
        json.append(prompt_dict)
    return json
    

def get_prompt_by_week(week):
    """Create and return a prompt"""
   
    current_prompt = JournalPrompt.query.get(week)
    
    return current_prompt

def save_new_entry(user_id, week, user_entry, entry_date, entry_modified, modified_date, visibility):

    entry = JournalEntry(user_id = user_id, week = week, user_entry = user_entry, entry_date = entry_date, entry_modified = entry_modified, modified_date = modified_date, visibility = visibility) 
    # entry = JournalEntry (user_id = user_id, week = week, user_entry = user_entry, entry_date = entry_date, visibility = visibility) 
    return entry


def get_all_user_entries(user_id):
    
    all_entries = JournalEntry.query.filter(JournalEntry.user_id == user_id).all()

    return all_entries


def get_public_entries():

    public = JournalEntry.query.filter(JournalEntry.visibility == 'Public').all()

    return public 

def get_public_entries_json():

    
    public_entry = JournalEntry.query.filter(JournalEntry.visibility == 'Public').all()
    
    json = []
    for entry in public_entry:
        entry_dict = {
            "fname": entry.user.fname, 
            "user_id":entry.user.id,
            "entry": entry.user_entry,
            "week": entry.week,
            "prompt": entry.prompt.week,
            "visibility": entry.visibility
        }
        json.append(entry_dict)
    print(json)
    return json

def delete_journal_entry(entry_id):

    entry = JournalEntry.query.get(entry_id)

    db.session.delete(entry)
    db.session.commit()




if __name__ == '__main__':
    from server import app
    connect_to_db(app)