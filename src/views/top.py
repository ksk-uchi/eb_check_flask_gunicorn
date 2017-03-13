# -*- coding: utf-8 -*-
from flask import Blueprint, request, current_app
import logging

app = Blueprint('top', __name__, url_prefix='/top')

@app.route('/')
def hello_top():
    return 'こんちわ'