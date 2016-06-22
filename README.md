# Python + falcon + whitenoise + AngularJS + Auth0 + Bootstrap3

This is a starter project for creating a web app based on the above technologies.

This project doesn't include any database setup.

## Getting started

1. Setup a virtualenv for python 3.5+
2. install
> pip install -r requirements.txt
3. start server
> gunicorn main:application
or with automatic python reloading
> gunicorn main:application --reload

Open http://localhost:8000 in your browser.

You'll probably want to rename the app to something else.

If you're using Heroku the runtime.txt and Procfile files are included.

Enjoy!
