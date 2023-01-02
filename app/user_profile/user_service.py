
from flask import session
from models.user import User
from extensions import db
from config import username_session_key, email_session_key


class UserService:
    def find_user_by_name(self, username):
        return User.query.filter_by(
            name=username).first()

    def add_new_user(self):
        user = User(session[username_session_key], None)
        db.session.add(user)
        db.session.commit()

    def update_email(self, new_email):
        self.find_user_by_name(
            session[username_session_key]).email = new_email
        db.session.commit()
        session[email_session_key] = new_email

    def has_set_email_already(self):
        return email_session_key in session
