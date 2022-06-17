from datetime import date
from time import strftime, time
from flask import Flask, redirect, request, render_template, session, flash
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
        user = crud.create_user(email, password, fname, lname)
        db.session.add(user)
        db.session.commit()
        flash("User created. Please log in.")
    
    return redirect('/')

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
        return render_template("my-journal.html", prompt = current_prompt, user = user)

@app.route("/entry", methods=["POST"])
def create_current_entry():
    
    entry = request.form.get('entry')
    visibility = request.form.get('visibility')
    user = crud.get_user_by_email(session['user'])
    new_entry = crud.save_new_entry(user.id, session['week'], entry, session['date'], visibility)
    
    db.session.add(new_entry)
    db.session.commit()
    
    flash(f'Journal Entry saved. Visibility: {visibility}')
    return render_template('user-page.html', new_entry = new_entry, user = user)

@app.route("/logout")
def logout ():

    session.pop('user')

    return redirect ("/")
   

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")