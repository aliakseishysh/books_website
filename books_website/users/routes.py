from flask import Blueprint, render_template, redirect, url_for

from books_website import bcrypt, db
from books_website.models import User
from books_website.users.forms import RegistrationForm, LoginForm
from flask_login import current_user, login_user, logout_user

users = Blueprint('users', __name__)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(user.password, form.password.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.home'))
    return render_template('login.html', title='Авторизация', form=form)


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Регистрация', form=form)


@users.route('/account')
def account():
    return render_template('account.html', title='Профиль')


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))










