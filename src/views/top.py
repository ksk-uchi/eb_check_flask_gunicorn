# -*- coding: utf-8 -*-
from flask import Blueprint, request, current_app, abort
from logging import getLogger

app = Blueprint('top', __name__)
logger = getLogger('views.api')

@app.route('/')
def hello_top():
    return 'こんちわ'
