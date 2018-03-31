# -*- coding: utf-8 -*-
from threading import Lock
from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
from flask_mail import Mail

async_mode = None

app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
mail = Mail(app)


from models import User
from routes import before_request,chat,index,register,login,logout,reset_password_request,edit_profile,reset_password,change_password
from websockets import background_thread,test_broadcast_message,join,leave,disconnect_request,test_connect,test_disconnect
