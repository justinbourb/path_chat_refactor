# -*- coding: utf-8 -*-
from app import app, socketio, db
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from models import User
from Order_Form_Models import Sample_Details, Histology_Details
from werkzeug.urls import url_parse
from forms import LoginForm, RegistrationForm, EditProfileForm,  \
    ResetPasswordRequestForm, ResetPasswordForm, ChangePasswordForm
from datetime import datetime
from email_file import send_password_reset_email

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/chat')
@login_required
def chat():
    return render_template('chat.html', async_mode=socketio.async_mode)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
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

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """allows users to update info / edit profile"""
    form = EditProfileForm()
    if request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
        form.address_1.data = current_user.address_1
        form.address_2.data = current_user.address_2
        form.city.data = current_user.city
        form.state.data = current_user.state
        form.zipcode.data = current_user.zipcode
        form.telephone.data = current_user.telephone
    if form.validate_on_submit():
        form.last_name.data = form.last_name.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        current_user.address_1 = form.address_1.data
        current_user.address_2 = form.address_2.data
        current_user.city = form.city.data
        current_user.state = form.state.data
        current_user.zipcode = form.zipcode.data
        current_user.telephone = form.telephone.data
        db.session.commit()
        flash(('Your changes have been saved.'))

        return redirect(url_for('edit_profile'))

    return render_template('edit_profile.html', title=('Edit Profile'),
                           form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash(('Your password has been reset.'))
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        current_user.set_password(form.new_password.data)
        db.session.commit()
        flash(('Your password has been changed.'))
        return redirect(url_for('edit_profile'))
    return render_template('change_password.html', form=form)

@app.route('/new_order', methods=['GET', 'POST'])
@login_required
def new_order():
    form = Sample_Details_Form()
    if form.validate_on_submit():
        sample_details = Sample_Details(species=form.species.data, tissue_types=form.tissue_types.data,
        wet_samples=form.wet_samples.data, cassettes=form.cassettes.data, paraffin_blocks=form.paraffin_blocks.data,
        fixative_used=form.fixative_used.data, time_in_fixative=form.time_in_fixative.data,
        current_storage=form.current_storage.data, time_in_current_storage=form.time_in_current_storage.data)
        db.session.add(sample_details)
        db.session.commit()
        flash(sample_details)
        return redirect(url_for('index'))
    return render_template('new_order.html', title='New Order', form=form)
