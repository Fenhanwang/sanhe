# coding: utf-8
# https://github.com/marcelomd/flask-wtf-login-example/tree/master/app

from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError
# from .models import User


class LoginForm(FlaskForm):
    email = StringField('Email',
            validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    def validate(self, extra_validators=None):
        initial_validation = super().validate(extra_validators)
        if not initial_validation:
            return False
        return True
        user = User.query.filter_by(email=self.email.data).first()
        if not user:
            self.email.errors.append('Unknown email')
            return False
        if not user.verify_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False
        return True


class RegisterForm(FlaskForm):
    username = StringField('Username',
            validators=[DataRequired(), Length(min=3, max=32)])
    email = StringField('Email',
            validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password',
            validators=[DataRequired(), Length(min=8, max=64)])
    confirm = PasswordField('Verify password',
            validators=[DataRequired(), EqualTo('password',
            message='Passwords must match')])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate(self, extra_validators=None):
        initial_validation = super().validate(extra_validators)
        if not initial_validation:
            return False
        return True
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("Username already registered")
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True
