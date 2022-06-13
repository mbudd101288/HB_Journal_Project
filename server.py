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

@app.route("/login", methods=["POST"])
def get_login_info():

    email = request.form.get("email")
    password = request.form.get("password") 

    user = crud.get_user_by_email(email)
    
    if user:
        if password == user.password:
            session['user_email']= user.email
            flash(f"{user.email}, you're logged in.")
        else:
            flash('Incorrect password. Try again.')
    else:
        flash('Email not found. Try again')

    return redirect("/my-journal")

@app.route("/my-journal", methods=["POST"])
def get_name():
    
    
    # if require to insert a name per the form
    #  username = request.args['name']
    # can call this way instead of with .get because it was required input by the homepage

    

    return render_template("my-journal.html")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")