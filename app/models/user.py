from app.extensions import db
from flask_login import UserMixin

class User (UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)# est ce que le unqiue ci est vraiment necessaire
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        def __repr__(self):
            return '<User %r>' % self.username

