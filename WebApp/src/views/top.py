# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    request,
    current_app,
    render_template
)
from logging import getLogger

app = Blueprint('top', __name__)
logger = getLogger('views.api')

def hello_top():
    logger.debug('here')
    variables = {
        'proper_text': 'こんちわ',
        'whois': '三河屋',
        'b_and_s': ['サザエ', 'かつお', 'わかめ']
    }
    return render_template('toppage.html', **variables)

# This view including below URLs.
app.add_url_rule('/', 'top_index', hello_top)
