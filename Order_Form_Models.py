from datetime import datetime
from hashlib import md5
from time import time
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import app, db, login
from models import User

class Sample_Order(db.Model):
    """db for creating histology orders"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    species = db.Column(db.String(255))
    tissue_types = db.Column(db.String(255))
    wet_samples = db.Column(db.String(255))
    cassettes = db.Column(db.String(255))
    paraffin_blocks = db.Column(db.String(255))
    fixative_used = db.Column(db.String(255))
    time_in_fixative = db.Column(db.String(255))
    current_storage = db.Column(db.String(255))
    time_in_current_storage = db.Column(db.String(255))
    decal = db.Column(db.Boolean)
    orientation = db.Column(db.String(255))
    slides_per_sample = db.Column(db.Integer)
    sections_per_slide = db.Column(db.Integer)
    section_thickness = db.Column(db.Integer)
    number_of_H_E = db.Column(db.Integer)
    special_stain_name = db.Column(db.String(255))
    number_of_specials = db.Column(db.Integer)
    region_of_interest = db.Column(db.String(2000))
    special_instructions = db.Column(db.String(2000))
    turn_around_time = db.Column(db.Integer)
    slide_scanning = db.Column(db.Boolean)
