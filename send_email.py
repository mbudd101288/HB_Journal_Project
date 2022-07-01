import os
import crud
from flask import Flask
from time import strftime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To
from model import connect_to_db, db, JournalEntry, JournalPrompt, User
# 0 9 * * 0 sudo /Users/mollibudd/src/HB-project/env/bin/python3 /src/HB-project/send_email.py
# app = Flask(__name__)
# app.secret_key = "SECRET_KEY"


def send_email():

    users = crud.get_users_with_twilio_alert()
    week = strftime('%U')
    prompt = crud.get_prompt_by_week(week)

  
    for user in users:
        
        message = Mail(
            from_email="mbudd101288@gmail.com",
            # from_email=os.environ.get('MAIL_DEFAULT_SENDER'),
            to_emails=user.email,

            subject='New weekly journal prompt available',
            html_content=f'Week {prompt.week}: {prompt.prompt}')
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    send_email()
    # app.run(debug=True, host="0.0.0.0")

