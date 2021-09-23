from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from models import User
from flask_login import current_user
import email_validator

"""
Purpose: This file contains class definitions for the various forms used in the app.
"""


class LoginForm(FlaskForm):
    email = StringField(('E-mail'), validators=[DataRequired()])
    password = PasswordField(('Password'), validators=[DataRequired()])
    remember_me = BooleanField(('Remember Me'))
    submit = SubmitField(('Sign In'))


class RegistrationForm(FlaskForm):
    first_name = StringField(('First Name'), validators=[DataRequired()])
    last_name = StringField(('Last Name'), validators=[DataRequired()])
    email = StringField(('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        ('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('password')])
    address_1 = StringField(('Address 1'), validators=[DataRequired()])
    address_2 = StringField(('Address 2'), validators=[DataRequired()])
    city = StringField(('City'), validators=[DataRequired()])
    state = StringField(('State'), validators=[DataRequired()])
    zipcode = StringField(('Zipcode'), validators=[DataRequired()])
    telephone = StringField(('Telephone'), validators=[DataRequired()])
    submit = SubmitField(('Submit'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(('Please use a different email address.'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(('Request Password Reset'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        ('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(('Request Password Reset'))


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField(('Current Password'), validators=[DataRequired()])
    new_password = PasswordField(('New Password'), validators=[DataRequired()])
    new_password2 = PasswordField(
        ('Repeat New Password'), validators=[DataRequired(),
                                           EqualTo('new_password')])
    submit = SubmitField(('Change Password'))

    def validate_current_password(self, current_password):
        if not current_user.check_password(current_password.data):
            raise ValidationError('Invalid current password, please try again.')


class EditProfileForm(FlaskForm):
    first_name = StringField(('First Name'), validators=[DataRequired()])
    last_name = StringField(('Last Name'), validators=[DataRequired()])
    email = StringField(('Email'), validators=[DataRequired(), Email()])
    address_1 = StringField(('Address 1'), validators=[DataRequired()])
    address_2 = StringField(('Address 2'), validators=[DataRequired()])
    city = StringField(('City'), validators=[DataRequired()])
    state = StringField(('State'), validators=[DataRequired()])
    zipcode = StringField(('Zipcode'), validators=[DataRequired()])
    telephone = StringField(('Telephone'), validators=[DataRequired()])
    submit = SubmitField(('Submit'))
