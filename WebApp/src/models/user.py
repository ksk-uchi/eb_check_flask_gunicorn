# -*- coding: utf-8 -*-

from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.relationship('EmailAddress', backref=db.backref('user', lazy='joined'),
                                lazy='dynamic')

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username


class EmailAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))