# -*- coding: utf-8 -*-
from app import app, socketio
from flask import render_template


@app.route('/chat')
def chat():
    return render_template('chat.html', async_mode=socketio.async_mode, current_user='user')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
#@login_required
def index():
    ''' nothing here yet'''
    return render_template('index.html', title='Home', current_user='user')

@app.route('/edit_profile')
def edit_profile():
    return ("profile page")

@app.route('/login')
def login():
    return ("login page")

@app.route('/logout')
def logout():
    return ("logout page")
