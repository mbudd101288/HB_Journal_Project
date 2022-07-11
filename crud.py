"""CRUD operations."""
#functions that call the database

from multiprocessing.context import ForkContext
from nturl2path import url2pathname
from flask import Blueprint, jsonify, session
import schedule
from datetime import datetime
import time
from model import db, User, JournalPrompt, JournalEntry, connect_to_db


def create_user(email, password, fname, lname, sign_up, profile_pic, twilio_alert):
    """Create and return a new user."""

    user = User(email = email, password = password, fname = fname, lname = lname, sign_up = sign_up, profile_pic = profile_pic, twilio_alert = twilio_alert)

    return user

def get_user_by_email(email):

    return User.query.filter_by(email = email).first()

def get_users_with_twilio_alert():

    return User.query.filter(User.twilio_alert == "Yes").all()

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
            "bonus_text":prompt.bonus_text,
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

    available_prompts= JournalPrompt.query.filter((JournalPrompt.week >= sign_up_week) & (JournalPrompt.week <= current_week)).order_by(JournalPrompt.week.desc()).all()

    return available_prompts

def prompts_available_to_user_json(user_id):
    """Return all prompts that user has access to"""    
    user = User.query.get(user_id)
    
    current_week = session['week']
    sign_up_week = datetime.strftime(user.sign_up, ("%U"))

    available_prompts= JournalPrompt.query.filter((JournalPrompt.week >= sign_up_week) & (JournalPrompt.week <= current_week)).order_by(JournalPrompt.week.desc()).all()
    json = []
    for prompt in available_prompts:
        prompt_dict = {
            "week": prompt.week,
            "prompt": prompt.prompt,
            "book": prompt.book,
            "bonus_text": prompt.bonus_text,
            "entry": None
            }
        entries_by_user= [entry for entry in prompt.entries if entry.user_id == user_id]
        if entries_by_user:
            prompt_dict['entry'] = entries_by_user[0].user_entry
        json.append(prompt_dict)
    
        # print("***", json)
    return json
    

def get_prompt_by_week(week):
    """Create and return a prompt"""
   
    current_prompt = JournalPrompt.query.get(week)
    
    return current_prompt

def save_new_entry(user_id, week, user_entry, entry_date, visibility, entry_modified, modified_date):

    entry = JournalEntry(user_id = user_id, week = week, user_entry = user_entry, entry_date = entry_date, visibility = visibility, entry_modified = entry_modified, modified_date = modified_date) 
    # entry = JournalEntry (user_id = user_id, week = week, user_entry = user_entry, entry_date = entry_date, visibility = visibility) 
    return entry

def get_entry_by_id(id):

    entry_id = JournalEntry.query.get(id)

    return entry_id


def get_all_user_entries(user_id):
    
    all_entries = JournalEntry.query.filter((JournalEntry.user_id == user_id) & (JournalEntry.visibility == 'Public') & (JournalEntry.user_entry != None)).order_by(JournalEntry.week.desc()).all()

    return all_entries

def get_entry_by_user_and_week(user_id, week):

    entry = JournalEntry.query.filter((JournalEntry.user_id == user_id) & (JournalEntry.week == week)).first()

    return entry


def get_public_entries():

    public = JournalEntry.query.filter(JournalEntry.visibility == 'Public').order_by(JournalEntry.week.desc()).all()

    return public 

def get_public_entries_json():

    
    public_entry = JournalEntry.query.filter(JournalEntry.visibility == 'Public').order_by(JournalEntry.week.desc()).all()
    
    json = []
    for entry in public_entry:
        entry_dict = {
            "fname": entry.user.fname, 
            "user_id":entry.user.id,
            "entry": entry.user_entry,
            "week": entry.week,
            "prompt_week": entry.prompt.week,
            "prompt": entry.prompt.prompt,
            "visibility": entry.visibility
        }
        json.append(entry_dict)
    print(json)
    return json


def get_friend_entries_json(user):
    public_entry = JournalEntry.query.filter(JournalEntry.visibility == 'Public').order_by(JournalEntry.week.desc()).all()
    users = []

    for user in user.following:
        users.append(user.id)

    # print("THESE ARE USERS", users)

    json = []
    
    # for friend in user.following:
    for entry in public_entry:
        # if the entry is written by someone in user.following
        if entry.user_id in users:
            following_entry_dict = {
                "fname": entry.user.fname, 
                "user_id":entry.user.id,
                "entry": entry.user_entry,
                "week": entry.week,
                "prompt_week": entry.prompt.week,
                "prompt": entry.prompt.prompt,
                "visibility": entry.visibility
            }
            json.append(following_entry_dict)
    print(json)
    return json

def delete_journal_entry(entry_id):

    entry = JournalEntry.query.get(entry_id)

    db.session.delete(entry)
    db.session.commit()




if __name__ == '__main__':
    from server import app
    connect_to_db(app)