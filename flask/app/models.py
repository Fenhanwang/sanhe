# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app         import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id       = db.Column(db.Integer,     primary_key=True)
    user     = db.Column(db.String(64),  unique = True)
    email    = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(500))
    token    = db.Column(db.String(500), unique = True)

    def __init__(self, user, email, password, token=None):
        self.user       = user
        self.password   = password
        self.email      = email
        self.token      = token

    def __repr__(self):
        return str(self.id) + ' - ' + str(self.user)

    def save(self):

        # inject self into db session    
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self
    
    def update(self, token) -> None:
        self.verified   = True
        self.token      = token
        db.session.commit()
        
        return self
