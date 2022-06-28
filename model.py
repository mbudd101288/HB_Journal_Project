"""Models for 52 Weeks Journal App."""

from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class User(db.Model):

    __tablename__='users'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    email = db.Column(db.String(), unique = True, nullable = False)
    fname = db.Column(db.String(), nullable =False)
    lname = db.Column(db.String())
    password = db.Column(db.String(), nullable = False)
    profile_pic = db.Column(db.String(), default = None)
    sign_up = db.Column(db.Date, default = date.today())

    #entries = db.relationship('JournalEntry', backref = 'user')

    def __repr__(self):
        return f"<User email = {self.email} sign_up={self.sign_up} >"


class JournalEntry(db.Model):

    __tablename__='entries'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    week = db.Column(db.Integer, db.ForeignKey('prompts.week'), nullable = False)
    entry_date = db.Column(db.Date, default = date.today())
    user_entry = db.Column(db.Text)
    entry_modified = db.Column(db.Boolean, default = False)
    modified_date = db.Column(db.Date, default = None, onupdate = date.today())
    visibility = db.Column(db.String(), default = 'Private')

    prompt = db.relationship('JournalPrompt', backref = 'entries')
    user = db.relationship('User', backref = 'entries')

    def __repr__(self):
        return f"<JournalEntry user_id = {self.user_id} journal_id = {self.id} entry_date = {self.entry_date} user_entry = {self.user_entry} visibility = {self.visibility}>"

class JournalPrompt(db.Model):

    __tablename__="prompts"

    week = db.Column(db.Integer, primary_key = True)    
    prompt = db.Column(db.String)
    book = db.Column(db.String(), default = None)
    bonus_text = db.Column(db.String(), default = None)
  

    

    #entries = db.relationship('JournalEntry', backref = 'prompt')

    def __repr__(self):
         return f"<JournalPrompt prompt = {self.prompt}: release_week= {self.week}>"


def connect_to_db(flask_app, db_uri="postgresql:///journals", echo=True):
    # make sure db is called journals or else need to change above
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
    db.create_all()
    #connects database to flask