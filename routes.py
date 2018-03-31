# -*- coding: utf-8 -*-
from app import app, socketio, db
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from models import User
from werkzeug.urls import url_parse
from forms import LoginForm, RegistrationForm, EditProfileForm,  \
    ResetPasswordRequestForm, ResetPasswordForm, ChangePasswordForm
from datetime import datetime

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/chat')
def chat():
    return render_template('chat.html', async_mode=socketio.async_mode)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
#@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, email=form.email.data,
        last_name=form.last_name.data, address_1=form.address_1.data,
        address_2=form.address_2.data, city=form.city.data, state=form.state.data,
        zipcode=form.zipcode.data, telephone=form.telephone.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(('Congratulations, you are now a registered user!'))
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
@app.route('/edit_profile')
def edit_profile():
    return ("profile page")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(('Invalid username or password'))
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash(
            ('Check your email for the instructions to reset your password'))
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)
