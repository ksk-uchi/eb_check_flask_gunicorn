# -*- coding: utf-8 -*-
from flask import Blueprint, request, current_app

app = Blueprint('top', __name__, url_prefix='/top')

@app.route('/')
def hello_top():
    current_app.logger.info('\n'.join(dir(request)))
    return 'こんちわ'