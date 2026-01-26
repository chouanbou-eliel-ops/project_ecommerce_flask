from app.extensions import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total = db.Column(db.Integer, nullable=False)
    def __init__(self, user_id, total):
        self.user_id = user_id
        self.total = total

