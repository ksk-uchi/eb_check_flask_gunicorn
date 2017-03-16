# -*- coding: utf-8 -*-

from models import db
from application import app

with app.app_context():
    db.create_all()

