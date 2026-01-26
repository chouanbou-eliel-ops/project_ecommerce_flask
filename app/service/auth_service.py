from app.models.admin import Admin
from app.models.user import User
from app.extensions import db

def create_admin(username, email, password):
    admin = Admin(username=username, email=email, password=password)
    db.session.add(admin)
    db.session.commit()
    return admin

def create_user(username, email, password):
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def login(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        return False
    if not user.check_password(password):
        return False
    return user
