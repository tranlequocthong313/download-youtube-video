from extensions import db


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    videoId = db.Column(db.String(20))
    quality = db.Column(db.String(20))
    destination = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, video, user_id: int) -> None:
        self.videoId = video.id
        self.quality = video.quality
        self.destination = video.destination
        self.user_id = user_id
