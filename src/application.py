# -*- coding: utf-8 -*-
import os
from flask import Flask

from app_config import BaseConfig, DevConfig
from views import top


def _get_config_obj():
    env = os.environ.get('APP_ENVIRONMENT', 'prod')
    if env == 'devel':
        return 'app_config.DevConfig'
    else:
        return 'app_config.BaseConfig'

app = Flask(__name__)
conf = _get_config_obj()
app.config.from_object(conf)
app.register_blueprint(top.app)

if __name__ == '__main__':
    app.run()
