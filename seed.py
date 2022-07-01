"""Script to seed database."""

import os
import json 
import crud
import model
import server
from datetime import datetime

os.system("dropdb journals")
os.system('createdb journals')

model.connect_to_db(server.app)
model.db.create_all()


with open('data/prompts.json') as p:
    prompt_data= json.loads(p.read())

# Create prompts store them in list
prompts_in_db = []
for prompt in prompt_data:

    journal_prompt = prompt["prompt"]
    week = prompt["week"]
    book = prompt["book"]
    bonus_text = prompt["bonus_text"]
    
    db_prompt = crud.create_weekly_prompt(journal_prompt, week, book, bonus_text)
    #Should db_prompt by db_JournalPrompt? 
    prompts_in_db.append(db_prompt)

with open('data/users.json') as u:
    user_data= json.loads(u.read())

# Create prompts store them in list
users_in_db = []
for user in user_data:

    email = user["email"]
    password = user["password"]
    fname = user["fname"]
    lname = user["lname"]
    sign_up = datetime.strptime(user["sign_up"], "%Y-%m-%d")
    profile_pic = user["profile_pic"]
    twilio_alert= user["twilio_alert"]
    
    db_user = crud.create_user(email, password, fname, lname, sign_up, profile_pic, twilio_alert) 
    users_in_db.append(db_user)

with open('data/entries.json') as e:
    entry_data= json.loads(e.read())

entries_in_db = []
for entry in entry_data:

    user_id = entry["user_id"]
    week = entry["week"]
    user_entry = entry["user_entry"]
    entry_date = datetime.strptime(entry["entry_date"], "%Y-%m-%d")
    visibility = entry["visibility"]
    entry_modified = entry["entry_modified"]
    modified_date = entry["modified_date"]
    
    
    db_entry = crud.save_new_entry(user_id, week, user_entry, entry_date, visibility, entry_modified, modified_date)
    entries_in_db.append(db_entry)

model.db.session.add_all(users_in_db)
model.db.session.add_all(prompts_in_db)
model.db.session.add_all(entries_in_db)
model.db.session.commit()

