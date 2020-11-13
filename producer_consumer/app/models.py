from app import db
from datetime import datetime

class Msg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    msg_num = db.Column(db.Integer, index=True)
    time = db.Column(db.Float, index = True)
    

    def __repr__(self):
        return '<Msg {}>'.format(self.msg_num)