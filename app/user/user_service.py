from flask import session
from models.user import UserModel
from extensions import db
from config import username_session_key, email_session_key
from models.video import VideoModel


class UserService:
    def find_user_by_name(self, username):
        return UserModel.query.filter_by(
            name=username).first()

    def add_new_user(self):
        user = UserModel(session[username_session_key], None)
        db.session.add(user)
        db.session.commit()

    def update_email(self, new_email):
        self.find_user_by_name(
            session[username_session_key]).email = new_email
        db.session.commit()
        session[email_session_key] = new_email

    def add_new_downloaded_video(self, video):
        user = self.find_user_by_name(session[username_session_key])
        downloaded_video = VideoModel(video, user.id)
        db.session.add(downloaded_video)
        db.session.commit()
