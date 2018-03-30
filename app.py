# -*- coding: utf-8 -*-
from threading import Lock
from flask import Flask
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()
bootstrap = Bootstrap(app)

from routes import *
from websockets import *
