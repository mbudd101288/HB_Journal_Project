# Mindful Growth
>Mindful Growth is an online journaling app that releases scheduled weekly prompts. Users are able to maintain a private journal and/or connect and share entries with other users. The app also utilizes the Twilio SendGrid API in conjunction with a Cron Job to send an optional weekly email alerting a user that a new journal prompt is available. 

## Technologies
Tech Stack: 
* Python
* Javascript
* Flask
* SQLAlchemy
* AJAX/JSON
* Jinja2
* HTML/CSS
* Bootstrap
* Argon2
* Cron

API: 
* Twilio SendGrid

## Features

## Installation

Prerequisites:
* Sign up for Twilio SendGrid to receive API key - https://www.twilio.com/sendgrid/email-api

Clone Repository: 
```
$ git clone https://github.com/mbudd101288/HB_Journal_Project
```

Create and activate a virtual environment in your journal project directory:
```
$ virtualenv
$ source env/bin/activate
```

Install requirements:
```
$pip3 install -r requirements.txt
```

Create secrets.sh file to store sensitive keys:
* Flask app secret key 
* Twilio SendGrid secret key

Activate secrets in virtual environment:
```
$ source secrets.sh
```

Seed the database with prompts from prompts.json (may omit entries.json and users.json):
```
$ python3 seed.py
```

Run the server:
```
$ python3 server.py
```


## Next Steps
Once deployed, the Cron Job will be updated to improve functionality by calling the cloud server as opposed to my local (intermittently running) server. Twilio Sendgrid will be updated to include a link to the Mindful Growth login page. 

## About the Developer
Molli Budd is a software engineer living in Omaha, NE. She created her first project, Mindful Growth, during her fellowship at Hackbright Academy.