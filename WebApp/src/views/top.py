# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    request,
    current_app,
    render_template
)
from logging import getLogger

from models.user import User, EmailAddress
from models.page import *

app = Blueprint('top', __name__)
logger = getLogger(__name__)

def hello_top():
    isono_family = User.query.order_by(User.id).all()
    variables = {
        'proper_text': 'こんちわ',
        'whois': '三河屋',
        'b_and_s': isono_family
    }
    return render_template('toppage.html', **variables)

# This view including below URLs.
app.add_url_rule('/', 'top_index', hello_top)
