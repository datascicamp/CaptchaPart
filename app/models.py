from app import db
from datetime import datetime


class CaptchaMatching(db.Model):
    # name of database
    __tablename__ = "CaptchaMatching"

    id = db.Column(db.Integer, primary_key=True)
    hash_code = db.Column(db.String(64), index=True, unique=True)
    captcha_code = db.Column(db.String(120), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<hash_code={}, captcha_code={}>'.format(self.hash_code, self.captcha_code)

    # for api usage
    def to_dict(self):
        data = {
            'hash_code': self.hash_code,
            'captcha_code': self.captcha_code,
            'timestamp': self.timestamp,
        }
        return data

