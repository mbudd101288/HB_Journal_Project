"""Script to seed database."""

import os
import json 
import crud
import model
import server

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
    
    db_prompt = crud.create_weekly_prompt(journal_prompt, week)
    #Should db_prompt by db_JournalPrompt? 
    prompts_in_db.append(db_prompt)



model.db.session.add_all(prompts_in_db)
model.db.session.commit()

