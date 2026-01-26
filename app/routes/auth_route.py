from urllib import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user

#from models.models import User
#from app_LSI import db

auth = Blueprint('auth', __name__)

# User.query.filter_by permet de savoir si un element est dans la db user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username = request.form['username']).first()
        if user and check_password_hash(user.password, password) :
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash("Identifiants incorrects.")
    return render_template('login.html')

"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == '':
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid username or password')

        #reflechir sur comment implementer une base de données (table client, admin etc)
"""

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # ceci nous permettra d'eviter les doublons
        user_exist = User.query.filter_by(username=username).first()
        if user_exist:
            flash("Username already exists")
            return redirect(url_for('auth.register'))

        #Hash du mot de passe
        hashed_password = generate_password_hash(password, method='sha256')

        # Creation utilisateur
        new_user = User(username, hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('main.home'))
    return render_template('register.html')
