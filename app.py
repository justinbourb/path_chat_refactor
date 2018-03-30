# -*- coding: utf-8 -*-
from threading import Lock
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap

async_mode = None

app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *
from routes import *
from websockets import *
