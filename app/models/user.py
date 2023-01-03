from extensions import db


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    downloaded_videos = db.relationship('Video', backref='user')

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
