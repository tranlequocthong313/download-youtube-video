import os
from datetime import timedelta

username_session_key = 'username'
email_session_key = 'email'


class Config:
    SECRET_KEY = os.environ.get('SESSION_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=60)
