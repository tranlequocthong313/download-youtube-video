from flask import session, request, redirect, url_for
from models.user import User
from extensions import db
from config import username_session_key, email_session_key
from user.user_service import UserService


class AuthService:
    __user = UserService()

    def login(self):
        self.set_new_session()

        found_user = self.__user.find_user_by_name(
            request.form[username_session_key])
        if found_user:
            session[email_session_key] = found_user.email
        else:
            self.__user.add_new_user()

        return redirect(url_for('main.home'))

    def set_new_session(self):
        session.permanent = True
        session[username_session_key] = request.form[username_session_key]

    def is_login(self):
        return username_session_key in session
