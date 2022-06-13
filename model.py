"""Models for 52 Weeks Journal App."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

db = SQLAlchemy()

class User(db.model):

    __tablename__='users'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    email = db.Column(db.String(), Unique = True, nullable = False)
    password = db.Column(db.String(), nullable = False)
    profile_pic = db.Column(db.String())
    sign_up = db.Column(db.DateTime)

    #entries = db.relationship('JournalEntry', backref = 'user')

    def __repr__(self):
        return f"<User email = {self.email} sign_up={self.sign_up} >"


class JournalEntry(db.model):

    __tablename__='entries'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable = False)
    journal_id = db.Columb(db.Integer, ForeignKey('journal.id'), nullable = False)
    entry_date = db.Column(db.DateTime, default = func.now())
    user_entry = db.Column(db.Text)
    entry_modified = db.Column(db.Bool, default = False)
    modified_date = db.Column(db.DateTime, default = None, onupdate = func.current_timestamp())
    visibility = db.Column(db.String(), default = 'Private')

    prompt = db.relationship('JournalPrompt', backref = 'entries')
    user = db.relationship('User', backref = 'entries')

    def __repr__(self):
        return f"<JournalEntry user_id = {self.user_id} journal_id = {self.journal_id} entry_date = {self.entry_date} user_entry = {self.user_entry} visibility = {self.visibility}>"

class JournalPrompt(db.model):

    __tablename__="prompts"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)    
    prompt = db.Column(db.Text)
    release_date= db.Column(db.DateTime, nullable = False)

    #entries = db.relationship('JournalEntry', backref = 'prompt')

    def __repr__(self):
         return f"<JournalPrompt prompt = {self.prompt}: release_date = {self.release_date}>"


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
    #connects database to flask