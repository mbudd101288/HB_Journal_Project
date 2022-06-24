from datetime import date
from time import strftime, time
from flask import Flask, redirect, request, render_template, session, flash, jsonify
from jinja2 import StrictUndefined
import os
import crud
from model import connect_to_db, db

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

app.secret_key = "SECRET_KEY"
# API_KEY = os.environ['TWILIO_KEY', 'GIPHY_KEY']


@app.route("/")
def homepage():
    
    if "user" in session:
        return redirect("/my-journal")

    return render_template("homepage.html")

@app.route('/users', methods=['POST'])
def new_user():
    
    email = request.form.get("email")
    password = request.form.get("password")
    fname = request.form.get("fname")
    lname = request.form.get("lname")

    user = crud.get_user_by_email(email)
    if user:
        flash("Email already exists. Try again.")
    else:
        user = crud.create_user(email, password, fname, lname, sign_up= date.today(), profile_pic = None)
        session['user'] = user.email
        db.session.add(user)
        db.session.commit()
        flash(f"User created. Welcome {user.fname}")
    
    return redirect('/my-journal')

@app.route('/login', methods=['POST'])
def get_login_info():

    email = request.form.get("email")
    password = request.form.get("password") 
    

    user = crud.get_user_by_email(email)
    
    if user:
        if password == user.password:
            session['user']= user.email
            return redirect ("/my-journal")
            # week = session['week']
            # current_prompt = crud.get_prompt_by_week(week)
            # return render_template ("my-journal.html", user = user, prompt = current_prompt)
             
        else:
            flash('Incorrect password. Try again.')
    else:
        flash('Email not found. Try again')

    return redirect("/")
    
@app.route("/my-journal")
def show_user_journal():
    if 'user' not in session:
        print('not in session')
        return render_template("homepage.html")
    else:
        session['date'] = date.today()
        session['week'] = strftime("%U")
        user = crud.get_user_by_email(session['user'])
        current_prompt = crud.get_prompt_by_week(session['week'])
        return redirect(f"/update-prompt-entry/{session['week']}")

@app.route("/get-user-entries.json")
def get_user_entries():

    user = crud.get_user_by_email(session['user'])
    user_id = user.id
    prompts = crud.prompts_available_to_user_json(user_id)
    
    return jsonify(prompts)

@app.route("/entry/<user_id>")
def get_additional_entries_by_user(user_id):
    """Can view more entries from a specific user on their user-page"""
    user = crud.get_user_by_id(user_id)
    entries = crud.get_all_user_entries(user_id)
    if user.email != session['user']:
        return render_template('shared-user-page.html', user = user, entries = entries)
    else:
        return render_template ('user-page.html', user = user, entries = entries)

@app.route("/entry", methods=['GET'])
def show_user_entries ():
    user = crud.get_user_by_email(session['user'])

    return render_template ('user-page.html', user = user)

@app.route('/entry', methods=['POST'])
def create_current_entry():

    text_entry = request.form.get('entry')
    visibility = request.form.get('visibility')

    if "entry_id" in request.form:
        entry_id = request.form.get('entry_id')
        entry = crud.get_entry_by_id(entry_id)
        entry.modified_entry = True
        entry.date_modified = date.today()
        entry.visibility = request.form.get('visibility')
        entry.user_entry = request.form.get('entry')
    
    else:
        user = crud.get_user_by_email(session['user'])
        new_entry = crud.save_new_entry(user.id, session['week'], text_entry, session['date'], entry_modified, date_modified, visibility)
        db.session.add(new_entry)
    db.session.commit()
    
    
    flash(f'Journal Entry saved. Visibility: {visibility}')
    return redirect('/entry')
    # return render_template('user-page.html', new_entry = new_entry, user = user)

    # In the server, access the entry_id using request.form
    # If an entry_id exists, use a crud function to get the entry by id
    #   update the entry_modified field and the user_entry field using inputs from the form.
    # How to update a record in a db:
    # example_entry.entry_modified = True
    # example_entry…. Update other fields


@app.route("/update-prompt-entry/<week>")
def edit_entry(week):
    """Can complete or edit an existing entry which will render on the my-journal.html"""
    user = crud.get_user_by_email(session['user'])
    prompt = crud.get_prompt_by_week(week)
    entry = crud.get_entry_by_user_and_week(user.id, week)

    return render_template('my-journal.html', user = user, prompt = prompt, entry = entry)

# @app.route("/create-prompt-entry/<week>")
# def create_entry(week):
#     """Can select a prompt to create an entry for - will render on the my-journal.html"""
#     user = crud.get_user_by_email(session['user'])
#     prompt = crud.get_prompt_by_week(week)

#     return render_template('my-journal.html', user = user, prompt = prompt)

@app.route("/get-shared-entries.json")
def get_community_journal_entries ():

    shared_entries = crud.get_public_entries_json()

    return jsonify(shared_entries)
   
@app.route("/shared-entries", methods=['GET'])
def view_community_journal_entries ():

    user = crud.get_user_by_email(session['user'])
   
    return render_template ('shared-entries.html', user = user)

    
@app.route("/logout")
def logout ():

    session.pop('user')

    return redirect ("/")
   

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")